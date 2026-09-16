<!-- STATUS: OK -->
# CT13 — compareAsc (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** comparar duas datas em ordem cronológica crescente, indicando se a primeira é anterior, posterior ou igual à segunda.

2. **Parâmetros de entrada:**
   - `dateLeft`: primeira data da comparação.
   - `dateRight`: segunda data da comparação.

   Ambos têm o tipo declarado `DateArg<Date> & {}` e são convertidos por `toDate` antes da comparação. O trecho não mostra a definição de `DateArg` nem a implementação de `toDate`, portanto não permite enumerar os formatos de entrada aceitos.

3. **Retorno:** um `number`:
   - `-1` se a primeira data for anterior à segunda;
   - `1` se a primeira data for posterior à segunda;
   - `0` se seus valores numéricos forem iguais;
   - `NaN` se a subtração dos valores numéricos obtidos resultar em `NaN`.

## Gabarito oficial (date-fns)

- **summary**: Compare the two dates and return -1, 0 or 1.
- **description**: Compare the two dates and return 1 if the first date is after the second, -1 if the first date is before the second or 0 if dates are equal.
