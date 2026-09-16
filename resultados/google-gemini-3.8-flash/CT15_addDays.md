<!-- STATUS: OK -->
# CT15 — addDays (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no trecho de código fornecido:

1. **Requisito Funcional:**
   A função tem como objetivo adicionar uma quantidade determinada de dias a uma data fornecida, gerando uma nova data correspondente ao deslocamento solicitado (ou mantendo a data inalterada caso o valor seja zero, e retornando uma data inválida se o valor de dias não for um número válido).

2. **Parâmetros de Entrada:**
   * **`date`** (`DateArg<DateType>`): A data inicial de referência que será manipulada.
   * **`amount`** (`number`): A quantidade de dias a ser adicionada à data (pode ser positiva, negativa ou zero).
   * **`options`** (`AddDaysOptions<ResultDate> | undefined`, opcional): Objeto de configurações que define o contexto para conversão e construção da data (por meio da propriedade `options.in`).

3. **Retorno:**
   * Retorna um objeto de data (`ResultDate`) com a quantidade de dias adicionada.
   * Caso `amount` seja `0`, retorna a data convertida sem alterações.
   * Caso `amount` seja `NaN`, retorna uma data inválida (construída a partir de `NaN`).

## Gabarito oficial (date-fns)

- **summary**: Add the specified number of days to the given date.
- **description**: Add the specified number of days to the given date.
