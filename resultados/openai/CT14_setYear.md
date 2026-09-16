<!-- STATUS: OK -->
# CT14 — setYear (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional**  
   Alterar o ano de uma data para o ano informado, usando as regras de `Date.prototype.setFullYear`. Os demais componentes da data são mantidos, sujeitos aos ajustes dessa operação para datas que não existam no novo ano. Se a data convertida for inválida, a função retorna uma data inválida, sem tentar alterar seu ano.

2. **Parâmetros de entrada**
   - **`date: DateArg<DateType>`**: data de referência cujo ano será alterado. Ela é convertida por `toDate`. Os formatos aceitos por `DateArg` não estão definidos no trecho.
   - **`year: number`**: ano a ser atribuído à data.
   - **`options?: SetYearOptions<ResultDate>`**: opções opcionais de contexto. A propriedade `in`, quando fornecida, é passada a `toDate` e também pode ser usada para construir o resultado inválido. Sua definição e seu funcionamento completo não aparecem no código.

3. **Retorno**  
   Um objeto de data tipado como **`ResultDate`**, com o ano alterado. Se `toDate` produzir uma data inválida, retorna um objeto de data inválida construído por `constructFrom`.

## Gabarito oficial (date-fns)

- **summary**: Set the year to the given date.
- **description**: Set the year to the given date.
