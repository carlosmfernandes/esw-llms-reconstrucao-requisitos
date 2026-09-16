# CT03 — isWeekend (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

**1. Requisito funcional**
A função determina se uma determinada data corresponde a um dia do final de semana (sábado ou domingo).

**2. Parâmetros de entrada**
* `date` (`DateArg<Date> & {}`): A data que será avaliada.
* `options` (`IsWeekendOptions | undefined`, opcional): Um objeto de opções que permite passar configurações adicionais de contexto (especificamente a propriedade `in`, utilizada para a conversão/interpretação da data).

**3. Retorno da função**
Retorna um valor booleano (`boolean`):
* `true` se a data for um final de semana (domingo, dia `0`, ou sábado, dia `6`).
* `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Does the given date fall on a weekend?
- **description**: Does the given date fall on a weekend? A weekend is either Saturday (`6`) or Sunday (`0`).
