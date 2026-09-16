<!-- STATUS: OK -->
# CT05 — isValid (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

1. **Requisito funcional:**  
   Verificar e validar se um determinado valor fornecido é uma data válida (aceitando especificamente instâncias de data ou números que correspondam a um valor temporal válido, ou seja, cujo valor numérico correspondente não seja `NaN`).

2. **Parâmetros de entrada:**  
   * `date` (tipo `unknown`): O valor arbitrário que se deseja testar para determinar se representa uma data válida.

3. **Retorno da função:**  
   Retorna um valor booleano (`boolean`):  
   * `true`: caso o valor seja uma data válida (objeto de data ou número que resulte em um timestamp numérico válido).  
   * `false`: caso o valor não seja uma data/número ou resulte em uma data inválida (`NaN`).

## Gabarito oficial (date-fns)

- **summary**: Is the given date valid?
- **description**: Returns false if argument is Invalid Date and true otherwise. Argument is converted to Date using `toDate`. See [toDate](https://date-fns.org/docs/toDate) Invalid Date is a Date, whose time value is NaN.
