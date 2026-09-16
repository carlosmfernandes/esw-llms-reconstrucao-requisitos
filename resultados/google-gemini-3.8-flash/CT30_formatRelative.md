<!-- STATUS: OK -->
# CT30 — formatRelative (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, seguem as respostas:

### 1. Requisito funcional implementado
A função tem como objetivo **formatar uma data de maneira relativa em relação a uma data de referência** (expressando textualmente noções como "hoje", "ontem", "amanhã", "semana passada", "próxima semana" ou outra data), aplicando regras de localização/idioma (*locale*) com base na diferença de dias de calendário entre elas.

---

### 2. Parâmetros de entrada
* **`date`** (`DateArg<Date> & {}`): A data-alvo que se deseja formatar.
* **`baseDate`** (`DateArg<Date> & {}`): A data base/de referência contra a qual a data-alvo será comparada.
* **`options`** (`FormatRelativeOptions`, opcional): Objeto de opções para customizar a operação, que pode conter:
  * `locale`: As definições de internacionalização/idioma a serem usadas na resolução do texto e formato relativo.
  * `weekStartsOn`: O dia que determina o início da semana.
  * `in`: Contexto para a normalização das datas fornecidas.

---

### 3. O que a função retorna
* Retorna uma **`string`** contendo a data formatada de acordo com a relação temporal relativa determinada (ou lança uma exceção `RangeError: "Invalid time value"` caso o cálculo de diferença entre as datas resulte em um valor inválido / `NaN`).

## Gabarito oficial (date-fns)

- **summary**: Represent the date in words relative to the given base date.
- **description**: Represent the date in words relative to the given base date.
