<!-- STATUS: OK -->
# CT17 — areIntervalsOverlapping (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

1. **Requisito funcional:**
   A função verifica se dois intervalos temporais se sobrepõem (possuem interseção no tempo). Ela normaliza a ordem cronológica das datas de cada intervalo e avalia se há colisão temporal entre eles, permitindo configurar se o contato apenas nos limites/extremidades dos intervalos deve ser considerado ou não uma sobreposição.

2. **Parâmetros de entrada:**
   * `intervalLeft`: O primeiro intervalo temporal a ser comparado, contendo as propriedades `start` (início) e `end` (fim).
   * `intervalRight`: O segundo intervalo temporal a ser comparado, também contendo `start` e `end`.
   * `options` *(opcional)*: Objeto de opções que pode conter:
     * `inclusive` *(opcional)*: Define se a sobreposição deve ser inclusiva nas bordas (se `true`, intervalos que apenas se tocam no mesmo instante são considerados sobrepostos).
     * `in` *(opcional, herdado de `ContextOptions`)*: Parâmetro de contexto repassado para a conversão das datas via `toDate`.

3. **Retorno:**
   * Retorna um valor booleano (`true` ou `false`): `true` se os intervalos se sobrepuserem segundo a regra de inclusão definida, e `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Is the given time interval overlapping with another time interval?
- **description**: Is the given time interval overlapping with another time interval? Adjacent intervals do not count as overlapping unless `inclusive` is set to `true`.
