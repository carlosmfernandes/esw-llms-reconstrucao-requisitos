<!-- STATUS: OK -->
# CT20 — startOfWeek (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional
Obter a data correspondente ao **início da semana que contém a data informada**, ajustando o horário para **00:00:00.000**.

O primeiro dia da semana é definido pelo primeiro valor não nulo nem indefinido nesta ordem:
1. `options.weekStartsOn`;
2. `options.locale.options.weekStartsOn`;
3. `defaultOptions.weekStartsOn`;
4. `defaultOptions.locale.options.weekStartsOn`;
5. `0` (domingo).

O cálculo usa os métodos de data locais (`getDay`, `setDate` e `setHours`), não os métodos UTC.

### 2. Parâmetros de entrada
- **`date: DateArg<DateType>`**: a data de referência para identificar a semana. É convertida por `toDate`. Como a definição de `DateArg` não foi fornecida, não é possível enumerar todos os formatos de entrada aceitos.
- **`options?: StartOfWeekOptions<ResultDate>`**: configurações opcionais. Os campos utilizados são:
  - **`weekStartsOn`**: dia que deve ser considerado o início da semana, conforme a numeração de `getDay()` (`0` = domingo até `6` = sábado). O trecho não valida esse valor.
  - **`locale.options.weekStartsOn`**: configuração alternativa do primeiro dia da semana.
  - **`in`**: argumento encaminhado a `toDate`; seu comportamento específico não está definido no trecho.

### 3. Retorno
Retorna **`ResultDate`**, um tipo que estende `Date`, representando o primeiro dia da semana calculada, à meia-noite.

O objeto retornado é aquele produzido por `toDate`, após os ajustes. Sem a implementação de `toDate`, não é possível afirmar se ele é um novo objeto ou se pode ser o próprio objeto recebido.

## Gabarito oficial (date-fns)

- **summary**: Return the start of a week for the given date.
- **description**: Return the start of a week for the given date. The result will be in the local timezone.
