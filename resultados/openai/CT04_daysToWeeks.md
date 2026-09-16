<!-- STATUS: OK -->
# CT04 — daysToWeeks (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** Converter uma quantidade de dias em semanas, dividindo-a pela constante `daysInWeek` e descartando a parte fracionária do resultado (truncamento em direção a zero). A função também garante que um resultado zero não seja retornado como `-0`.

2. **Parâmetro de entrada:**
   - `days: number`: quantidade de dias a converter.

   A constante `daysInWeek` é importada, não é um parâmetro. Seu valor não aparece no trecho fornecido.

3. **Retorno:** Um `number` correspondente ao resultado truncado de `days / daysInWeek`, com qualquer resultado zero normalizado para `0`.

## Gabarito oficial (date-fns)

- **summary**: Convert days to weeks.
- **description**: Convert a number of days to a full number of weeks.
