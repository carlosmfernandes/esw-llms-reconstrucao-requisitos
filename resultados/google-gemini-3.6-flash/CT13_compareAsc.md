<!-- STATUS: OK -->
# CT13 — compareAsc (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas para os três pontos solicitados:

### 1. Requisito Funcional
A função implementa a **comparação cronológica crescente entre duas datas**. O objetivo é determinar a ordem de precedência entre duas datas para fins de ordenação (saber se a primeira data é anterior, posterior ou igual à segunda data, ou se a comparação é inválida).

### 2. Parâmetros de Entrada
A função aceita dois parâmetros de entrada:
* **`dateLeft`** (tipo `DateArg<Date> & {}`): Representa a primeira data (ou um argumento conversível para data) a ser comparada.
* **`dateRight`** (tipo `DateArg<Date> & {}`): Representa a segunda data (ou um argumento conversível para data) a ser comparada com a primeira.

### 3. Retorno da Função
A função retorna um número (`number`), que pode ser:
* **`-1`**: se `dateLeft` for cronologicamente **anterior** a `dateRight`.
* **`1`**: se `dateLeft` for cronologicamente **posterior** a `dateRight`.
* **`0`**: se ambas as datas representarem o **mesmo instante**.
* **`NaN`**: se a comparação resultar em um valor não numérico (caso uma ou ambas as datas sejam inválidas).

## Gabarito oficial (date-fns)

- **summary**: Compare the two dates and return -1, 0 or 1.
- **description**: Compare the two dates and return 1 if the first date is after the second, -1 if the first date is before the second or 0 if dates are equal.
