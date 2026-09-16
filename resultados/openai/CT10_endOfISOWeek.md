<!-- STATUS: OK -->
# CT10 — endOfISOWeek (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** obter o fim da semana ISO correspondente à data informada. Para isso, a função delega o cálculo a `endOfWeek`, impondo `weekStartsOn: 1`. Esse valor prevalece sobre qualquer configuração de mesmo nome em `options`. O trecho não mostra como `endOfWeek` calcula o instante final da semana.

2. **Parâmetros de entrada:**
   - **`date: DateArg<DateType>`**: data de referência para o cálculo. Como a definição de `DateArg` não foi fornecida, não é possível enumerar os formatos de entrada aceitos.
   - **`options?: EndOfISOWeekOptions<ResultDate>`**: opções opcionais de contexto, repassadas a `endOfWeek`. A interface estende `ContextOptions<ResultDate>` sem adicionar propriedades; os campos disponíveis não estão definidos no trecho.

3. **Retorno:** o resultado de `endOfWeek`, tipado como **`ResultDate`**, um tipo que estende `Date` e que, por padrão, é `DateType`. Representa o fim da semana calculado com `weekStartsOn: 1`; o horário exato retornado não pode ser confirmado sem a implementação de `endOfWeek`.

## Gabarito oficial (date-fns)

- **summary**: Return the end of an ISO week for the given date.
- **description**: Return the end of an ISO week for the given date. The result will be in the local timezone.
