<!-- STATUS: OK -->
# CT20 — startOfWeek (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas para os seus questionamentos:

### 1. Requisito Funcional
A função calcula e retorna o **início da semana** para uma determinada data. Ela ajusta a data fornecida para o primeiro dia dessa semana (com base na configuração do dia em que a semana se inicia, como domingo ou segunda-feira) e redefine o horário desse dia para o início exato (00:00:00.000).

---

### 2. Parâmetros de Entrada

1. **`date`** (`DateArg<DateType>`):
   * A data de referência a partir da qual o início da semana será determinado.
2. **`options`** (`StartOfWeekOptions<ResultDate>`, opcional):
   * Um objeto opcional de configurações para personalizar o comportamento da função. Pode conter:
     * **`weekStartsOn`**: O dia em que a semana começa (um valor numérico, onde `0` representa o padrão caso não seja fornecido).
     * **`locale`**: Objeto de localização que também pode conter a opção `weekStartsOn`.
     * **`in`**: Parâmetro de contexto/conversão repassado para a função interna `toDate`.

---

### 3. Retorno da Função

* **`ResultDate`**: Retorna um novo objeto de data correspondente ao **primeiro dia da semana** em relação à data informada, com o horário zerado (horas, minutos, segundos e milissegundos ajustados para `00:00:00.000`).

## Gabarito oficial (date-fns)

- **summary**: Return the start of a week for the given date.
- **description**: Return the start of a week for the given date. The result will be in the local timezone.
