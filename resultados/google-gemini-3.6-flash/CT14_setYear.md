# CT14 — setYear (google/gemini-3.6-flash)

## Resposta do LLM

Com base na análise do código-fonte fornecido, seguem as respostas aos três pontos solicitados:

### 1. Requisito funcional que a função implementa
A função tem como requisito alterar (definir) o ano de uma data fornecida para um valor especificado. Ela garante que a operação respeite o contexto especificado pelas opções de entrada e lide com dados corrompidos/inválidos, retornando uma data inválida caso a data de entrada original não seja válida.

---

### 2. Parâmetros de entrada
* **`date`** (`DateArg<DateType>`): A data original à qual se deseja aplicar a alteração do ano.
* **`year`** (`number`): O valor numérico correspondente ao novo ano que será atribuído à data.
* **`options`** (`SetYearOptions<ResultDate> | undefined`, opcional): Objeto opcional para configurações adicionais de contexto (que pode incluir a propriedade `in` para indicar o contexto ou formato da data de saída/conversão).

---

### 3. O que a função retorna
A função retorna um objeto de data (`ResultDate`) contendo o ano atualizado com o valor informado no parâmetro `year`. Caso a data fornecida na entrada seja inválida, a função retorna uma representação de data inválida (construída via `constructFrom` com o valor `NaN`).

## Gabarito oficial (date-fns)

- **summary**: Set the year to the given date.
- **description**: Set the year to the given date.
