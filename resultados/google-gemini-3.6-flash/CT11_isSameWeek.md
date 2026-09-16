<!-- STATUS: OK -->
# CT11 — isSameWeek (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

**1. Requisito funcional**
A função implementa a verificação para determinar se duas datas pertencem à mesma semana (ou seja, se o início da semana calculado para ambas é exatamente o mesmo), levando em consideração eventuais configurações de contexto, localização ou definição de início da semana.

---

**2. Parâmetros de entrada**
* `laterDate` (`DateArg<Date> & {}`): A primeira data a ser comparada (conceitualmente a data mais recente/posterior).
* `earlierDate` (`DateArg<Date> & {}`): A segunda data a ser comparada (conceitualmente a data mais antiga/anterior).
* `options` (`IsSameWeekOptions`, opcional): Objeto de configurações opcionais que contêm parâmetros de contexto (`in`), opções relativas à semana (`WeekOptions`) e de localização (`LocalizedOptions`).

---

**3. O que a função retorna**
Retorna um valor booleano (`boolean`):
* `true`: Se as duas datas pertencerem à mesma semana.
* `false`: Caso pertençam a semanas diferentes.

## Gabarito oficial (date-fns)

- **summary**: Are the given dates in the same week (and month and year)?
- **description**: Are the given dates in the same week (and month and year)?
