<!-- STATUS: OK -->
# CT11 — isSameWeek (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise do código: `isSameWeek`

## 1. Requisito funcional

A função verifica se duas datas pertencem à **mesma semana** (a semana sendo definida a partir de um dia inicial configurável, ex.: domingo ou segunda-feira, e/ou localização). O critério de comparação é: ambas as datas, quando normalizadas para o início de sua respectiva semana, devem coincidir no mesmo instante.

Trata-se de uma função utilitária de comparação de datas por período (semana), útil para agrupamento, validações ou lógica de calendário (ex.: "esse evento ocorre na mesma semana que aquele?").

## 2. Parâmetros de entrada

- **`laterDate: DateArg<Date> & {}`** — a primeira data a ser comparada (representa, semanticamente, a data "mais recente", embora a função não valide isso explicitamente).
- **`earlierDate: DateArg<Date> & {}`** — a segunda data a ser comparada (semanticamente, a data "mais antiga").
- **`options?: IsSameWeekOptions`** — objeto opcional de configuração, que combina:
  - **`WeekOptions`** — provavelmente define o dia em que a semana começa (ex.: `weekStartsOn`).
  - **`LocalizedOptions<"options">`** — permite definir localização (`locale`) que pode influenciar a convenção de início de semana.
  - **`ContextOptions<Date>`** — permite definir o construtor de data (`in`), possivelmente para suportar contextos de fuso horário ou tipos de data alternativos.

## 3. Retorno

- **`boolean`** — `true` se as duas datas fornecidas estão dentro da mesma semana (segundo os critérios de início de semana definidos em `options`); `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Are the given dates in the same week (and month and year)?
- **description**: Are the given dates in the same week (and month and year)?
