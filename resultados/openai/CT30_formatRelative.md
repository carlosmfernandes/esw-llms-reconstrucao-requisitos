<!-- STATUS: OK -->
# CT30 — formatRelative (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional

Produzir uma **representação textual localizada de uma data em relação a uma data de referência**, escolhendo o formato conforme a diferença em dias de calendário:

| Diferença (`date − baseDate`) | Categoria de formatação |
|---|---|
| Menor que −6 dias | `other` |
| De −6 a −2 dias | `lastWeek` |
| −1 dia | `yesterday` |
| 0 dias | `today` |
| +1 dia | `tomorrow` |
| De +2 a +6 dias | `nextWeek` |
| Maior ou igual a +7 dias | `other` |

Essas categorias são passadas ao locale para definir o padrão de formatação. **O texto exato não pode ser determinado pelo trecho**, pois depende de `locale.formatRelative` e de `format`. As categorias `lastWeek` e `nextWeek` são selecionadas pelos intervalos acima, não por uma verificação de pertencimento à semana anterior ou seguinte.

### 2. Parâmetros de entrada

- **`date: DateArg<Date> & {}`**: data que será formatada. A definição de `DateArg` não está incluída, portanto o trecho não permite enumerar suas representações aceitas.
- **`baseDate: DateArg<Date> & {}`**: data de referência usada para calcular a diferença em dias de calendário.
- **`options?: FormatRelativeOptions`**: configurações opcionais. O código utiliza:
  - **`locale`**: fornece as regras de formatação localizada. Na ausência dessa opção, utiliza o locale das opções globais ou, por último, `defaultLocale`.
  - **`weekStartsOn`**: configuração do início da semana, passada à formatação. Sua precedência é: opção explícita → configuração do locale explícito → opção global → configuração do locale global → `0`.
  - **`in`**: contexto passado a `normalizeDates` para normalizar as duas datas. Os detalhes desse contexto não aparecem no trecho.

### 3. Retorno

Retorna uma **`string` com `date` formatada**, usando o padrão escolhido pelo locale para a categoria relativa calculada.

Se a diferença em dias resultar em `NaN`, a função **lança `RangeError("Invalid time value")`**, em vez de retornar uma string.

## Gabarito oficial (date-fns)

- **summary**: Represent the date in words relative to the given base date.
- **description**: Represent the date in words relative to the given base date.
