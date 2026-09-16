<!-- STATUS: OK -->
# CT08 — differenceInSeconds (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

1. **Requisito funcional:**
   A função calcula a diferença de tempo em segundos entre duas datas, permitindo aplicar um método de arredondamento específico ao resultado.

2. **Parâmetros de entrada:**
   * `laterDate` (`DateArg<Date> & {}`): A data final (ou mais recente) a ser comparada.
   * `earlierDate` (`DateArg<Date> & {}`): A data inicial (ou anterior) a ser comparada.
   * `options` (`DifferenceInSecondsOptions`, opcional): Objeto de opções que permite configurar a estratégia de arredondamento (`roundingMethod`) para o cálculo.

3. **Retorno:**
   * Retorna um número (`number`) que representa a quantidade de segundos resultante da diferença entre as duas datas, após a aplicação do método de arredondamento.

## Gabarito oficial (date-fns)

- **summary**: Get the number of seconds between the given dates.
- **description**: Get the number of seconds between the given dates.
