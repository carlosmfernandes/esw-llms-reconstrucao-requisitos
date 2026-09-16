#!/usr/bin/env python3
"""
select_and_extract.py
======================

Reconstrução do script de seleção e extração das unidades de código
utilizadas no estudo (30 funções da biblioteca `date-fns`, estratificadas
em 3 níveis de complexidade: fácil / médio / difícil).

CONTEXTO E LIMITAÇÃO IMPORTANTE
--------------------------------
O script original usado para gerar `manifest_resumo.csv` e a pasta
`unidades/` NÃO foi preservado durante a execução do experimento. Este
arquivo é uma RECONSTRUÇÃO, escrita a posteriori, com dois objetivos
explícitos e um limite claro entre eles:

1. Validado empiricamente (100% de correspondência): a fórmula de
   complexidade (LOC + contagem de "branches") usada para calcular a
   coluna `score_complexidade` do manifesto foi deduzida por engenharia
   reversa e testada contra as 30 unidades reais do manifesto. O
   resultado é uma correspondência EXATA (loc e branches) nas 30 linhas
   de `manifest_resumo.csv` -- ver `--validar` abaixo.

2. NÃO reconstruído (limitação assumida): o procedimento exato que
   escolheu, dentre o universo de funções candidatas do date-fns, quais
   30 específicas comporiam a amostra (por exemplo, se houve amostragem
   aleatória com semente, curadoria manual, ou outro critério de corte
   dentro de cada terço de pontuação) não pôde ser recuperado. Este
   script portanto NÃO tenta sortear novamente as 30 unidades -- ele
   recebe a lista já definida (`manifest_resumo.csv`) como entrada e a
   usa para (a) validar a fórmula de pontuação e (b) reextrair o
   código-fonte de cada unidade a partir do repositório oficial.

Também há uma pequena divergência não resolvida e aqui documentada com
transparência: o levantamento do pool de candidatas feito por este
script encontra 245 funções top-level em `pkgs/core/src` com uma
exportação (`export function`/`export const`) de mesmo nome do
diretório, ao passo que a documentação interna do projeto (LEIA-ME.md)
registra "242 funções candidatas". A diferença (3 funções, ~1,2% do
pool) não pôde ser atribuída com certeza a um critério específico --
possivelmente exclusões manuais adicionais feitas na execução original
(p.ex. funções wrapper triviais como getters de campo único) que não
ficaram documentadas. Isso não afeta a validação do item 1 acima, pois
esta usa diretamente as 30 unidades já conhecidas.

USO
---
    # Validar a fórmula de pontuação contra o manifesto conhecido
    # (requer um clone do date-fns em --repo, ver abaixo)
    python3 select_and_extract.py --validar --repo /caminho/para/date-fns

    # Reextrair o código-fonte das 30 unidades para unidades_reextraidas/
    python3 select_and_extract.py --extrair --repo /caminho/para/date-fns

    # Listar o pool de funções candidatas (para inspeção/depuração)
    python3 select_and_extract.py --listar-pool --repo /caminho/para/date-fns

Repositório de origem usado neste estudo:
    https://github.com/date-fns/date-fns
    commit 18cbd436f1428d0f45f89f710df65f62546c42f0 (30/08/2026)

O código de `date-fns` é distribuído sob a licença MIT
(Copyright (C) 2020 Sasha Koss and Lesha Koss -- ver LICENSE-date-fns
neste repositório). Os trechos extraídos para `unidades/` são citações
de um terceiro para fins de pesquisa, não trabalho original dos autores
deste estudo.
"""

import argparse
import csv
import os
import re
import sys

# Diretórios de nível superior em pkgs/core/src que NÃO são funções
# públicas individuais (agrupam constantes, variantes "fp", dados de
# locale, ou não possuem index.ts). Excluídos do pool de candidatas.
NON_FUNCTION_DIRS = {"_lib", "tp", "fp", "locale", "constants"}


def find_src_root(repo_path):
    candidate = os.path.join(repo_path, "pkgs", "core", "src")
    if os.path.isdir(candidate):
        return candidate
    # fallback para checkouts mais antigos que usam layout de pacote único
    candidate2 = os.path.join(repo_path, "src")
    if os.path.isdir(candidate2):
        return candidate2
    raise FileNotFoundError(
        f"Não encontrei pkgs/core/src (nem src/) dentro de {repo_path}. "
        "Confirme que --repo aponta para um clone de "
        "https://github.com/date-fns/date-fns."
    )


def list_candidate_pool(src_root):
    """Enumera as funções candidatas: diretórios de nível superior com um
    index.ts que exporta `function <nome>` ou `const <nome>` igual ao nome
    do diretório."""
    candidates = []
    for d in sorted(os.listdir(src_root)):
        full = os.path.join(src_root, d)
        if not os.path.isdir(full) or d in NON_FUNCTION_DIRS:
            continue
        idx = os.path.join(full, "index.ts")
        if not os.path.isfile(idx):
            continue
        text = open(idx, encoding="utf-8").read()
        if re.search(r"^export (function|const) " + re.escape(d) + r"\b", text, re.MULTILINE):
            candidates.append(d)
    return candidates


def extract_function_source(fn_name, src_root):
    """Extrai o texto completo do arquivo index.ts (import + JSDoc + corpo)
    de uma função, para uso em unidades/<fn>.ts."""
    path = os.path.join(src_root, fn_name, "index.ts")
    if not os.path.isfile(path):
        return None
    return open(path, encoding="utf-8").read()


def extract_function_body(fn_name, src_root):
    """Extrai apenas a assinatura + corpo da função (sem imports nem
    JSDoc acima dela), usada para o cálculo de LOC/branches."""
    path = os.path.join(src_root, fn_name, "index.ts")
    if not os.path.isfile(path):
        return None
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^export (function|const) " + re.escape(fn_name) + r"\b", text, re.MULTILINE)
    if not m:
        return None
    start = m.start()
    # localizar o fechamento da lista de parâmetros (respeitando parênteses
    # aninhados, p.ex. tipos genéricos com funções)
    p_open = text.index("(", start)
    depth = 0
    k = p_open
    while k < len(text):
        if text[k] == "(":
            depth += 1
        elif text[k] == ")":
            depth -= 1
            if depth == 0:
                break
        k += 1
    p_close = k
    # a chave de abertura do corpo é a primeira '{' após o fechamento dos
    # parâmetros (evita capturar '{' de anotações de tipo como
    # `DateArg<Date> & {}` dentro da própria lista de parâmetros)
    i = text.index("{", p_close)
    depth = 0
    j = i
    while j < len(text):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    end = j + 1
    return text[start:end]


def count_loc(body):
    """Linhas não vazias da assinatura + corpo da função."""
    return len([l for l in body.split("\n") if l.strip() != ""])


def count_branches(body):
    """Conta pontos de decisão: if/for/while/case (palavra-chave nua, sem
    exigir parênteses -- isso inclui, propositalmente, ocorrências dessas
    palavras dentro de comentários, pois foi assim que a fórmula original
    se comportou ao ser validada contra o manifesto conhecido), &&, ||,
    coalescência nula (??) e o operador ternário (?). Encadeamento opcional
    (?.) é ignorado por não representar um ponto de decisão."""
    tmp = body.replace("?.", "")
    count = 0
    count += len(re.findall(r"\bif\b", tmp))
    count += len(re.findall(r"\bfor\b", tmp))
    count += len(re.findall(r"\bwhile\b", tmp))
    count += len(re.findall(r"\bcase\b", tmp))
    count += len(re.findall(r"&&", tmp))
    count += len(re.findall(r"\|\|", tmp))
    count += len(re.findall(r"\?\?", tmp))
    tmp = tmp.replace("??", "")
    count += len(re.findall(r"(?<![a-zA-Z0-9_])\?(?!:)", tmp))
    return count


def compute_score(fn_name, src_root):
    body = extract_function_body(fn_name, src_root)
    if body is None:
        return None
    loc = count_loc(body)
    branches = count_branches(body)
    score = loc + 2 * branches
    return loc, branches, score


def cmd_listar_pool(args):
    src_root = find_src_root(args.repo)
    pool = list_candidate_pool(src_root)
    print(f"Pool de funções candidatas encontrado: {len(pool)}")
    print(
        "(nota: o LEIA-ME.md do projeto registra 242 candidatas; esta "
        "reconstrução encontra 245 -- divergência de 3 funções não "
        "resolvida, ver docstring deste arquivo)"
    )
    for fn in pool:
        print(f"  {fn}")


def cmd_validar(args):
    src_root = find_src_root(args.repo)
    rows = list(csv.DictReader(open(args.manifest, encoding="utf-8")))
    print(f"{'id':6}{'funcao':32}{'loc_manifesto':14}{'loc_calc':10}"
          f"{'branches_manifesto':20}{'branches_calc':14}{'score_manifesto':16}"
          f"{'score_calc':10}status")
    mismatches = 0
    for r in rows:
        fn = r["funcao"]
        result = compute_score(fn, src_root)
        if result is None:
            print(f"{r['id']:6}{fn:32} FUNÇÃO NÃO ENCONTRADA em {src_root}")
            mismatches += 1
            continue
        loc_c, branches_c, score_c = result
        loc_m, branches_m = int(r["loc"]), int(r["branches"])
        score_m = int(r["score"]) if "score" in r else loc_m + 2 * branches_m
        ok = (loc_c == loc_m and branches_c == branches_m and score_c == score_m)
        if not ok:
            mismatches += 1
        print(f"{r['id']:6}{fn:32}{loc_m:<14}{loc_c:<10}{branches_m:<20}"
              f"{branches_c:<14}{score_m:<16}{score_c:<10}{'OK' if ok else 'DIVERGENTE'}")
    print(f"\nTotal de divergências: {mismatches}/{len(rows)}")
    if mismatches == 0:
        print("Fórmula de pontuação (LOC + 2 x branches) validada com "
              "100% de correspondência contra o manifesto conhecido.")
    sys.exit(1 if mismatches else 0)


def cmd_extrair(args):
    src_root = find_src_root(args.repo)
    rows = list(csv.DictReader(open(args.manifest, encoding="utf-8")))
    os.makedirs(args.saida, exist_ok=True)
    ok, falhas = 0, 0
    for r in rows:
        fn = r["funcao"]
        source = extract_function_source(fn, src_root)
        if source is None:
            print(f"[FALHA] {r['id']} ({fn}): arquivo-fonte não encontrado")
            falhas += 1
            continue
        out_path = os.path.join(args.saida, f"{fn}.ts")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(source)
        ok += 1
    print(f"Extraídas {ok}/{len(rows)} unidades para {args.saida}/ ({falhas} falhas)")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--repo", required=True, help="Caminho para um clone local de https://github.com/date-fns/date-fns")
    p.add_argument("--manifest", default=os.path.join(os.path.dirname(__file__), "..", "manifest_resumo.csv"),
                    help="Caminho para manifest_resumo.csv (padrão: ../manifest_resumo.csv relativo a este script)")
    p.add_argument("--saida", default="unidades_reextraidas", help="Pasta de saída para --extrair")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--listar-pool", action="store_true", help="Lista o pool de funções candidatas")
    g.add_argument("--validar", action="store_true", help="Valida a fórmula de pontuação contra o manifesto")
    g.add_argument("--extrair", action="store_true", help="Reextrai o código-fonte das 30 unidades do manifesto")
    args = p.parse_args()

    if args.listar_pool:
        cmd_listar_pool(args)
    elif args.validar:
        cmd_validar(args)
    elif args.extrair:
        cmd_extrair(args)


if __name__ == "__main__":
    main()
