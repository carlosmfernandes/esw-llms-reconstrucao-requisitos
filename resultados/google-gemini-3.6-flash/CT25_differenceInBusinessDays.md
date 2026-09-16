<!-- STATUS: OK -->
# CT25 — differenceInBusinessDays (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código-fonte fornecido, seguem as respostas:

### 1. Requisito Funcional
A função calcula a **diferença em dias úteis** (desconsiderando os dias de fim de semana) entre duas datas. O cálculo identifica quantos dias não são fins de semana no intervalo fornecido, respeitando a ordem cronológica entre as datas (retornando um número positivo se a primeira data for posterior à segunda, ou negativo caso seja anterior).

---

### 2. Parâmetros de Entrada

* **`laterDate`** (`DateArg<Date> & {}`): A primeira data para a comparação (representa a data teoricamente posterior).
* **`earlierDate`** (`DateArg<Date> & {}`): A segunda data para a comparação (representa a data teoricamente anterior).
* **`options`** (`DifferenceInBusinessDaysOptions | undefined`, opcional): Objeto opcional contendo configurações de contexto (como a opção `in` para normalização de datas) que também são repassadas para a verificação de fim de semana (`isWeekend`).

---

### 3. Retorno
A função retorna um valor do tipo **`number`**:
* O número total de **dias úteis** no intervalo entre as duas datas (positivo, negativo ou `0`).
* O valor **`NaN`**, caso pelo menos uma das datas de entrada seja inválida.

## Gabarito oficial (date-fns)

- **summary**: Get the number of business days between the given dates.
- **description**: Get the number of business day periods between the given dates. Business days being days that aren't in the weekend. Like `differenceInCalendarDays`, the function removes the times from the dates before calculating the difference.
