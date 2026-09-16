<!-- STATUS: OK -->
# CT28 — eachWeekOfInterval (anthropic/claude-sonnet-5)

## Resposta do LLM

## 1. Requisito funcional

A função gera um array com o **início de cada semana** compreendida entre as datas de início e fim de um intervalo (`interval`). Ou seja, dado um intervalo de datas, ela retorna todas as datas correspondentes ao primeiro dia de cada semana (conforme configuração de qual dia inicia a semana) que estão contidas nesse intervalo.

Características adicionais do comportamento especificado:
- Funciona corretamente mesmo se `start` for posterior a `end` (intervalo "invertido"), retornando os resultados na ordem correspondente.
- Permite pular semanas usando um "passo" (`step`), incluindo passos negativos, que invertem a ordem do resultado.
- Se `step` for `0`, retorna um array vazio.
- Usa manipulação de hora (`setHours(15)` / `setHours(0)`) como estratégia interna para evitar problemas de horário de verão (DST) ao comparar/adicionar semanas — isso é detalhe de implementação, não requisito funcional em si.

## 2. Parâmetros de entrada

- **`interval: IntervalType`**: objeto contendo `start` e `end`, representando o intervalo de datas a ser percorrido (as datas podem ser de tipos diferentes, como `Date`, string, number, etc., dependendo do contexto usado pela biblioteca).

- **`options?: EachWeekOfIntervalOptions<DateType>`** (opcional): objeto de configuração que pode conter:
  - **`step`**: número de semanas a avançar a cada iteração (padrão 1); se negativo, inverte a ordem do resultado; se zero, retorna array vazio.
  - Opções herdadas de `WeekOptions` (ex.: `weekStartsOn`), que definem qual dia da semana é considerado o início (usado por `startOfWeek`).
  - Opções herdadas de `LocalizedOptions<"options">` (ex.: `locale`), usadas para localização (repassadas a `startOfWeek`).
  - **`in`** (de `ContextOptions<DateType>`): contexto/construtor usado para normalizar/criar as datas de retorno (repassado a `normalizeInterval` e `constructFrom`).

## 3. Retorno

Um **array de datas** (`EachWeekOfIntervalResult`), onde cada elemento representa o início de uma semana dentro do intervalo fornecido, espaçadas de acordo com o `step`. A ordem do array respeita a ordem original do intervalo (crescente ou decrescente, conforme `start` e `end`, e ajustada se `step` for negativo). O tipo de cada elemento do array é inferido a partir das opções (`options.in`) ou das datas do próprio intervalo.

## Gabarito oficial (date-fns)

- **summary**: Return the array of weeks within the specified time interval.
- **description**: Return the array of weeks within the specified time interval.
