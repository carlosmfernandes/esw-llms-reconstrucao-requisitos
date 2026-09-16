<!-- STATUS: OK -->
# CT27 — formatDuration (google/gemini-3.6-flash)

## Resposta do LLM

Com base estritamente no código fornecido, seguem as respostas para os três pontos solicitados:

---

### 1. Requisito Funcional
A função tem como objetivo **converter uma estrutura de duração de tempo em uma string de texto formatada e localizada (traduzida)**. Ela permite transformar valores numéricos de tempo (como anos, meses, dias, horas, etc.) em uma representação legível por humanos, oferecendo personalização sobre quais unidades exibir, a inclusão ou omissão de valores zerados e o caractere de separação entre as partes.

---

### 2. Parâmetros de Entrada

*   **`duration`** (tipo `Duration`): Objeto que contém os valores numéricos da duração a ser formatada, organizados por propriedades de unidades de tempo (ex.: anos, meses, dias, etc.).
*   **`options`** (tipo `FormatDurationOptions`, opcional): Objeto de configuração para personalizar o resultado final, composto por:
    *   **`format`** (`DurationUnit[]`, opcional): Lista com a ordem e quais unidades de tempo devem ser processadas. Se omitido, utiliza uma lista padrão (`["years", "months", "weeks", "days", "hours", "minutes", "seconds"]`).
    *   **`zero`** (`boolean`, opcional): Flag booleana que indica se unidades com valor igual a `0` (ou não definidos/falsy) devem ser incluídas no resultado final. O padrão é `false`.
    *   **`delimiter`** (`string`, opcional): Texto/caractere utilizado para separar cada uma das unidades formatadas na string final. O padrão é um espaço em branco (`" "`).
    *   **`locale`** (opcional, herdado de `LocalizedOptions`): Objeto de localização que fornece as regras de tradução/formatação (função `formatDistance`) para cada unidade. Se omitido, recorre às opções padrão ou ao `defaultLocale`.

---

### 3. Retorno da Função

Retorna uma **`string`**:
*   A representação textual e concatenada (utilizando o `delimiter`) das unidades de tempo formatadas.
*   Retorna uma string vazia (`""`) caso o objeto de localização (`locale`) fornecido não possua o método `formatDistance`.

## Gabarito oficial (date-fns)

- **summary**: Formats a duration in human-readable format
- **description**: Return human-readable duration string i.e. "9 months 2 days"
