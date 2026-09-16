<!-- STATUS: OK -->
# CT22 — add (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

1. **Requisito Funcional:**
   A função calcula e gera uma nova data resultante da adição de uma duração especificada (composta por anos, meses, semanas, dias, horas, minutos e segundos) a uma data base inicial.

2. **Parâmetros de Entrada:**
   * **`date`**: A data base (ou argumento conversível para data) a partir da qual a duração será somada.
   * **`duration`**: Um objeto contendo as unidades de tempo a serem adicionadas (`years`, `months`, `weeks`, `days`, `hours`, `minutes` e `seconds`). Caso alguma unidade não seja informada, seu valor padrão é `0`.
   * **`options`** *(opcional)*: Um objeto de configuração de contexto que pode conter a propriedade `in`, usada para determinar o contexto de conversão da data inicial e de criação da data resultante.

3. **Retorno:**
   * Retorna um novo objeto de data (`ResultDate`) representando o momento final exato após a aplicação de todos os incrementos de tempo especificados na duração sobre a data inicial.

## Gabarito oficial (date-fns)

- **summary**: Add the specified years, months, weeks, days, hours, minutes, and seconds to the given date.
- **description**: Add the specified years, months, weeks, days, hours, minutes, and seconds to the given date.
