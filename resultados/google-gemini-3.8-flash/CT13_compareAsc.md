<!-- STATUS: OK -->
# CT13 — compareAsc (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no trecho de código fornecido:

1. **Requisito funcional que a função implementa:**
   A função implementa a comparação cronológica entre duas datas em ordem ascendente (crescente), servindo como uma função comparadora para determinar qual data ocorre antes, se ocorrem no mesmo instante, ou se a comparação é inválida.

2. **Parâmetros de entrada e seus significados:**
   * **`dateLeft`** (`DateArg<Date> & {}`): A primeira data a ser comparada (termo da esquerda da comparação).
   * **`dateRight`** (`DateArg<Date> & {}`): A segunda data a ser comparada (termo da direita da comparação).

3. **O que a função retorna:**
   Retorna um valor numérico (`number`), sendo:
   * **`-1`**: se a primeira data (`dateLeft`) for anterior à segunda (`dateRight`).
   * **`1`**: se a primeira data (`dateLeft`) for posterior à segunda (`dateRight`).
   * **`0`**: se ambas as datas representarem o mesmo momento no tempo.
   * **`NaN`**: se a diferença calculada não for um número (por exemplo, caso uma ou ambas as datas sejam inválidas).

## Gabarito oficial (date-fns)

- **summary**: Compare the two dates and return -1, 0 or 1.
- **description**: Compare the two dates and return 1 if the first date is after the second, -1 if the first date is before the second or 0 if dates are equal.
