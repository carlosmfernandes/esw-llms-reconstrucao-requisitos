# CT02 — getISODay (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas:

### 1. Requisito funcional
A função calcula e retorna o dia da semana de uma determinada data de acordo com o padrão ISO (no qual a semana começa na segunda-feira representada pelo número 1 e termina no domingo representado pelo número 7, ajustando o comportamento padrão do JavaScript que considera o domingo como 0).

---

### 2. Parâmetros de entrada
* **`date`** (`DateArg<Date> & {}`): A data (ou objeto/valor representando uma data) da qual se deseja extrair o dia da semana.
* **`options`** (`GetISODayOptions`, opcional): Um objeto de opções de configuração que pode conter a propriedade `in` para especificar o contexto de conversão/fuso da data ao executá-la em `toDate`.

---

### 3. Retorno
Retorna um valor numérico (`number`) entre **1 e 7**, onde:
* `1` representa Segunda-feira;
* `2` a `6` representam de Terça-feira a Sábado;
* `7` representa Domingo.

## Gabarito oficial (date-fns)

- **summary**: Get the day of the ISO week of the given date.
- **description**: Get the day of the ISO week of the given date, which is 7 for Sunday, 1 for Monday etc.
