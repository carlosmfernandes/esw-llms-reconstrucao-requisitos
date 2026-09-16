<!-- STATUS: OK -->
# CT26 — differenceInMonths (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional**  
   Calcular a diferença **com sinal em meses completos** entre duas datas, descontando o mês que não se completou. O cálculo inclui regras específicas para limites de mês:
   - Ajusta a data de trabalho quando a primeira data está em fevereiro, após o dia 27.
   - Quando a primeira data é posterior à segunda, é o último dia do mês e a diferença de meses de calendário é exatamente 1, considera esse mês completo.

2. **Parâmetros de entrada**
   - **`laterDate: DateArg<Date> & {}`**: primeira data da comparação, nominalmente a data posterior. O código compara as datas, portanto não exige que ela seja realmente a posterior.
   - **`earlierDate: DateArg<Date> & {}`**: segunda data, usada como referência, nominalmente a anterior.
   - **`options?: DifferenceInMonthsOptions`**: opções facultativas. No trecho, somente `options.in` é utilizado, sendo passado a `normalizeDates` como contexto de normalização. A definição desse contexto e os formatos aceitos por `DateArg` não aparecem no código fornecido.

3. **Retorno**  
   Um **`number`** representando a quantidade de meses completos calculada:
   - Positiva se a primeira data for posterior à segunda e houver meses completos.
   - Negativa se a primeira data for anterior à segunda e houver meses completos.
   - `0` quando não houver meses completos segundo essas regras.

   O retorno também converte explicitamente um eventual `-0` em `0`.

## Gabarito oficial (date-fns)

- **summary**: Get the number of full months between the given dates.
- **description**: 
