<!-- STATUS: OK -->
# CT08 — differenceInSeconds (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** calcular a diferença entre duas datas em segundos, a partir da diferença em milissegundos dividida por 1.000, e aplicar um método de arredondamento ao resultado.

2. **Parâmetros de entrada:**
   - `laterDate: DateArg<Date> & {}`: primeira data, indicada pelo nome como a data posterior.
   - `earlierDate: DateArg<Date> & {}`: segunda data, indicada pelo nome como a data anterior. O trecho não valida a ordem das datas.
   - `options?: DifferenceInSecondsOptions`: opções facultativas de arredondamento. A propriedade `roundingMethod` é passada a `getRoundingMethod` para selecionar o método aplicado. Os métodos aceitos e o comportamento padrão não estão definidos no trecho.

   A definição de `DateArg` não foi fornecida, portanto não é possível enumerar os formatos de data aceitos.

3. **Retorno:** um `number` com a diferença em segundos após a aplicação do método de arredondamento.

## Gabarito oficial (date-fns)

- **summary**: Get the number of seconds between the given dates.
- **description**: Get the number of seconds between the given dates.
