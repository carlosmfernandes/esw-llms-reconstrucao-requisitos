<!-- STATUS: OK -->
# CT02 — getISODay (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no trecho de código fornecido, seguem as respostas:

1. **Requisito funcional:**
   A função tem como objetivo calcular e obter o número correspondente ao dia da semana de uma data no formato padrão ISO (onde a contagem vai de 1 a 7, ajustando o domingo — originalmente representado por 0 pelo método `getDay()` — para o valor 7).

2. **Parâmetros de entrada:**
   * `date` (`DateArg<Date> & {}`): Representa a data (ou argumento que define a data) da qual se deseja extrair o dia da semana.
   * `options` (opcional, do tipo `GetISODayOptions`): Representa um objeto de configurações adicionais de contexto (contendo a propriedade `in`, herdada de `ContextOptions<Date>`), utilizado para parametrizar a conversão da data pela função `toDate`.

3. **Retorno da função:**
   Retorna um número (`number`) que representa o dia da semana, sendo um valor de 1 a 6 caso o dia não seja 0, ou 7 caso o valor obtido seja 0.

## Gabarito oficial (date-fns)

- **summary**: Get the day of the ISO week of the given date.
- **description**: Get the day of the ISO week of the given date, which is 7 for Sunday, 1 for Monday etc.
