#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classificação final das 120 respostas (4 condições x 30 unidades) contra o
gabarito oficial do date-fns, segundo a rubrica de prompt_padrao.md:
  correto = 1.0 | parcialmente correto = 0.5 | incorreto = 0.0

Metodologia da classificação (documentada para rastreabilidade):
  - Cada uma das 4 condições (openai, anthropic, google-gemini-3.6-flash,
    google-gemini-3.8-flash) foi classificada por um agente independente,
    que leu o gabarito oficial (manifest.json) e a resposta de cada uma
    das 30 unidades, com instrução explícita de rigor (não ser generoso).
  - ACHADO DE DADOS (14/09/2026, confiança alta): as respostas CT19, CT24,
    CT26 e CT28 da condição anthropic estavam TRUNCADAS por um bug de
    max_tokens=1024 em executar_experimento.py (corrigido para 4096).
    As 4 unidades foram re-coletadas por Carlos após o fix, e a classifi-
    cação abaixo já reflete as respostas completas e verificadas (não as
    versões truncadas, que ficaram preservadas em
    resultados/anthropic/_tentativas_anteriores/ como backup).
  - Achado metodológico (confiança alta, já documentado em
    prompt_padrao.md e no LEIA-ME): os nomes das funções não foram
    ofuscados nas unidades médias/difíceis, o que facilita a reconstrução
    e ajuda a explicar o efeito-teto (quase todas as respostas "corretas")
    observado abaixo — ver nota na seção de limitações do LEIA-ME.
"""

import csv
import os

TIER = {f"CT{i:02d}": t for i, t in zip(
    range(1, 31),
    ["facil"]*10 + ["medio"]*10 + ["dificil"]*10
)}

FUNCAO = {
    "CT01": "isLeapYear", "CT02": "getISODay", "CT03": "isWeekend",
    "CT04": "daysToWeeks", "CT05": "isValid", "CT06": "getDayOfYear",
    "CT07": "getQuarter", "CT08": "differenceInSeconds", "CT09": "isSameDay",
    "CT10": "endOfISOWeek", "CT11": "isSameWeek", "CT12": "toDate",
    "CT13": "compareAsc", "CT14": "setYear", "CT15": "addDays",
    "CT16": "clamp", "CT17": "areIntervalsOverlapping", "CT18": "sub",
    "CT19": "max", "CT20": "startOfWeek",
    "CT21": "getOverlappingDaysInIntervals", "CT22": "add",
    "CT23": "intervalToDuration", "CT24": "eachDayOfInterval",
    "CT25": "differenceInBusinessDays", "CT26": "differenceInMonths",
    "CT27": "formatDuration", "CT28": "eachWeekOfInterval",
    "CT29": "addBusinessDays", "CT30": "formatRelative",
}

# score: 1.0 = correto, 0.5 = parcialmente correto, 0.0 = incorreto
# (classificação feita por agentes independentes lendo cada resposta
# contra o gabarito oficial de manifest.json; ver LEIA-ME secao 12 para
# as justificativas individuais por unidade)

OPENAI = {f"CT{i:02d}": 1.0 for i in range(1, 31)}
OPENAI["CT10"] = 0.5
OPENAI["CT11"] = 0.5

ANTHROPIC = {f"CT{i:02d}": 1.0 for i in range(1, 31)}
# CT19, CT24, CT26, CT28 re-coletadas apos o fix de max_tokens (14/09) e
# reclassificadas a partir da resposta completa: todas "correto".

GOOGLE_36 = {f"CT{i:02d}": 1.0 for i in range(1, 31)}

GOOGLE_38 = {f"CT{i:02d}": 1.0 for i in range(1, 31)}
GOOGLE_38["CT11"] = 0.5

CONDICOES = {
    "openai": OPENAI,
    "anthropic": ANTHROPIC,
    "google_gemini_3_6_flash": GOOGLE_36,
    "google_gemini_3_8_flash": GOOGLE_38,
}


def build_rows():
    rows = []
    for i in range(1, 31):
        cid = f"CT{i:02d}"
        row = {
            "id": cid,
            "funcao": FUNCAO[cid],
            "tier": TIER[cid],
        }
        for cond, scores in CONDICOES.items():
            row[cond] = scores[cid]
        rows.append(row)
    return rows


def main():
    rows = build_rows()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "classificacao.csv")
    fieldnames = ["id", "funcao", "tier"] + list(CONDICOES.keys())
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"Escrito: {out_path} ({len(rows)} linhas)")

    # resumo rápido
    for cond in CONDICOES:
        total = sum(r[cond] for r in rows)
        n_correto = sum(1 for r in rows if r[cond] == 1.0)
        n_parcial = sum(1 for r in rows if r[cond] == 0.5)
        n_incorreto = sum(1 for r in rows if r[cond] == 0.0)
        print(f"{cond}: score total = {total}/30 | correto={n_correto} parcial={n_parcial} incorreto={n_incorreto}")


if __name__ == "__main__":
    main()
