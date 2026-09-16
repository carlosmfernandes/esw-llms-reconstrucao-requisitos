<!-- STATUS: OK -->
# CT26 — differenceInMonths (anthropic/claude-sonnet-5)

## Resposta do LLM

## 1. Requisito funcional

A função calcula a diferença em **meses completos** entre duas datas, ajustando o resultado de `differenceInCalendarMonths` (que conta apenas transições de mês no calendário, ignorando o dia) para refletir se o mês contado é de fato um mês "cheio" (full month), com base no dia do mês.

Ou seja, difere de um simples cálculo de "quantos meses de calendário existem entre as datas": aqui a função verifica se, subtraindo o número de meses de diferença calendário da data mais recente, o resultado ainda ultrapassa (ou não) a data mais antiga — indicando que o último mês contado não estava completo, e nesse caso decrementa o resultado em 1.

Há também um tratamento especial:
- Ajuste para o mês de fevereiro (índice 1) quando o dia é maior que 27, fixando o dia em 30 para evitar problemas de overflow ao subtrair meses (ex: 31 de janeiro vira março ao invés de fevereiro).
- Um caso especial quando `laterDate` é o último dia do mês e a diferença é exatamente 1 mês, tratando esse caso como mês completo mesmo que a comparação de dias sugerisse o contrário.

O sinal do resultado indica a direção temporal (positivo se `laterDate` é posterior a `earlierDate`, negativo caso contrário).

## 2. Parâmetros de entrada

- **`laterDate: DateArg<Date> & {}`**: uma das duas datas a serem comparadas (não necessariamente a cronologicamente posterior — o nome sugere isso, mas o algoritmo lida com qualquer ordem através do `sign`).
- **`earlierDate: DateArg<Date> & {}`**: a outra data a ser comparada.
- **`options?: DifferenceInMonthsOptions`**: objeto opcional de configuração que estende `ContextOptions<Date>`, permitindo especificar (via `options.in`) o contexto/fuso horário ou construtor de data a ser usado para normalizar as datas antes do cálculo.

## 3. Retorno

Um **`number`** (inteiro) representando a quantidade de meses completos entre `laterDate` e `earlierDate`:
- Positivo se `laterDate` for cronologicamente posterior a `earlierDate`.
- Negativo se for anterior.
- `0` se a diferença for menor que um mês completo (incluindo o caso em que o resultado do cálculo dá exatamente zero, normalizado explicitamente para evitar retorno de `-0`).

## Gabarito oficial (date-fns)

- **summary**: Get the number of full months between the given dates.
- **description**: 
