<!-- STATUS: OK -->
# CT10 — endOfISOWeek (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui está a análise:

---

### 1. Requisito Funcional
A função calcula e retorna a data correspondente ao **fim da semana no padrão ISO** para uma determinada data informada. O requisito garante que o cálculo considere explicitamente a segunda-feira como o primeiro dia da semana (`weekStartsOn: 1`), que é a regra do calendário ISO (fazendo com que a semana encerre no domingo).

---

### 2. Parâmetros de Entrada

* **`date`** (`DateArg<DateType>`): A data de referência sobre a qual será calculado o final da semana ISO.
* **`options`** (`EndOfISOWeekOptions<ResultDate>`, opcional): Objeto contendo opções de configuração adicionais (herdadas de `ContextOptions`), como contexto de execução ou fuso horário, para personalizar o cálculo efetuado pela função subjacente.

---

### 3. Retorno

* Retorna uma nova data (do tipo `ResultDate`) representando o momento correspondente ao final da semana ISO associada à data informada.

## Gabarito oficial (date-fns)

- **summary**: Return the end of an ISO week for the given date.
- **description**: Return the end of an ISO week for the given date. The result will be in the local timezone.
