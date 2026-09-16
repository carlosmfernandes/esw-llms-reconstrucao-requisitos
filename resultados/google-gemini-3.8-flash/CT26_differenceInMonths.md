<!-- STATUS: OK -->
# CT26 — differenceInMonths (google/gemini-3.8-flash)

## Resposta do LLM

Com base estritamente no código fornecido:

### 1. Requisito funcional
A função implementa o cálculo da **quantidade de meses completos decorridos entre duas datas**, levando em consideração a ordem cronológica entre elas (atribuindo sinal positivo ou negativo conforme a direção no tempo) e ajustando a contagem para desconsiderar meses incompletos (com regras específicas para o último dia do mês e finais de fevereiro).

---

### 2. Parâmetros de entrada
* **`laterDate`**: A primeira data da comparação (nominalmente esperada como a data mais recente ou posterior).
* **`earlierDate`**: A segunda data da comparação (nominalmente esperada como a data mais antiga ou anterior).
* **`options`** *(opcional)*: Objeto de opções/configuração (`DifferenceInMonthsOptions`) que pode conter a propriedade `in`, repassada para o contexto de normalização das datas.

---

### 3. Retorno da função
Retorna um valor numérico (`number`) representando o número de **meses inteiros** entre as duas datas:
* **Positivo**: se `laterDate` for cronologicamente posterior a `earlierDate`.
* **Negativo**: se `laterDate` for cronologicamente anterior a `earlierDate`.
* **`0`**: se as datas forem iguais ou se o intervalo entre elas não atingir um mês completo.

## Gabarito oficial (date-fns)

- **summary**: Get the number of full months between the given dates.
- **description**: 
