<!-- STATUS: OK -->
# CT03 — isWeekend (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no trecho de código fornecido:

1. **Requisito funcional:**
   Verificar se uma determinada data corresponde a um final de semana (sábado ou domingo).

2. **Parâmetros de entrada:**
   * **`date`** (`DateArg<Date> & {}`): A data que se deseja verificar.
   * **`options`** (`IsWeekendOptions | undefined`, opcional): Objeto de opções/contexto que contém a propriedade `in`, repassada para a função de conversão `toDate`.

3. **Retorno:**
   Um valor booleano (`boolean`): retorna `true` se o dia da semana for domingo (`0`) ou sábado (`6`); caso contrário, retorna `false`.

## Gabarito oficial (date-fns)

- **summary**: Does the given date fall on a weekend?
- **description**: Does the given date fall on a weekend? A weekend is either Saturday (`6`) or Sunday (`0`).
