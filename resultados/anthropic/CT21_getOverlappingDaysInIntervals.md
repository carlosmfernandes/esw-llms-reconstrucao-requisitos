<!-- STATUS: OK -->
# CT21 — getOverlappingDaysInIntervals (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `getOverlappingDaysInIntervals`

## 1. Requisito funcional

A função calcula o **número de dias completos de sobreposição (overlap) entre dois intervalos de datas**. Ou seja, dado dois intervalos (cada um com uma data de início e uma data de fim), a função determina quantos dias eles têm em comum.

Requisitos específicos identificados no código:
- Os intervalos podem ter suas datas de início/fim em qualquer ordem (a função normaliza internamente, ordenando start/end).
- Se os intervalos não se sobrepõem, o resultado deve ser `0` (evitando retornar `NaN`).
- O cálculo deve ser resiliente a efeitos de horário de verão (DST), removendo o offset de fuso horário antes de calcular a diferença.
- Dias parciais de sobreposição devem ser contados como um dia inteiro (arredondamento para cima).

## 2. Parâmetros de entrada

- **`intervalLeft: Interval`** — o primeiro intervalo de tempo, contendo propriedades `start` e `end` (representando as datas de início e fim desse intervalo).
- **`intervalRight: Interval`** — o segundo intervalo de tempo, com a mesma estrutura (`start` e `end`), a ser comparado com o primeiro.

(O tipo `Interval` é importado externamente, mas pelo uso no código, seus campos `start`/`end` aceitam valores conversíveis em data via `toDate`.)

## 3. Retorno

- **`number`** — a quantidade de dias (inteiros) em que os dois intervalos se sobrepõem.
  - Retorna `0` caso não haja sobreposição alguma entre os intervalos.
  - Caso haja sobreposição, retorna o número de dias arredondado para cima (`Math.ceil`), contabilizando inclusive sobreposições parciais de um dia.

## Gabarito oficial (date-fns)

- **summary**: Get the number of days that overlap in two time intervals
- **description**: Get the number of days that overlap in two time intervals. It uses the time between dates to calculate the number of days, rounding it up to include partial days.
