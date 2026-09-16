<!-- STATUS: OK -->
# CT14 — setYear (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no trecho de código fornecido, seguem as respostas:

### 1. Requisito funcional
A função tem como objetivo alterar o ano de uma data para um ano específico fornecido. Caso a data original fornecida seja inválida, a função assegura a criação e o retorno de uma data inválida correspondente, em vez de aplicar a alteração de ano.

---

### 2. Parâmetros de entrada
* **`date` (`DateArg<DateType>`)**: A data base que terá seu ano modificado.
* **`year` (`number`)**: O valor numérico que representa o novo ano a ser aplicado à data.
* **`options` (`SetYearOptions<ResultDate> | undefined`, opcional)**: Objeto de opções adicionais (herdado de `ContextOptions`) contendo a propriedade `in`, utilizada para definir o contexto ou o construtor da data de resultado.

---

### 3. Retorno da função
* **`ResultDate`**: Retorna a instância de data com o ano atualizado. Caso a data original seja inválida, retorna uma nova instância representando uma data inválida (`NaN`).

## Gabarito oficial (date-fns)

- **summary**: Set the year to the given date.
- **description**: Set the year to the given date.
