<!-- STATUS: OK -->
# CT27 — formatDuration (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `formatDuration`

## 1. Requisito funcional

A função implementa a formatação de um objeto de duração (composto por unidades de tempo como anos, meses, semanas, dias, horas, minutos e segundos) em uma string legível por humanos, de acordo com um locale específico.

O requisito é permitir que o desenvolvedor exiba uma duração (por exemplo, resultado de cálculos de diferença entre datas) como texto formatado, com controle sobre:
- **Quais unidades** devem aparecer na saída (via parâmetro `format`);
- **Se unidades com valor zero** devem ser exibidas ou omitidas (via parâmetro `zero`);
- **Qual separador** usar entre as partes formatadas (via parâmetro `delimiter`);
- **Em qual idioma/locale** o texto deve ser gerado.

A lógica percorre as unidades especificadas em `format`, e para cada uma que possui valor definido em `duration` (e que não seja zero, a menos que `zero` seja `true`), monta um "token" (ex: `xYears`, `xMonths`) e delega à função `formatDistance` do locale a tradução desse valor para texto. Os textos resultantes são concatenados usando o delimitador definido.

## 2. Parâmetros de entrada

- **`duration: Duration`** — objeto contendo a duração a ser formatada, com propriedades opcionais para cada unidade de tempo (years, months, weeks, days, hours, minutes, seconds), cada uma com um valor numérico.

- **`options?: FormatDurationOptions`** — objeto opcional de configuração, contendo:
  - **`locale`** — locale a ser usado para tradução/formatação (herdado de `LocalizedOptions<"formatDistance">`). Se não informado, usa o locale padrão configurado globalmente ou o `defaultLocale`.
  - **`format?: DurationUnit[]`** — array indicando quais unidades de tempo devem ser incluídas na saída e em que ordem. Padrão: `["years", "months", "weeks", "days", "hours", "minutes", "seconds"]`.
  - **`zero?: boolean`** — indica se unidades com valor zero devem ser incluídas no resultado. Padrão: `false` (unidades zeradas são omitidas).
  - **`delimiter?: string`** — string usada para separar as partes formatadas no resultado final. Padrão: `" "` (espaço).

## 3. Retorno

A função retorna uma **`string`** contendo a duração formatada por extenso, com as unidades concatenadas pelo delimitador especificado.

Caso o locale não possua a propriedade `formatDistance` definida, a função retorna uma **string vazia** (`""`).

## Gabarito oficial (date-fns)

- **summary**: Formats a duration in human-readable format
- **description**: Return human-readable duration string i.e. "9 months 2 days"
