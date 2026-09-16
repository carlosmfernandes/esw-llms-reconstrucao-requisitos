<!-- STATUS: OK -->
# CT22 — add (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

### 1. Requisito funcional
A função implementa a operação de **adicionar uma duração de tempo especificada a uma data base**, permitindo somar diferentes unidades temporais (anos, meses, semanas, dias, horas, minutos e segundos) a essa data e, opcionalmente, considerar um contexto específico de data para a operação e instanciação do resultado.

---

### 2. Parâmetros de entrada

* **`date` (`DateArg<DateType>`)**: A data inicial/base à qual o período de tempo será adicionado.
* **`duration` (`Duration`)**: Objeto que define a quantidade de tempo a ser somada, composto pelas propriedades (todas assumindo `0` se ausentes):
  * `years` (anos)
  * `months` (meses)
  * `weeks` (semanas)
  * `days` (dias)
  * `hours` (horas)
  * `minutes` (minutos)
  * `seconds` (segundos)
* **`options` (`AddOptions<ResultDate> | undefined`, opcional)**: Objeto de opções de contexto que contém a propriedade `in`, usada para determinar o contexto temporal/construtor de referência tanto para a conversão inicial da data quanto para a construção da data final.

---

### 3. Retorno da função
Retorna uma **nova data (`ResultDate`)** correspondente à data original acrescida do tempo especificado na duração, construída com base no contexto definido em `options.in` (se fornecido) ou na própria data original (`date`).

## Gabarito oficial (date-fns)

- **summary**: Add the specified years, months, weeks, days, hours, minutes, and seconds to the given date.
- **description**: Add the specified years, months, weeks, days, hours, minutes, and seconds to the given date.
