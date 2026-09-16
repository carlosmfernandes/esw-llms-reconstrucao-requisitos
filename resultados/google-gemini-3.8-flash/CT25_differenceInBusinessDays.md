<!-- STATUS: OK -->
# CT25 — differenceInBusinessDays (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

### 1. Requisito funcional
A função calcula a **quantidade de dias úteis** (desconsiderando finais de semana) existentes entre duas datas. O cálculo preserva o sentido temporal: o resultado é positivo se a primeira data for posterior à segunda, negativo se for anterior, ou zero se coincidirem no mesmo dia ou não houver dias úteis no intervalo.

---

### 2. Parâmetros de entrada
* **`laterDate`** (`DateArg<Date> & {}`): A primeira data da comparação (nominalmente a data posterior/mais recente).
* **`earlierDate`** (`DateArg<Date> & {}`): A segunda data da comparação (nominalmente a data anterior/mais antiga).
* **`options`** (`DifferenceInBusinessDaysOptions | undefined`, opcional): Objeto de configurações de contexto (contendo a propriedade `in`), utilizado para a normalização das datas e repassado para a verificação de finais de semana.

---

### 3. O que a função retorna
Retorna um valor numérico (`number`):
* O **número inteiro de dias úteis** entre as datas (positivo, negativo ou `0`).
* **`NaN`**, caso qualquer uma das duas datas de entrada seja inválida.

## Gabarito oficial (date-fns)

- **summary**: Get the number of business days between the given dates.
- **description**: Get the number of business day periods between the given dates. Business days being days that aren't in the weekend. Like `differenceInCalendarDays`, the function removes the times from the dates before calculating the difference.
