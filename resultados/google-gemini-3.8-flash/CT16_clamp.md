<!-- STATUS: OK -->
# CT16 — clamp (google/gemini-3.8-flash)

## Resposta do LLM

Com base estritamente no código fornecido, seguem as respostas:

### 1. Requisito funcional implementado
A função tem como objetivo **restringir (fazer o *clamp* de) uma data dentro de um intervalo delimitado**. Ou seja, garante que a data fornecida não seja anterior ao início nem posterior ao fim do intervalo especificado:
* Se a data for anterior ao início do intervalo, assume a data de início;
* Se a data for posterior ao fim do intervalo, assume a data de fim;
* Se a data já estiver dentro do intervalo, permanece inalterada.

---

### 2. Parâmetros de entrada
* **`date`** (`DateType`): A data alvo que deve ser avaliada e limitada dentro do intervalo.
* **`interval`** (`IntervalType`): O objeto de intervalo que define os limites temporais permitidos, contendo as propriedades `start` (limite inferior) e `end` (limite superior).
* **`options`** (`Options`, opcional): Objeto de configurações de contexto (`ClampOptions`), que inclui a propriedade `in` (usada na normalização das datas) e repassa opções de contexto para as operações de comparação (`min`/`max`).

---

### 3. O que a função retorna
Retorna a **data resultante após a restrição ao intervalo** (a data original, a data de início ou a data de fim), tipada/formatada de acordo com o contexto definido nas opções ou nos próprios tipos de entrada (`ClampResult`).

## Gabarito oficial (date-fns)

- **summary**: Return a date bounded by the start and the end of the given interval.
- **description**: Clamps a date to the lower bound with the start of the interval and the upper bound with the end of the interval.
