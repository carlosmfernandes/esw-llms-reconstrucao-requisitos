<!-- STATUS: OK -->
# CT07 — getQuarter (google/gemini-3.8-flash)

## Resposta do LLM

Com base estritamente no código fornecido:

**1. Requisito funcional**
A função tem como objetivo identificar e obter o número do trimestre do ano correspondente a uma data informada.

**2. Parâmetros de entrada**
* `date` (`DateArg<Date> & {}`): A data de referência a partir da qual se deseja calcular o trimestre.
* `options` (`GetQuarterOptions | undefined`, opcional): Objeto de configurações adicionais de contexto, que pode conter a propriedade `in` utilizada na conversão/normalização da data (via `toDate`).

**3. Retorno da função**
Retorna um valor numérico (`number`) que representa o trimestre do ano da data avaliada (calculado com base no mês).

## Gabarito oficial (date-fns)

- **summary**: Get the year quarter of the given date.
- **description**: Get the year quarter of the given date.
