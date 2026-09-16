<!-- STATUS: OK -->
# CT26 — differenceInMonths (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código TypeScript fornecido, aqui está a análise solicitada:

### 1. Requisito Funcional
A função calcula a **quantidade de meses completos passados entre duas datas**. 

Diferente de uma simples diferença de meses de calendário (ex: de 31 de janeiro a 1 de fevereiro), ela valida se um mês inteiro realmente se completou em termos de dias, considerando a ordem das datas (retorna valor positivo se a primeira data for posterior à segunda, ou negativo caso seja anterior) e tratando casos de borda como o fim do mês e o mês de fevereiro.

---

### 2. Parâmetros de Entrada

* **`laterDate`** (`DateArg<Date> & {}`): A primeira data para a comparação (nominalmente a data mais recente ou final do intervalo).
* **`earlierDate`** (`DateArg<Date> & {}`): A segunda data para a comparação (nominalmente a data mais antiga ou inicial do intervalo).
* **`options`** (`DifferenceInMonthsOptions | undefined`, opcional): Objeto opcional de configurações que aceita a propriedade `in` (herdada de `ContextOptions<Date>`), utilizada no processo de normalização do contexto/fuso das datas.

---

### 3. Retorno da Função

Retorna um número (**`number`**):
* O total inteiro de **meses completos** entre as duas datas.
* **Positivo** se `laterDate` for posterior a `earlierDate`.
* **Negativo** se `laterDate` for anterior a `earlierDate`.
* **`0`** se o tempo decorrido entre as datas for inferior a um mês completo ou se o resultado calculado for `-0`.

## Gabarito oficial (date-fns)

- **summary**: Get the number of full months between the given dates.
- **description**: 
