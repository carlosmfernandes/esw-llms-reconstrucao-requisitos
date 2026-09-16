<!-- STATUS: OK -->
# CT11 — isSameWeek (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** verificar se duas datas pertencem à mesma semana, considerando as opções fornecidas. A função determina isso comparando os valores numéricos do início da semana de cada data, após normalizá-las.

2. **Parâmetros de entrada:**
   - **`laterDate`**: uma das datas a comparar, com tipo `DateArg<Date> & {}`.
   - **`earlierDate`**: a outra data a comparar, com o mesmo tipo. Apesar dos nomes, o código não exige nem verifica que a primeira seja posterior à segunda.
   - **`options`** *(opcional)*: opções dos tipos `WeekOptions`, `LocalizedOptions<"options">` e `ContextOptions<Date>`. O campo `in` é passado à normalização das datas, e o objeto completo é passado ao cálculo do início da semana. O trecho não mostra os demais campos, seus comportamentos nem seus valores padrão.

3. **Retorno:** um **`boolean`**: `true` se os inícios de semana calculados tiverem o mesmo valor numérico; `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Are the given dates in the same week (and month and year)?
- **description**: Are the given dates in the same week (and month and year)?
