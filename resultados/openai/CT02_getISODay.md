<!-- STATUS: OK -->
# CT02 — getISODay (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** obter o dia da semana de uma data com numeração ISO: **segunda-feira = 1, …, domingo = 7**. A função usa `getDay()` da data convertida e ajusta o domingo de `0` para `7`.

2. **Parâmetros de entrada:**
   - **`date: DateArg<Date> & {}`** — valor que representa a data a consultar, convertido por `toDate`. Como a definição de `DateArg` não foi fornecida, não é possível enumerar os formatos aceitos.
   - **`options?: GetISODayOptions`** — opções facultativas de contexto. A propriedade `options.in`, quando presente, é repassada a `toDate`. Seu comportamento específico não está definido no trecho.

3. **Retorno:** um **`number`** correspondente ao dia da semana, de **1 a 7 para uma data válida**. O trecho não implementa validação nem tratamento explícito de datas inválidas.

## Gabarito oficial (date-fns)

- **summary**: Get the day of the ISO week of the given date.
- **description**: Get the day of the ISO week of the given date, which is 7 for Sunday, 1 for Monday etc.
