<!-- STATUS: OK -->
# CT01 — isLeapYear (google/gemini-3.8-flash)

## Resposta do LLM

Com base estritamente no código fornecido, seguem as respostas:

1. **Requisito funcional:**  
   Determinar se o ano correspondente a uma data informada é um ano bissexto.

2. **Parâmetros de entrada:**  
   * `date` (`DateArg<Date> & {}`): A data (ou representação de data) cujo ano será verificado.
   * `options` (`IsLeapYearOptions | undefined`, opcional): Um objeto de opções de contexto contendo a propriedade `in` (usada internamente na conversão da data via `toDate`).

3. **Retorno:**  
   Um valor booleano (`boolean`): retorna `true` se o ano da data for bissexto (divisível por 400 ou divisível por 4 e não por 100) e `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Is the given date in the leap year?
- **description**: Is the given date in the leap year?
