<!-- STATUS: OK -->
# CT29 — addBusinessDays (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, seguem as respostas:

### 1. Requisito funcional
A função tem como objetivo **adicionar ou subtrair uma quantidade determinada de dias úteis a uma data base**, ignorando os dias de fim de semana (sábado e domingo). Se o valor a ser adicionado for negativo, ela subtrai dias úteis; se a contagem iniciar em um fim de semana, ela faz os ajustes necessários para que o resultado caia em um dia útil apropriado, preservando o horário original da data.

---

### 2. Parâmetros de entrada
* **`date`** (`DateArg<DateType>`): A data inicial de referência a partir da qual os dias úteis serão adicionados ou subtraídos.
* **`amount`** (`number`): A quantidade de dias úteis a ser somada (se positivo) ou subtraída (se negativo).
* **`options`** (`AddBusinessDaysOptions<ResultDate> | undefined`, opcional): Objeto de configurações de contexto (como a propriedade `in`, utilizada internamente para construção/conversão da data e propagada para funções auxiliares).

---

### 3. O que a função retorna
* Retorna uma **instância de data (`ResultDate`)** representando a nova data resultante após o acréscimo ou decréscimo dos dias úteis, mantendo a hora original. Caso o parâmetro `amount` seja `NaN` (não seja um número válido), a função retorna uma data inválida (`NaN`).

## Gabarito oficial (date-fns)

- **summary**: Add the specified number of business days (mon - fri) to the given date.
- **description**: Add the specified number of business days (mon - fri) to the given date, ignoring weekends.
