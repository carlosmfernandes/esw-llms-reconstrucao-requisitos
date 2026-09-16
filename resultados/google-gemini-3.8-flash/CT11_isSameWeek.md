<!-- STATUS: OK -->
# CT11 — isSameWeek (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

1. **Requisito funcional:**
   A função verifica se duas datas informadas pertencem à mesma semana (considerando possíveis parametrizações de início de semana, localidade ou contexto).

2. **Parâmetros de entrada:**
   * `laterDate` (`DateArg<Date> & {}`): A primeira data a ser avaliada (nomeada como a data mais recente/posterior).
   * `earlierDate` (`DateArg<Date> & {}`): A segunda data a ser avaliada (nomeada como a data mais antiga/anterior).
   * `options` (`IsSameWeekOptions`, opcional): Objeto contendo configurações adicionais para a operação, tais como contexto de normalização (`options?.in`), além de opções de semana e localização herdadas das interfaces estendidas (`WeekOptions`, `LocalizedOptions`, `ContextOptions`).

3. **Retorno:**
   * Retorna um valor booleano (`boolean`): `true` se ambas as datas estiverem na mesma semana (tiverem a mesma data/horário de início de semana calculada por `startOfWeek`) ou `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Are the given dates in the same week (and month and year)?
- **description**: Are the given dates in the same week (and month and year)?
