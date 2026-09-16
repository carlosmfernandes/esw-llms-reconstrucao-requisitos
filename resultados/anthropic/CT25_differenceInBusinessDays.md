<!-- STATUS: OK -->
# CT25 — differenceInBusinessDays (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `differenceInBusinessDays`

## 1. Requisito funcional

A função calcula a **quantidade de dias úteis (dias de semana, excluindo sábados e domingos)** entre duas datas fornecidas. O resultado representa quantos dias que não são finais de semana existem no intervalo entre `earlierDate` e `laterDate`.

A lógica funciona da seguinte forma:
- Calcula a diferença total em dias de calendário entre as duas datas.
- Determina quantas semanas completas cabem nessa diferença (cada semana completa contribui com exatamente 5 dias úteis).
- Para os dias restantes (menos de uma semana), itera dia a dia verificando se cada um é fim de semana, somando ao resultado apenas os que não são.
- Trata corretamente diferenças negativas (quando `laterDate` é anterior a `earlierDate`), preservando o sinal do resultado.
- Evita retornar "zero negativo" (-0), normalizando para 0.
- Se qualquer uma das datas de entrada for inválida, retorna `NaN`.

## 2. Parâmetros de entrada

- **`laterDate: DateArg<Date> & {}`** — a data considerada "posterior" (ou de referência final) para o cálculo da diferença.
- **`earlierDate: DateArg<Date> & {}`** — a data considerada "anterior" (ou de referência inicial) para o cálculo da diferença.
- **`options?: DifferenceInBusinessDaysOptions`** — objeto opcional de configuração que estende `ContextOptions<Date>`. Permite, por exemplo, especificar um contexto de data customizado (`options.in`) usado na normalização das datas e passado adiante para `isWeekend`.

## 3. Retorno

- **`number`** — a quantidade de dias úteis entre `earlierDate` e `laterDate`:
  - Positivo se `laterDate` for posterior a `earlierDate`.
  - Negativo se `laterDate` for anterior a `earlierDate`.
  - `0` (nunca `-0`) se as datas coincidirem ou o cálculo resultar em zero.
  - `NaN` se `laterDate` ou `earlierDate` forem datas inválidas.

## Gabarito oficial (date-fns)

- **summary**: Get the number of business days between the given dates.
- **description**: Get the number of business day periods between the given dates. Business days being days that aren't in the weekend. Like `differenceInCalendarDays`, the function removes the times from the dates before calculating the difference.
