<!-- STATUS: OK -->
# CT01 — isLeapYear (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** verificar se o ano da data fornecida é bissexto. A regra aplicada considera bissexto o ano divisível por 400 ou divisível por 4, desde que não seja divisível por 100.

2. **Parâmetros de entrada:**
   - **`date`** (obrigatório), do tipo `DateArg<Date> & {}`: representa a data cujo ano será verificado. É convertido por `toDate`, e o ano é obtido com `getFullYear()`. O trecho não apresenta a definição de `DateArg`, portanto não permite enumerar os formatos de entrada aceitos.
   - **`options`** (opcional), do tipo `IsLeapYearOptions`: opções de contexto. Sua propriedade `in`, quando disponível, é repassada a `toDate`. O código fornecido não detalha o significado dessa propriedade.

3. **Retorno:** um `boolean`: `true` se o ano obtido satisfizer a regra de ano bissexto; `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Is the given date in the leap year?
- **description**: Is the given date in the leap year?
