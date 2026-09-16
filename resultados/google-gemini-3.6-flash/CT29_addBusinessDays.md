<!-- STATUS: OK -->
# CT29 — addBusinessDays (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas para os três pontos solicitados:

### 1. Requisito Funcional
A função implementa a **adição ou subtração de uma quantidade especificada de dias úteis a uma determinada data**, desconsiderando os dias de fim de semana (sábados e domingos). 

Do ponto de vista de especificação:
* Se o valor a ser adicionado for positivo, ela avança a data no tempo apenas contabilizando os dias úteis.
* Se for negativo, ela recua a data apenas contabilizando os dias úteis.
* Se a data inicial for em um fim de semana ou o resultado incidir em um, a função ajusta o resultado final para garantir que caia em um dia útil apropriado.
* O horário (horas) da data original é preservado no resultado final para evitar distorções de fusos horários/horário de verão.

---

### 2. Parâmetros de Entrada

1. **`date`** (`DateArg<DateType>`): A data inicial a partir da qual o cálculo dos dias úteis será realizado.
2. **`amount`** (`number`): O número de dias úteis a serem adicionados (se o valor for positivo) ou subtraídos (se o valor for negativo).
3. **`options`** (`AddBusinessDaysOptions<ResultDate> | undefined`, opcional): Objeto opcional contendo configurações adicionais de contexto (como a propriedade `in` para definir o contexto da data) e opções repassadas para as validações de fim de semana.

---

### 3. O que a função retorna

Retorna um objeto de data (do tipo `ResultDate`) representando a **nova data calculada após a adição ou subtração dos dias úteis**. 

*Caso o parâmetro `amount` não seja um número válido (`NaN`), a função retorna um objeto de data representando uma data inválida (`NaN`).*

## Gabarito oficial (date-fns)

- **summary**: Add the specified number of business days (mon - fri) to the given date.
- **description**: Add the specified number of business days (mon - fri) to the given date, ignoring weekends.
