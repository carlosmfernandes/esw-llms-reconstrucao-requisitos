#!/usr/bin/env python3
"""
Script para SER EXECUTADO NO SEU COMPUTADOR (não no ambiente do Claude).

ATENÇÃO (13/09/2026): este script agora cuida SOMENTE de OpenAI e
Anthropic — os dois já estão em 30/30 respostas válidas e PROTEGIDAS
(nunca sobrescritas, ver seção de proteção abaixo). Google e DeepSeek
foram removidos daqui de propósito e passaram a ter scripts próprios e
isolados:
  - executar_google_36.py  -> só gemini-3.6-flash, só resultados/google-gemini-3.6-flash/
  - executar_google_38.py  -> só gemini-3.8-flash, só resultados/google-gemini-3.8-flash/
  - executar_deepseek.py   -> só DeepSeek, só resultados/deepseek/
Isso existe para que rodar este script (ou os outros três) nunca tenha
como tocar acidentalmente nos resultados de um provedor diferente — cada
script só conhece o nome da própria pasta de saída, em código.

O que faz:
  - Lê manifest.json (as 30 unidades selecionadas + gabarito oficial)
  - Para cada unidade, monta o prompt padronizado (prompt_padrao.md)
  - Envia UMA ÚNICA VEZ (sem refinamento) para OpenAI e Anthropic
  - Salva cada resposta bruta em resultados/<llm>/<CT_id>.md

Segurança: este script NUNCA deve conter chaves de API escritas no código.
Ele lê as chaves de variáveis de ambiente. Configure-as no terminal antes
de rodar (exemplos abaixo) — NÃO em um arquivo de texto dentro de uma
pasta sincronizada com o Claude.

    export OPENAI_API_KEY="sk-..."
    export ANTHROPIC_API_KEY="sk-ant-..."

Instalação das dependências (uma vez):
    pip install openai anthropic "Brotli>=1.1.0" --break-system-packages

    O "Brotli>=1.1.0" NÃO é opcional. Os SDKs da OpenAI e da Anthropic usam
    httpx2, que descomprime respostas brotli chamando
    Decompressor.process(data, output_buffer_limit=...). Esse parâmetro só
    existe a partir do Brotli 1.1.0. Com o Brotli 1.0.9 (versão que vinha no
    Anaconda), TODA chamada falha com "TypeError: process() takes no keyword
    arguments", que o SDK mascara como um genérico "Connection error." — foi
    exatamente esse o falso "problema de rede" das rodadas de 13/09/2026.

Uso:
    python3 executar_experimento.py                 # roda todos os LLMs configurados, todas as 30 unidades
    python3 executar_experimento.py --llm openai     # roda só um provedor
    python3 executar_experimento.py --unidade CT05   # roda só uma unidade (teste rápido)
    python3 executar_experimento.py --dry-run        # só mostra os prompts, não chama nenhuma API

Sobre os nomes de modelo (leia isso antes de rodar tudo):
    Os nomes de modelo de cada provedor mudam com frequência. Para cada
    provedor, o script tenta uma LISTA de candidatos (ver PROVIDERS
    abaixo) e usa automaticamente o primeiro que responder sem erro —
    você verá no terminal a linha "[modelo confirmado] <provedor> -> <nome>"
    dizendo qual foi usado de fato. Se TODOS os candidatos de um provedor
    falharem, ele é pulado e o motivo é impresso; nesse caso, confira o
    nome correto na documentação oficial do provedor e adicione-o à lista
    em PROVIDERS. Recomendo testar antes com:
        python3 executar_experimento.py --unidade CT05
    (chama só 1 unidade em vez das 30, para validar rápido que as 4 APIs
    estão respondendo antes de rodar o lote completo).
"""
import argparse
import json
import os
import sys
import time
import traceback


def describe_error(e):
    """Monta uma descrição detalhada do erro, incluindo a cadeia de causas
    (__cause__/__context__). O SDK da OpenAI/Anthropic costuma resumir tudo
    como "Connection error." na mensagem principal, escondendo o motivo
    real (timeout? DNS? SSL?) um ou dois níveis abaixo, em __cause__. Isso
    existe porque tentamos 2 rodadas reais e o "Connection error." sozinho
    não foi suficiente pra diagnosticar — precisamos ver o que está por
    trás dele desta vez."""
    parts = [f"{type(e).__name__}: {e}"]
    cause = e.__cause__ or e.__context__
    seen = set()
    while cause is not None and id(cause) not in seen:
        seen.add(id(cause))
        parts.append(f"  causado por -> {type(cause).__name__}: {cause}")
        cause = cause.__cause__ or cause.__context__
    return "\n".join(parts)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MANIFEST_PATH = os.path.join(BASE_DIR, "manifest.json")
RESULTS_DIR = os.path.join(BASE_DIR, "resultados")

PROMPT_TEMPLATE = """Você receberá um trecho de código-fonte extraído de uma biblioteca real de \
manipulação de datas (TypeScript). Analise o código e responda, de forma objetiva:

1. Qual é o requisito funcional que esta função implementa? (o que ela faz, do ponto de vista de \
quem especificou o software — não uma descrição linha a linha do código)
2. Quais são os parâmetros de entrada e o que cada um representa?
3. O que a função retorna?

Não presuma nada além do que está no código abaixo. Não pesquise o nome da função em nenhuma \
fonte externa — baseie-se exclusivamente na leitura do código fornecido.

Código:
```typescript
{codigo}
```"""

# Modelo(s) de cada provedor — LISTA de candidatos, na ordem em que serão
# tentados. Restrito a OpenAI e Anthropic de propósito (ver nota no topo
# do arquivo) — os dois já confirmados em 30/30, model fixo e sem mistura.
PROVIDERS = {
    "openai": {"env": "OPENAI_API_KEY", "models": ["gpt-6-astra", "gpt-5.6-sol", "gpt-4o"]},
    "anthropic": {"env": "ANTHROPIC_API_KEY", "models": ["claude-sonnet-5"]},
}


def load_manifest():
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


# --- Proteção dos arquivos de resultado já gerados -------------------------
#
# Cada arquivo de resultado começa com um marcador oculto (comentário HTML,
# invisível ao renderizar o .md) dizendo se aquela resposta é válida:
#   <!-- STATUS: OK -->     -> resposta real do LLM, NUNCA é sobrescrita
#   <!-- STATUS: ERROR -->  -> só tem erro salvo, pode ser tentada de novo
# Isso é mais confiável que procurar o texto "ERRO AO CHAMAR API" dentro da
# resposta (um LLM poderia, em teoria, escrever essa frase por acaso ao
# comentar tratamento de erro no próprio código-fonte da unidade).
STATUS_MARKER_OK = "<!-- STATUS: OK -->"
STATUS_MARKER_ERROR = "<!-- STATUS: ERROR -->"


def read_status(path):
    """Lê o status de um arquivo de resultado já existente. Arquivos
    antigos (gerados antes desse marcador existir) são tratados como ERROR
    por segurança, então entram no fluxo de backup+nova tentativa em vez de
    serem silenciosamente aceitos como válidos sem checagem."""
    with open(path, encoding="utf-8") as f:
        head = f.read(200)
    if STATUS_MARKER_OK in head:
        return "OK"
    if STATUS_MARKER_ERROR in head:
        return "ERROR"
    # Arquivo de formato antigo (sem marcador): usa a heurística antiga como
    # fallback, só para não tratar como erro os resultados bons já obtidos
    # antes desta versão do script.
    with open(path, encoding="utf-8") as f:
        content = f.read()
    return "ERROR" if "ERRO AO CHAMAR API" in content else "OK"


def backup_previous_attempt(out_path, prov_name):
    """Move (não apaga) a tentativa anterior com erro para uma subpasta de
    backup antes de tentar de novo, para nunca perder rastro do que
    aconteceu, mesmo em uma resposta que será substituída."""
    backup_dir = os.path.join(RESULTS_DIR, prov_name, "_tentativas_anteriores")
    os.makedirs(backup_dir, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    base = os.path.basename(out_path)
    backup_path = os.path.join(backup_dir, f"{base}.{stamp}.bak")
    os.replace(out_path, backup_path)


def write_result_file(out_path, item, prov_name, working_model, resposta, status):
    marker = STATUS_MARKER_OK if status == "OK" else STATUS_MARKER_ERROR
    # Escreve em um arquivo temporário e só troca de nome no final (rename
    # é atômico) — evita deixar um arquivo pela metade se o processo for
    # interrompido (Ctrl+C, queda de energia) no meio da escrita.
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(marker + "\n")
        f.write(f"# {item['id']} — {item['funcao']} ({prov_name}/{working_model})\n\n")
        f.write("## Resposta do LLM\n\n")
        f.write(resposta or "(vazio)")
        f.write("\n\n## Gabarito oficial (date-fns)\n\n")
        f.write(f"- **summary**: {item['gabarito']['summary']}\n")
        f.write(f"- **description**: {item['gabarito']['description']}\n")
    os.replace(tmp_path, out_path)


def load_unit_code(unit_item):
    path = os.path.join(BASE_DIR, unit_item["arquivo_unidade"])
    with open(path, encoding="utf-8") as f:
        return f.read()


def call_openai(model, prompt):
    from openai import OpenAI
    # timeout/max_retries maiores: os modelos mais novos ("gpt-6-astra" etc.)
    # apresentaram "Connection error" intermitente no seu ambiente — isso é
    # sintoma clássico de timeout/pool de conexão, não de chave ou rede
    # bloqueada (a própria API respondeu normalmente nas duas tentativas
    # anteriores). NOTA: sem parâmetro "temperature" — os modelos mais
    # novos da OpenAI (gpt-6-astra, gpt-5.6-*) só aceitam o valor padrão
    # (1) e rejeitam temperature=0 com erro 400.
    client = OpenAI(timeout=60.0, max_retries=3)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content


def call_anthropic(model, prompt):
    import anthropic
    # mesmo raciocínio do call_openai: aumentar timeout e max_retries do
    # próprio cliente, em vez de confiar em uma única tentativa rápida.
    #
    # CORRIGIDO (14/09/2026, achado durante a verificação de rigor pedida
    # por Carlos): max_tokens=1024 estava CORTANDO respostas no meio da
    # frase para as unidades mais longas (tier médio/difícil) — a resposta
    # ficava incompleta (faltando o item 2 e/ou 3), mas como não continha a
    # string "ERRO AO CHAMAR API" o marcador de status ainda gravava
    # <!-- STATUS: OK --> nela. Ou seja: um corte de token virava um erro
    # SILENCIOSO, disfarçado de sucesso. Confirmado em pelo menos 3 das 30
    # unidades (CT19, CT26, CT28) e um caso limítrofe (CT24). Nenhum outro
    # provedor tinha esse limite (openai e google não fixam max_tokens).
    # Subido para 4096 — generoso o bastante para nunca mais cortar uma
    # resposta de 3 itens curtos como estes, com custo desprezível.
    client = anthropic.Anthropic(timeout=60.0, max_retries=3)
    resp = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(block.text for block in resp.content if hasattr(block, "text"))


TRANSIENT_MARKERS = ("503", "UNAVAILABLE", "429", "RESOURCE_EXHAUSTED", "Connection error", "rate_limit")


def call_with_retry(caller, model, prompt, attempts=3, base_delay=8):
    """Tenta a chamada até `attempts` vezes com espera crescente, só para
    erros que parecem transitórios (sobrecarga momentânea, limite de taxa,
    timeout de conexão). Erros permanentes (ex.: crédito insuficiente,
    modelo inexistente) não valem a pena repetir e sobem na primeira
    tentativa."""
    last_err = None
    for i in range(attempts):
        try:
            return caller(model, prompt)
        except Exception as e:
            last_err = e
            msg = str(e)
            if not any(marker in msg for marker in TRANSIENT_MARKERS):
                print(f"    [erro NÃO transitório — detalhe completo:]\n    " +
                      describe_error(e).replace("\n", "\n    "))
                raise  # erro permanente (ex.: saldo insuficiente) — não adianta repetir
            if i < attempts - 1:
                wait = base_delay * (i + 1)
                print(f"    [erro transitório, tentando de novo em {wait}s — detalhe completo:]\n    " +
                      describe_error(e).replace("\n", "\n    "))
                time.sleep(wait)
            else:
                print(f"    [esgotou as tentativas — detalhe completo do último erro:]\n    " +
                      describe_error(e).replace("\n", "\n    "))
    raise last_err


CALLERS = {
    "openai": call_openai,
    "anthropic": call_anthropic,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--llm", choices=list(PROVIDERS.keys()), help="rodar só este provedor")
    ap.add_argument("--unidade", help="rodar só esta unidade (ex.: CT05)")
    ap.add_argument("--dry-run", action="store_true", help="só imprime os prompts, não chama API nenhuma")
    args = ap.parse_args()

    manifest = load_manifest()
    if args.unidade:
        manifest = [m for m in manifest if m["id"] == args.unidade]
        if not manifest:
            print(f"Unidade {args.unidade} não encontrada no manifest.")
            sys.exit(1)

    providers_to_run = [args.llm] if args.llm else list(PROVIDERS.keys())

    for prov_name in providers_to_run:
        prov = PROVIDERS[prov_name]
        api_key = os.environ.get(prov["env"])
        if not api_key and not args.dry_run:
            print(f"[pular] {prov_name}: variável de ambiente {prov['env']} não configurada.")
            continue

        out_dir = os.path.join(RESULTS_DIR, prov_name)
        os.makedirs(out_dir, exist_ok=True)

        # Resolve, uma vez por provedor, qual candidato de modelo realmente
        # funciona (os nomes de modelo mudam com frequência — ver comentário
        # em PROVIDERS acima). Testa com um prompt mínimo e fica com o
        # primeiro que responder sem erro.
        working_model = None
        if not args.dry_run:
            for candidate in prov["models"]:
                try:
                    call_with_retry(CALLERS[prov_name], candidate, "Responda apenas: ok", attempts=2, base_delay=5)
                    working_model = candidate
                    print(f"[modelo confirmado] {prov_name} -> {candidate}")
                    break
                except Exception as e:
                    print(f"  [modelo '{candidate}' falhou para {prov_name} — detalhe completo:]\n  " +
                          describe_error(e).replace("\n", "\n  "))
            if working_model is None:
                print(f"[pular] {prov_name}: nenhum dos modelos candidatos funcionou "
                      f"({prov['models']}). Verifique o nome do modelo manualmente na "
                      f"documentação oficial do provedor e edite PROVIDERS no topo deste script.")
                continue

        for item in manifest:
            code = load_unit_code(item)
            prompt = PROMPT_TEMPLATE.format(codigo=code)
            out_path = os.path.join(out_dir, f"{item['id']}_{item['funcao']}.md")

            if args.dry_run:
                print(f"--- {prov_name} / {item['id']} ({item['funcao']}) ---")
                print(prompt[:200] + "...\n")
                continue

            if os.path.exists(out_path):
                status = read_status(out_path)
                if status == "OK":
                    # PROTEGIDO: uma resposta válida NUNCA é tocada de novo,
                    # nem lida para reenvio, nem sobrescrita — isso vale
                    # mesmo que o script seja rodado 10 vezes.
                    print(f"[protegido, pulando] {out_path}")
                    continue
                else:
                    # Resposta anterior era erro (ou arquivo de formato
                    # antigo, sem marcador — tratado como erro por segurança).
                    # Antes de tentar de novo, guarda uma cópia da tentativa
                    # anterior em vez de simplesmente perder o conteúdo.
                    backup_previous_attempt(out_path, prov_name)
                    print(f"[retentando, resposta anterior tinha erro — backup salvo] {out_path}")

            print(f"[chamando] {prov_name} ({working_model}) / {item['id']} ({item['funcao']})...")
            try:
                resposta = call_with_retry(CALLERS[prov_name], working_model, prompt)
                status = "OK"
            except Exception as e:
                detalhe = describe_error(e)
                resposta = f"ERRO AO CHAMAR API:\n{detalhe}"
                status = "ERROR"
                print(f"  -> ERRO (detalhe completo):\n  " + detalhe.replace("\n", "\n  "))

            # Segunda trava de segurança, redundante com a checagem acima:
            # nunca sobrescreve um arquivo que já está marcado como OK,
            # mesmo que algum bug futuro no código acima deixe passar.
            if os.path.exists(out_path) and read_status(out_path) == "OK":
                print(f"[BLOQUEADO] {out_path} já tem resposta válida — resposta nova descartada, nada escrito.")
                continue

            write_result_file(out_path, item, prov_name, working_model, resposta, status)

            time.sleep(1)  # respiro entre chamadas

    print("\nConcluído. Resultados em:", RESULTS_DIR)


if __name__ == "__main__":
    main()
