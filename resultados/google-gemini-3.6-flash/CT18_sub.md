<!-- STATUS: OK -->
# CT18 — sub (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas para as três perguntas:

---

### 1. Requisito Funcional
A função implementa a **subtração de uma duração específica em relação a uma data de referência**. Do ponto de vista de especificação, ela permite que o usuário passe uma data e defina um período a ser removido (combinando anos, meses, semanas, dias, horas, minutos e segundos), retornando a nova data calculada após essa regressão temporal.

---

### 2. Parâmetros de Entrada

1. **`date`** (`DateArg<DateType>`): A data base/inicial a partir da qual a duração será subtraída.
2. **`duration`** (`Duration`): Objeto que especifica a quantidade de tempo a ser subtraída. Pode conter os campos `years`, `months`, `weeks`, `days`, `hours`, `minutes` e `seconds` (todos opcionais, assumindo valor `0` por padrão caso não informados).
3. **`options`** (`SubOptions<ResultDate>`, *opcional*): Objeto de configurações adicionais de contexto (como a opção `in`, utilizada para determinar a referência de contexto na construção da data final).

---

### 3. Retorno
A função retorna um **novo objeto de data** (do tipo `ResultDate`) representando o momento exato resultante da subtração de toda a duração informada a partir da data de origem.

## Gabarito oficial (date-fns)

- **summary**: Subtract the specified years, months, weeks, days, hours, minutes and seconds from the given date.
- **description**: Subtract the specified years, months, weeks, days, hours, minutes and seconds from the given date.
