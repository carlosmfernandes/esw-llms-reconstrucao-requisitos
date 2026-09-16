<!-- STATUS: OK -->
# CT27 — formatDuration (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, seguem as respostas:

### 1. Requisito funcional
A função tem como objetivo converter um objeto de duração de tempo em uma representação textual legível por humanos e localizada (de acordo com um idioma/localidade). Ela permite configurar quais unidades de tempo serão exibidas (e em qual ordem), se unidades com valor zero devem aparecer no texto e qual delimitador deve separar as partes da duração.

---

### 2. Parâmetros de entrada

* **`duration` (`Duration`)**: Objeto que contém os valores numéricos das unidades de tempo que compõem a duração (como anos, meses, semanas, dias, horas, minutos, segundos).
* **`options` (`FormatDurationOptions`, opcional)**: Objeto com opções de personalização da formatação, contendo:
  * **`locale`** *(herdado de `LocalizedOptions`)*: Objeto de localização/idioma responsável por fornecer a função de tradução/formatação textual (`formatDistance`). Se omitido, usa a localidade padrão.
  * **`format` (`DurationUnit[]`)**: Lista de unidades de tempo a serem consideradas e a ordem em que devem aparecer na saída formatada (o padrão contempla de anos a segundos).
  * **`zero` (`boolean`)**: Flag que indica se unidades cujo valor seja `0` devem ser incluídas na formatação final (padrão: `false`).
  * **`delimiter` (`string`)**: Caractere ou texto utilizado para unir/separar cada unidade de tempo formatada (padrão: um espaço em branco `" "`).

---

### 3. O que a função retorna

Retorna uma **`string`**:
* O texto concatenado com as unidades de tempo formatadas e traduzidas, separadas pelo delimitador configurado.
* Uma **string vazia (`""`)** caso a localidade informada (ou padrão) não possua a implementação da função `formatDistance`, ou caso nenhuma unidade atenda aos critérios de inclusão.

## Gabarito oficial (date-fns)

- **summary**: Formats a duration in human-readable format
- **description**: Return human-readable duration string i.e. "9 months 2 days"
