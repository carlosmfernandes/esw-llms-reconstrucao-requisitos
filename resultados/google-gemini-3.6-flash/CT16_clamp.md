# CT16 — clamp (google/gemini-3.6-flash)

## Resposta do LLM

Com base no código-fonte fornecido, seguem as respostas:

---

### 1. Requisito funcional
A função limita (ou ajusta) uma determinada data para que ela permaneça dentro de um intervalo delimitado por uma data inicial e uma data final. 

* Se a data informada for **anterior** ao início do intervalo, a função retorna a data de início do intervalo.
* Se a data informada for **posterior** ao fim do intervalo, a função retorna a data de término do intervalo.
* Se a data informada estiver **dentro** do intervalo, a função retorna a própria data informada.

---

### 2. Parâmetros de entrada

* **`date`** (`DateType`): A data que se deseja delimitar/ajustar dentro do intervalo.
* **`interval`** (`IntervalType`): Um objeto que define o intervalo permitido, contendo as propriedades:
  * `start`: a data limite inferior (início).
  * `end`: a data limite superior (fim).
* **`options`** (`Options`, opcional): Objeto opcional de configurações/contexto que pode conter a opção `in` (usada para normalizar as datas e o contexto/fuso das instâncias) e repassada às operações internas de comparação.

---

### 3. O que a função retorna

Retorna um objeto de data (no tipo inferido por `ClampResult`, geralmente uma instância de `Date` ou tipo equivalente fornecido) representando a data final após o ajuste, garantindo que ela esteja dentro dos limites do intervalo (`start` <= *retorno* <= `end`).

## Gabarito oficial (date-fns)

- **summary**: Return a date bounded by the start and the end of the given interval.
- **description**: Clamps a date to the lower bound with the start of the interval and the upper bound with the end of the interval.
