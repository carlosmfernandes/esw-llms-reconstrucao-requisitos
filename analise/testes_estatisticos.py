#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes estatísticos sobre a classificação das 120 respostas (4 condições
independentes x 30 unidades de código), conforme protocolo definido em
prompt_padrao.md:

  1. Cochran's Q  -- diferença global entre as 4 condições (dado binário:
     correto=1 vs. não-totalmente-correto=0).
  2. McNemar pareado (6 pares) com correção de Holm -- comparações post-hoc.
  3. Friedman + Wilcoxon post-hoc, por tier de dificuldade (facil/medio/
     dificil, 10 unidades cada) -- usa o score 0/0.5/1 (nao binarizado).
  4. Kendall's W -- tamanho de efeito da concordancia entre condicoes.

Lê classificacao.csv (gerado por classificacao.py) e escreve
resultados_estatisticos.md com os resultados e as ressalvas metodológicas
(efeito-teto: pouquíssima variância nos dados, ver LEIA-ME).
"""

import csv
import os
import itertools

import numpy as np
from scipy import stats
from statsmodels.stats.contingency_tables import mcnemar
from statsmodels.stats.multitest import multipletests

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "classificacao.csv")
OUT_PATH = os.path.join(HERE, "resultados_estatisticos.md")

CONDICOES = ["openai", "anthropic", "google_gemini_3_6_flash", "google_gemini_3_8_flash"]
NOMES_LEGIVEIS = {
    "openai": "OpenAI (gpt-6-astra)",
    "anthropic": "Anthropic (claude-sonnet-5)",
    "google_gemini_3_6_flash": "Google (gemini-3.6-flash)",
    "google_gemini_3_8_flash": "Google (gemini-3.8-flash)",
}


def load_rows():
    with open(CSV_PATH, encoding="utf-8") as f:
        r = csv.DictReader(f)
        rows = list(r)
    for row in rows:
        for c in CONDICOES:
            row[c] = float(row[c])
    return rows


def cochrans_q(bin_matrix):
    """bin_matrix: array (n_subjects, k_conditions) de 0/1.
    Retorna (Q, df, p)."""
    n, k = bin_matrix.shape
    col_sums = bin_matrix.sum(axis=0)
    row_sums = bin_matrix.sum(axis=1)
    L = col_sums.sum()
    numerator = k * (k - 1) * np.sum((col_sums - L / k) ** 2)
    denominator = k * L - np.sum(row_sums ** 2)
    if denominator == 0:
        return float("nan"), k - 1, float("nan")
    Q = numerator / denominator
    df = k - 1
    p = 1 - stats.chi2.cdf(Q, df)
    return Q, df, p


def kendalls_w(score_matrix):
    """Kendall's W a partir de uma matriz (n_subjects, k_conditions) de
    scores (podem ser 0/0.5/1). Usa a formulacao baseada em postos por
    sujeito (equivalente ao W derivado da estatistica de Friedman)."""
    n, k = score_matrix.shape
    # rankings por linha (sujeito), com tratamento de empates (media dos postos)
    ranks = np.apply_along_axis(stats.rankdata, 1, score_matrix)
    R_j = ranks.sum(axis=0)
    R_mean = ranks.sum() / k
    S = np.sum((R_j - n * (k + 1) / 2) ** 2)
    W = 12 * S / (n ** 2 * (k ** 3 - k))
    return W


def main():
    rows = load_rows()
    n = len(rows)
    lines = []
    lines.append("# Resultados estatísticos — Projeto Final ESW (DFS03007)\n")
    lines.append(f"N = {n} unidades de código por condição; {len(CONDICOES)} condições independentes "
                  f"(OpenAI, Anthropic, Google gemini-3.6-flash, Google gemini-3.8-flash). "
                  f"DeepSeek fora do estudo (não financiado).\n")

    # ---------- Resumo descritivo ----------
    lines.append("## 1. Resumo descritivo\n")
    lines.append("| Condição | Correto | Parcial | Incorreto | Score total (máx. 30) |")
    lines.append("|---|---|---|---|---|")
    score_matrix = np.zeros((n, len(CONDICOES)))
    for j, cond in enumerate(CONDICOES):
        vals = [row[cond] for row in rows]
        score_matrix[:, j] = vals
        n_correto = sum(1 for v in vals if v == 1.0)
        n_parcial = sum(1 for v in vals if v == 0.5)
        n_incorreto = sum(1 for v in vals if v == 0.0)
        lines.append(f"| {NOMES_LEGIVEIS[cond]} | {n_correto} | {n_parcial} | {n_incorreto} | {sum(vals):.1f} |")
    lines.append("")

    # ---------- Cochran's Q ----------
    lines.append("## 2. Cochran's Q (diferença global entre as 4 condições)\n")
    lines.append("Binarização usada: `correto` (score=1.0) = 1; `parcial` ou `incorreto` (score<1.0) = 0 "
                  "— exigida pelo teste, que só aceita dados binários.\n")
    bin_matrix = (score_matrix == 1.0).astype(int)
    Q, df, p = cochrans_q(bin_matrix)
    lines.append(f"- Q = {Q:.4f}, df = {df}, p = {p:.4f}\n")
    if p >= 0.05 or np.isnan(p):
        lines.append("- **Não significativo** ao nível de 5%. Com apenas 2 das 30 unidades (CT10, CT11) "
                      "apresentando qualquer discordância entre as 4 condições, o teste tem poder "
                      "estatístico extremamente baixo — a hipótese nula de que as condições têm a mesma "
                      "taxa de acerto não pode ser rejeitada, mas isso reflete um **efeito-teto** nos "
                      "dados, não necessariamente ausência real de diferença entre os modelos.\n")
    else:
        lines.append("- Significativo ao nível de 5%.\n")

    # ---------- McNemar pareado + Holm ----------
    lines.append("## 3. McNemar pareado (6 comparações) com correção de Holm\n")
    pares = list(itertools.combinations(CONDICOES, 2))
    pvalues = []
    detalhes = []
    for a, b in pares:
        va = bin_matrix[:, CONDICOES.index(a)]
        vb = bin_matrix[:, CONDICOES.index(b)]
        tab = np.zeros((2, 2))
        tab[1, 1] = np.sum((va == 1) & (vb == 1))
        tab[1, 0] = np.sum((va == 1) & (vb == 0))
        tab[0, 1] = np.sum((va == 0) & (vb == 1))
        tab[0, 0] = np.sum((va == 0) & (vb == 0))
        res = mcnemar(tab, exact=True)
        pvalues.append(res.pvalue)
        detalhes.append((a, b, tab[1, 0], tab[0, 1], res.pvalue))

    reject, p_holm, _, _ = multipletests(pvalues, alpha=0.05, method="holm")
    lines.append("| Par | Discordâncias (A só / B só) | p (McNemar exato) | p (Holm) | Rejeita H0 (5%) |")
    lines.append("|---|---|---|---|---|")
    for (a, b, only_a, only_b, p_raw), p_h, rej in zip(detalhes, p_holm, reject):
        lines.append(f"| {NOMES_LEGIVEIS[a]} vs {NOMES_LEGIVEIS[b]} | {int(only_a)} / {int(only_b)} | "
                      f"{p_raw:.4f} | {p_h:.4f} | {'sim' if rej else 'não'} |")
    lines.append("")
    lines.append("Nenhuma comparação par a par tem poder estatístico real aqui: o número de unidades "
                  "discordantes entre qualquer par de condições é 0, 1 ou 2 em 30 — muito pouco para "
                  "um teste de McNemar detectar diferença, mesmo antes da correção de Holm.\n")

    # ---------- Friedman global (todas as 30 unidades) ----------
    lines.append("## 4. Friedman global (todas as 30 unidades, score 0/0.5/1)\n")
    try:
        stat_g, p_g = stats.friedmanchisquare(*[score_matrix[:, j] for j in range(score_matrix.shape[1])])
        lines.append(f"- Friedman χ² = {stat_g:.4f}, p = {p_g:.4f}\n")
    except ValueError as e:
        lines.append(f"- Não computável ({e}).\n")

    # ---------- Friedman + Wilcoxon por tier ----------
    lines.append("## 5. Friedman + Wilcoxon post-hoc, por tier de dificuldade\n")
    for tier in ["facil", "medio", "dificil"]:
        sub = [row for row in rows if row["tier"] == tier]
        mat = np.array([[row[c] for c in CONDICOES] for row in sub])
        lines.append(f"### Tier: {tier} (n={len(sub)})\n")
        if np.all(mat == mat[0, 0]):
            lines.append("- Todas as respostas idênticas entre condições e unidades — Friedman não é "
                          "computável (variância zero). Efeito-teto total neste tier.\n")
            continue
        try:
            stat, p = stats.friedmanchisquare(*[mat[:, j] for j in range(mat.shape[1])])
            lines.append(f"- Friedman χ² = {stat:.4f}, p = {p:.4f}\n")
        except ValueError as e:
            lines.append(f"- Friedman não computável ({e}) — variância insuficiente neste tier.\n")
            continue

        # Wilcoxon pareado post-hoc (sem correção separada aqui; reportado como
        # exploratório, já que o Friedman global não é significativo na maior
        # parte dos tiers)
        for a, b in itertools.combinations(CONDICOES, 2):
            xa = mat[:, CONDICOES.index(a)]
            xb = mat[:, CONDICOES.index(b)]
            diffs = xa - xb
            if np.all(diffs == 0):
                lines.append(f"  - {NOMES_LEGIVEIS[a]} vs {NOMES_LEGIVEIS[b]}: idênticos neste tier, "
                              f"Wilcoxon não computável.")
                continue
            try:
                wstat, wp = stats.wilcoxon(xa, xb)
                lines.append(f"  - {NOMES_LEGIVEIS[a]} vs {NOMES_LEGIVEIS[b]}: W={wstat:.2f}, p={wp:.4f}")
            except ValueError as e:
                lines.append(f"  - {NOMES_LEGIVEIS[a]} vs {NOMES_LEGIVEIS[b]}: não computável ({e})")
        lines.append("")

    # ---------- Kendall's W ----------
    lines.append("## 6. Kendall's W (tamanho de efeito, concordância de postos entre condições)\n")
    W = kendalls_w(score_matrix)
    lines.append(f"- W = {W:.4f} (0 = nenhuma concordância de postos além do acaso, 1 = concordância perfeita)\n")
    lines.append("- **Atenção à interpretação**: W saiu baixo (perto de 0), não perto de 1. Isso NÃO "
                  "significa que os modelos discordam entre si — significa o oposto: em 28 das 30 "
                  "unidades todas as condições empatam no mesmo valor (todas 'correto'), e postos "
                  "empatados não contribuem variância nenhuma à estatística de Kendall's W. Como o "
                  "cálculo de W depende de haver variação de postos entre as unidades para detectar "
                  "concordância, e só 2 das 30 unidades (CT10, CT11) têm qualquer variação, W fica "
                  "artificialmente baixo por falta de dados informativos — não por desacordo real "
                  "entre os modelos. Reportar este resultado citando W isoladamente, sem esta ressalva, "
                  "seria enganoso.\n")

    lines.append("## 7. Limitação central destes resultados (leia antes de interpretar)\n")
    lines.append("Das 30 unidades, 28 tiveram concordância unânime (\"correto\") entre as 4 condições; "
                  "apenas CT10 (`endOfISOWeek`, OpenAI parcial) e CT11 (`isSameWeek`, OpenAI e "
                  "Gemini-3.8-flash parciais) mostraram qualquer variação. Isso é consistente com uma "
                  "limitação já registrada no desenho do experimento (`prompt_padrao.md`): os nomes das "
                  "funções não foram ofuscados nas unidades de tier médio/difícil, e o date-fns é uma "
                  "biblioteca extremamente popular e bem documentada — é plausível que os 4 modelos "
                  "tenham memorizado ou reconhecido essas funções em vez de reconstruir o requisito "
                  "puramente a partir da leitura do código. Isso reduz drasticamente a variância "
                  "disponível para os testes estatísticos e deve ser discutido como limitação explícita "
                  "na seção de Discussão do relatório.\n")

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Escrito: {OUT_PATH}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
