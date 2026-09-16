<!-- STATUS: OK -->
# CT03 — isWeekend (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** Verificar se a data informada cai em um fim de semana, considerando **domingo e sábado** como dias de fim de semana (`getDay()` igual a `0` ou `6`).

2. **Parâmetros de entrada:**
   - **`date: DateArg<Date> & {}`**: valor que representa a data a verificar, passado a `toDate` para conversão. O trecho não define `DateArg`, portanto não permite enumerar os formatos de entrada aceitos.
   - **`options?: IsWeekendOptions`**: opções opcionais que estendem `ContextOptions<Date>`. Apenas a propriedade `in` é utilizada, sendo repassada a `toDate`. Seu significado específico não está definido no trecho.

3. **Retorno:** Um **`boolean`**: `true` se o dia da semana da data convertida for domingo ou sábado; `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Does the given date fall on a weekend?
- **description**: Does the given date fall on a weekend? A weekend is either Saturday (`6`) or Sunday (`0`).
