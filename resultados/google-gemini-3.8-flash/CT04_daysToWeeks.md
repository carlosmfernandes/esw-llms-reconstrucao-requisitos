<!-- STATUS: OK -->
# CT04 — daysToWeeks (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

1. **Requisito funcional:**  
   Converter uma determinada quantidade de dias no número correspondente de semanas inteiras (com o valor truncado, descartando partes fracionárias) e assegurar que o resultado nunca seja retornado como zero negativo (`-0`).

2. **Parâmetros de entrada:**  
   * `days` (tipo `number`): Representa a quantidade de dias que se deseja converter para semanas.

3. **Retorno:**  
   * Um valor numérico (tipo `number`) correspondente à quantidade inteira truncada de semanas resultantes da conversão, sendo `0` caso o truncamento resulte em zero.

## Gabarito oficial (date-fns)

- **summary**: Convert days to weeks.
- **description**: Convert a number of days to a full number of weeks.
