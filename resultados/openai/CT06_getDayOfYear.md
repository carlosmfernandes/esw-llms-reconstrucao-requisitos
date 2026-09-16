<!-- STATUS: OK -->
# CT06 — getDayOfYear (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** determinar a posição de uma data dentro do seu ano, em dias de calendário, considerando o primeiro dia do ano como **dia 1**. Para isso, calcula a diferença em dias de calendário entre a data e o início do mesmo ano e soma 1.

2. **Parâmetros de entrada:**
   - **`date: DateArg<Date> & {}`**: a data cuja posição no ano será calculada. É processada por `toDate` antes do cálculo. Como a definição de `DateArg` não foi fornecida, não é possível enumerar os formatos de entrada aceitos.
   - **`options?: GetDayOfYearOptions`**: opções opcionais, cujo tipo estende `ContextOptions<Date>`. O código utiliza apenas `options.in`, repassando-o a `toDate`. O significado específico dessa opção não está definido no trecho.

3. **Retorno:** um **`number`** correspondente ao dia ordinal da data no ano: a diferença em dias de calendário em relação ao início do ano, acrescida de 1. O comportamento para entradas inválidas não pode ser determinado apenas pelo trecho fornecido.

## Gabarito oficial (date-fns)

- **summary**: Get the day of the year of the given date.
- **description**: Get the day of the year of the given date.
