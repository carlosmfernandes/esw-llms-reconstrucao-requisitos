# CT04 — daysToWeeks (google/gemini-3.6-flash)

## Resposta do LLM

Com base estritamente no código fornecido, aqui estão as respostas:

1. **Requisito funcional:**
   Converter uma determinada quantidade de dias no número correspondente de semanas completas (inteiras), descartando qualquer fração de semana resultante da divisão e garantindo que zero não seja retornado como um zero negativo (`-0`).

2. **Parâmetros de entrada:**
   * `days` (tipo `number`): representa a quantidade total de dias que se deseja converter em semanas.

3. **Retorno da função:**
   Retorna um número (`number`) inteiro truncado que representa a quantidade de semanas inteiras resultantes da conversão dos dias informados (retornando `0` caso o resultado da divisão truncada seja zero).

## Gabarito oficial (date-fns)

- **summary**: Convert days to weeks.
- **description**: Convert a number of days to a full number of weeks.
