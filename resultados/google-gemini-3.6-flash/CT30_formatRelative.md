<!-- STATUS: OK -->
# CT30 — formatRelative (google/gemini-3.6-flash)

## Resposta do LLM

Com base na análise exclusiva do código fornecido:

---

### 1. Requisito Funcional
A função implementa a **formatação de uma data em formato relativo a uma data de referência**. 

Em vez de exibir apenas uma data estática (ex: "10/05/2023"), ela calcula a diferença em dias entre a data informada e uma data base, categorizando a relação temporal (como *"hoje"*, *"ontem"*, *"amanhã"*, *"semana passada"*, *"próxima semana"* ou *"outro"*) e gerando uma representação textual formatada de acordo com o idioma/localização (*locale*) e regras configuradas (como o dia em que a semana se inicia).

---

### 2. Parâmetros de Entrada

* **`date`** (`DateArg<Date> & {}`): A data principal que se deseja formatar.
* **`baseDate`** (`DateArg<Date> & {}`): A data de referência a partir da qual a comparação de dias será feita para determinar a relação relativa (ex.: se a `date` é "hoje" ou "ontem" em relação a esta `baseDate`).
* **`options`** (`FormatRelativeOptions`, opcional): Objeto contendo configurações para customizar a execução, incluindo:
  * `locale`: As definições de localização/idioma a serem usadas para gerar os tokens textuais e formatar o resultado final.
  * `weekStartsOn`: O dia da semana que deve ser considerado o primeiro dia da semana.
  * `in`: Parâmetro utilizado na normalização do contexto das datas.

---

### 3. Retorno

* **Retorno normal:** Retorna uma **`string`** contendo a data formatada de forma relativa ao contexto temporal e conforme as regras do idioma configurado.
* **Exceção:** Lança um erro do tipo **`RangeError("Invalid time value")`** caso a diferença calculada entre as datas seja um valor numérico inválido (`NaN`).

## Gabarito oficial (date-fns)

- **summary**: Represent the date in words relative to the given base date.
- **description**: Represent the date in words relative to the given base date.
