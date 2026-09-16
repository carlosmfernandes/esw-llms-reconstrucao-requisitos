<!-- STATUS: OK -->
# CT30 — formatRelative (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `formatRelative`

## 1. Requisito funcional

A função implementa a formatação de uma data de forma **relativa** a uma data de referência (data base), produzindo uma string legível que descreve a data em termos como "ontem", "hoje", "amanhã", "na semana passada", "na próxima semana" ou, caso a diferença seja maior que uma semana em qualquer direção, utiliza um formato padrão (não relativo).

A lógica central é:
- Calcular a diferença em dias de calendário entre `date` e `baseDate`.
- Classificar essa diferença em uma das categorias (token): `yesterday`, `today`, `tomorrow`, `lastWeek`, `nextWeek` ou `other`.
- Obter, a partir do locale, o padrão de formatação textual correspondente a esse token.
- Aplicar esse padrão para formatar a data final, retornando a string resultante.

Também há tratamento de erro: se a diferença calculada for `NaN` (ou seja, uma das datas é inválida), a função lança um `RangeError`.

## 2. Parâmetros de entrada

- **`date: DateArg<Date> & {}`** — a data que se deseja formatar de forma relativa.
- **`baseDate: DateArg<Date> & {}`** — a data de referência (base) em relação à qual `date` será comparada/formatada.
- **`options?: FormatRelativeOptions`** — objeto opcional de configuração, que pode conter:
  - `locale` — o locale a ser usado para localização (idioma) da formatação (afeta `formatRelative` e `formatLong`).
  - `weekStartsOn` — dia da semana considerado como início (usado no cálculo/formatação relacionados a semanas).
  - `in` — (via `ContextOptions<Date>`) contexto/construtor usado para normalizar as datas de entrada.

## 3. Retorno

A função retorna uma **`string`**, contendo a representação textual relativa da `date` em relação à `baseDate`, já formatada de acordo com o locale e as regras de início de semana aplicáveis (por exemplo: `"yesterday at 2:30 PM"`, `"last Monday at 10:00 AM"`, etc., dependendo do locale usado).

Se as datas fornecidas forem inválidas (resultando em `NaN` no cálculo de diferença), a função lança uma exceção `RangeError("Invalid time value")` em vez de retornar uma string.

## Gabarito oficial (date-fns)

- **summary**: Represent the date in words relative to the given base date.
- **description**: Represent the date in words relative to the given base date.
