# CT06 — getDayOfYear (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código-fonte fornecido, aqui estão as respostas:

### 1. Requisito Funcional
A função calcula e retorna o dia do ano (o número ordinal do dia no ano, variando de 1 a 365/366) para uma determinada data informada.

### 2. Parâmetros de Entrada
* **`date`**: A data (ou representação de data aceita) a partir da qual o dia do ano será calculado.
* **`options`** *(opcional)*: Objeto de opções de contexto (que permite passar a propriedade `in` para especificar o contexto/fuso horário no qual a data deve ser avaliada).

### 3. O que a função retorna
* Retorna um número inteiro (`number`) representando a posição do dia dentro do ano da data fornecida (onde o primeiro dia do ano, 1º de janeiro, corresponde ao valor `1`).

## Gabarito oficial (date-fns)

- **summary**: Get the day of the year of the given date.
- **description**: Get the day of the year of the given date.
