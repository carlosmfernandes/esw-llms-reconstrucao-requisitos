<!-- STATUS: OK -->
# CT27 — formatDuration (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional
Converter uma duração em uma **representação textual localizada**, permitindo escolher quais unidades exibir, sua ordem, a inclusão de valores iguais a zero e o separador entre as partes. A função formata os valores fornecidos, sem realizar conversão entre unidades.

### 2. Parâmetros de entrada
- **`duration: Duration`**: objeto com os valores da duração por unidade. As unidades do formato padrão são: anos (`years`), meses (`months`), semanas (`weeks`), dias (`days`), horas (`hours`), minutos (`minutes`) e segundos (`seconds`). Valores `undefined` não são exibidos.
- **`options?: FormatDurationOptions`**: configurações opcionais:
  - **`locale`**: fornece a função `formatDistance`, responsável pelo texto de cada unidade. Na ausência de um locale explícito, usa o das opções globais ou, se também ausente, `defaultLocale`.
  - **`format`**: lista das unidades a exibir, na ordem desejada. Por padrão, usa as sete unidades acima, nessa ordem.
  - **`zero`**: controla a inclusão de valores zero. O padrão é `false`; com `true`, zeros são incluídos, mas valores `undefined` continuam omitidos.
  - **`delimiter`**: texto usado para separar as partes formatadas. O padrão é um espaço (`" "`).

### 3. Retorno
Uma **`string`** com as partes formatadas por `locale.formatDistance` e unidas pelo separador escolhido.

Retorna `""` se o locale selecionado não disponibilizar `formatDistance` ou se nenhuma unidade for incluída no resultado.

## Gabarito oficial (date-fns)

- **summary**: Formats a duration in human-readable format
- **description**: Return human-readable duration string i.e. "9 months 2 days"
