<!-- STATUS: OK -->
# CT04 — daysToWeeks (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise do código

## 1. Requisito funcional

A função implementa a conversão de uma quantidade de **dias** em uma quantidade equivalente de **semanas completas**. Ou seja, dado um número de dias, ela calcula quantas semanas inteiras (7 dias cada) cabem nesse total, descartando dias que não completam uma semana (truncamento, não arredondamento).

Há também um requisito adicional explícito no código: evitar que o resultado seja retornado como "zero negativo" (`-0`), normalizando esse caso específico para `0` positivo — provavelmente para garantir consistência em comparações ou serialização do valor.

## 2. Parâmetros de entrada

- **`days: number`** — representa a quantidade total de dias a ser convertida em semanas. Pode ser um valor positivo, negativo ou zero (o tratamento do "zero negativo" sugere que valores negativos são esperados e suportados).

## 3. Retorno

A função retorna um **`number`**, representando a quantidade de **semanas completas** contidas no valor de `days` informado, calculada por divisão truncada (`Math.trunc`) usando a constante `daysInWeek` (presumivelmente igual a 7, definida externamente). Caso o resultado do truncamento seja `-0`, a função retorna `0` em vez disso.

## Gabarito oficial (date-fns)

- **summary**: Convert days to weeks.
- **description**: Convert a number of days to a full number of weeks.
