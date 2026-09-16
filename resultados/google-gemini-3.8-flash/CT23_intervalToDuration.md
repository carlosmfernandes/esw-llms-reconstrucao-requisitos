<!-- STATUS: OK -->
# CT23 — intervalToDuration (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, seguem as respostas:

1. **Requisito funcional que a função implementa:**
   A função converte um intervalo de datas (delimitado por um início e um fim) em uma duração discriminada em unidades de tempo (anos, meses, dias, horas, minutos e segundos), calculando a diferença acumulada e progressiva entre os dois pontos no tempo.

2. **Parâmetros de entrada e o que representam:**
   * `interval` (`Interval`): Representa o intervalo de tempo a ser calculado/convertido (do qual são extraídos os pontos inicial `start` e final `end`).
   * `options` (`IntervalToDurationOptions | undefined`, opcional): Objeto de opções/contexto (que estende `ContextOptions<Date>`), do qual a propriedade `in` é utilizada como contexto na normalização do intervalo (`normalizeInterval`).

3. **O que a função retorna:**
   Retorna um objeto do tipo `Duration`, contendo as propriedades de tempo (`years`, `months`, `days`, `hours`, `minutes` e `seconds`) preenchidas apenas com os valores que forem diferentes de zero (ou seja, caso alguma unidade resulte em `0`, ela não é incluída no objeto).

## Gabarito oficial (date-fns)

- **summary**: Convert interval to duration
- **description**: Convert an interval object to a duration object.
