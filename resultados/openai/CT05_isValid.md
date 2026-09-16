<!-- STATUS: OK -->
# CT05 — isValid (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** Verificar se um valor é uma data válida segundo dois critérios: ele deve ser reconhecido por `isDate` **ou** ser do tipo `number`; além disso, o resultado de `toDate`, convertido em número pelo operador `+`, não pode ser `NaN`.

2. **Parâmetro de entrada:** `date: unknown` — o valor cuja validade será verificada. O tipo `unknown` permite receber valores de qualquer tipo.

3. **Retorno:** Um `boolean`:
   - `true` se o valor satisfizer os dois critérios acima.
   - `false` se não for reconhecido por `isDate` nem for um número, ou se a conversão resultar em `NaN`.

O trecho não mostra como `isDate` e `toDate` funcionam internamente; portanto, não permite especificar detalhes adicionais sobre reconhecimento ou conversão de datas.

## Gabarito oficial (date-fns)

- **summary**: Is the given date valid?
- **description**: Returns false if argument is Invalid Date and true otherwise. Argument is converted to Date using `toDate`. See [toDate](https://date-fns.org/docs/toDate) Invalid Date is a Date, whose time value is NaN.
