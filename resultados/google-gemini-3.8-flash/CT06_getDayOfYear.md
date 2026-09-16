<!-- STATUS: OK -->
# CT06 — getDayOfYear (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no trecho de código fornecido, seguem as respostas:

1. **Requisito funcional que a função implementa:**  
   Obter o dia do ano (o número ordinal do dia dentro do respectivo ano civil) para uma determinada data de referência (sendo 1 o primeiro dia do ano).

2. **Parâmetros de entrada:**  
   * `date` (`DateArg<Date> & {}`): A data a partir da qual o dia do ano será calculado (convertida internamente para um objeto de data).
   * `options` (`GetDayOfYearOptions | undefined`, opcional): Objeto de opções adicionais de contexto (que estende `ContextOptions<Date>`), contendo a propriedade opcional `in` utilizada para contextualizar a conversão da data.

3. **Retorno da função:**  
   Retorna um número (`number`) que representa o dia do ano correspondente à data informada.

## Gabarito oficial (date-fns)

- **summary**: Get the day of the year of the given date.
- **description**: Get the day of the year of the given date.
