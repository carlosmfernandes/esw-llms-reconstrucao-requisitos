#!/usr/bin/env python3
"""
Script para SER EXECUTADO NO SEU COMPUTADOR — roda SOMENTE o Google,
SOMENTE no modelo gemini-3.8-flash, e escreve SOMENTE na pasta
resultados/google-gemini-3.8-flash/.

Irmão deste script: executar_google_36.py (mesma lógica, modelo
gemini-3.6-flash, pasta resultados/google-gemini-3.6-flash/). Ver o
cabeçalho daquele arquivo para a explicação de por que os dois modelos do
Google viraram duas condições experimentais separadas, cada uma com
N=30 própria, em vez de uma única condição "Google" misturada.

Nenhum código aqui referencia openai/, anthropic/ ou deepseek/.

Pré-requisito: billing ativado no projeto Google associado à sua
GOOGLE_API_KEY. Teste primeiro com --unidade CT24 antes de rodar o lote.

Uso:
    python3 executar_google_38.py
    python3 executar_google_38.py --unidade CT24
    python3 executar_google_38.py --dry-run
"""
import argparse
import json
import os
import sys
import time


def describe_error(e):
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

MODEL = "gemini-3.8-flash"
OUT_DIR = os.path.join(BASE_DIR, "resultados", "google-gemini-3.8-flash")

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

STATUS_MARKER_OK = "<!-- STATUS: OK -->"
STATUS_MARKER_ERROR = "<!-- STATUS: ERROR -->"

TRANSIENT_MARKERS = ("503", "UNAVAILABLE", "429", "RESOURCE_EXHAUSTED", "Connection error", "rate_limit")


def load_manifest():
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_unit_code(unit_item):
    path = os.path.join(BASE_DIR, unit_item["arquivo_unidade"])
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_status(path):
    with open(path, encoding="utf-8") as f:
        head = f.read(200)
    if STATUS_MARKER_OK in head:
        return "OK"
    if STATUS_MARKER_ERROR in head:
        return "ERROR"
    with open(path, encoding="utf-8") as f:
        content = f.read()
    return "ERROR" if "ERRO AO CHAMAR API" in content else "OK"


def backup_previous_attempt(out_path):
    backup_dir = os.path.join(OUT_DIR, "_tentativas_anteriores")
    os.makedirs(backup_dir, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    base = os.path.basename(out_path)
    backup_path = os.path.join(backup_dir, f"{base}.{stamp}.bak")
    os.replace(out_path, backup_path)


def write_result_file(out_path, item, resposta, status):
    marker = STATUS_MARKER_OK if status == "OK" else STATUS_MARKER_ERROR
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(marker + "\n")
        f.write(f"# {item['id']} — {item['funcao']} (google/{MODEL})\n\n")
        f.write("## Resposta do LLM\n\n")
        f.write(resposta or "(vazio)")
        f.write("\n\n## Gabarito oficial (date-fns)\n\n")
        f.write(f"- **summary**: {item['gabarito']['summary']}\n")
        f.write(f"- **description**: {item['gabarito']['description']}\n")
    os.replace(tmp_path, out_path)


def call_google(prompt):
    from google import genai
    client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
    resp = client.models.generate_content(model=MODEL, contents=prompt)
    return resp.text


def call_with_retry(prompt, attempts=3, base_delay=8):
    last_err = None
    for i in range(attempts):
        try:
            return call_google(prompt)
        except Exception as e:
            last_err = e
            msg = str(e)
            if not any(marker in msg for marker in TRANSIENT_MARKERS):
                print("    [erro NÃO transitório — detalhe completo:]\n    " +
                      describe_error(e).replace("\n", "\n    "))
                raise
            if i < attempts - 1:
                wait = base_delay * (i + 1)
                print(f"    [erro transitório, tentando de novo em {wait}s — detalhe completo:]\n    " +
                      describe_error(e).replace("\n", "\n    "))
                time.sleep(wait)
            else:
                print("    [esgotou as tentativas — detalhe completo do último erro:]\n    " +
                      describe_error(e).replace("\n", "\n    "))
    raise last_err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--unidade", help="rodar só esta unidade (ex.: CT24)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not os.environ.get("GOOGLE_API_KEY") and not args.dry_run:
        print("[erro] variável de ambiente GOOGLE_API_KEY não configurada.")
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)

    manifest = load_manifest()
    if args.unidade:
        manifest = [m for m in manifest if m["id"] == args.unidade]
        if not manifest:
            print(f"Unidade {args.unidade} não encontrada no manifest.")
            sys.exit(1)

    if not args.dry_run:
        try:
            call_with_retry("Responda apenas: ok", attempts=2, base_delay=5)
            print(f"[modelo confirmado] google -> {MODEL}")
        except Exception as e:
            print(f"[ERRO] {MODEL} não respondeu — detalhe completo:\n" +
                  describe_error(e).replace("\n", "\n  "))
            print("Verifique se o billing está mesmo ativo no projeto dessa chave "
                  "(o erro 429 com quotaId '...FreeTier...' significa que o projeto "
                  "ainda está no nível gratuito, mesmo que exista saldo em outro lugar).")
            sys.exit(1)

    for item in manifest:
        code = load_unit_code(item)
        prompt = PROMPT_TEMPLATE.format(codigo=code)
        out_path = os.path.join(OUT_DIR, f"{item['id']}_{item['funcao']}.md")

        if args.dry_run:
            print(f"--- google/{MODEL} / {item['id']} ({item['funcao']}) ---")
            print(prompt[:200] + "...\n")
            continue

        if os.path.exists(out_path):
            status = read_status(out_path)
            if status == "OK":
                print(f"[protegido, pulando] {out_path}")
                continue
            else:
                backup_previous_attempt(out_path)
                print(f"[retentando, resposta anterior tinha erro — backup salvo] {out_path}")

        print(f"[chamando] google ({MODEL}) / {item['id']} ({item['funcao']})...")
        try:
            resposta = call_with_retry(prompt)
            status = "OK"
        except Exception as e:
            detalhe = describe_error(e)
            resposta = f"ERRO AO CHAMAR API:\n{detalhe}"
            status = "ERROR"
            print("  -> ERRO (detalhe completo):\n  " + detalhe.replace("\n", "\n  "))

        if os.path.exists(out_path) and read_status(out_path) == "OK":
            print(f"[BLOQUEADO] {out_path} já tem resposta válida — resposta nova descartada, nada escrito.")
            continue

        write_result_file(out_path, item, resposta, status)
        time.sleep(1)

    print(f"\nConcluído. Resultados em: {OUT_DIR}")


if __name__ == "__main__":
    main()
