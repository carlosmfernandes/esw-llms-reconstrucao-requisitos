<!-- STATUS: OK -->
# CT07 — getQuarter (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional:** determinar o trimestre do ano ao qual pertence a data informada, agrupando os meses em quatro períodos:
   - Janeiro a março: **1**
   - Abril a junho: **2**
   - Julho a setembro: **3**
   - Outubro a dezembro: **4**

2. **Parâmetros de entrada:**
   - `date: DateArg<Date> & {}`: a data cujo trimestre será calculado. Ela é passada a `toDate` antes do cálculo. Como a definição de `DateArg` não foi fornecida, o trecho não permite enumerar todos os formatos de entrada aceitos.
   - `options?: GetQuarterOptions`: opções opcionais. A propriedade `options?.in` é repassada a `toDate`; seu significado específico não pode ser determinado sem as definições correspondentes.

3. **Retorno:** um `number` que representa o trimestre, de **1 a 4** para uma data válida. Se a conversão resultar em uma data cujo `getMonth()` devolva `NaN`, o resultado também será `NaN`.

## Gabarito oficial (date-fns)

- **summary**: Get the year quarter of the given date.
- **description**: Get the year quarter of the given date.
