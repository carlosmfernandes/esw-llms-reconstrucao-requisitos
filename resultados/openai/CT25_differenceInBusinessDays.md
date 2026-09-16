<!-- STATUS: OK -->
# CT25 — differenceInBusinessDays (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional

Calcular a **diferença com sinal em dias úteis entre duas datas**, considerando cinco dias úteis por semana completa e desconsiderando, nos dias restantes, aqueles classificados como fim de semana por `isWeekend`.

A contagem:
- Parte de `earlierDate` em direção a `laterDate`, **incluindo o dia de `earlierDate` e excluindo o de `laterDate`**.
- É positiva ou zero quando `laterDate` está depois de `earlierDate`, e negativa ou zero quando a ordem está invertida.
- Usa dias de calendário, não períodos completos de 24 horas.
- Não contém tratamento explícito de feriados.

O trecho não mostra quais dias `isWeekend` classifica como fim de semana.

### 2. Parâmetros de entrada

- **`laterDate: DateArg<Date> & {}`**: data de destino da contagem. Apesar do nome, o código permite que seja anterior à outra data.
- **`earlierDate: DateArg<Date> & {}`**: data de partida da contagem.
- **`options?: DifferenceInBusinessDaysOptions`**: opções facultativas de contexto. A propriedade `in` é passada para a normalização das datas, e `options` também é encaminhado a `isWeekend`. Os detalhes dessas opções não estão definidos no trecho.

Os formatos aceitos por `DateArg` também não são apresentados no código fornecido.

### 3. Retorno

Um **`number`** que representa:
- A diferença inteira, com sinal, em dias úteis.
- **`0`** quando a contagem é nula, inclusive quando as datas correspondem ao mesmo dia; o código evita retornar `-0`.
- **`NaN`** se alguma das datas, após a normalização, for inválida.

## Gabarito oficial (date-fns)

- **summary**: Get the number of business days between the given dates.
- **description**: Get the number of business day periods between the given dates. Business days being days that aren't in the weekend. Like `differenceInCalendarDays`, the function removes the times from the dates before calculating the difference.
