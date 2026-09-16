<!-- STATUS: OK -->
# CT24 — eachDayOfInterval (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, seguem as respostas:

### 1. Requisito funcional
A função tem como objetivo **gerar uma sequência de datas representando os dias contidos dentro de um intervalo delimitado**, permitindo configurar o espaçamento (passo) entre esses dias e suportando intervalos e passos progressivos ou regressivos (ordenados do início ao fim ou vice-versa).

---

### 2. Parâmetros de entrada
A função recebe dois parâmetros:

* **`interval`** (`IntervalType`): Objeto que representa o intervalo temporal a ser percorrido, contendo ao menos uma data de início (`start`) e uma data de término (`end`).
* **`options`** (`Options`, opcional): Objeto para configurações adicionais que pode conter:
  * **`step`**: O incremento/passo em dias entre uma data e a próxima na sequência gerada (o valor padrão é `1`).
  * **`in`**: Parâmetro de contexto repassado para a normalização do intervalo (`normalizeInterval`).

---

### 3. O que a função retorna
Retorna um **array de objetos de data** (`Date` ou o tipo específico de data derivado do contexto/intervalo) contendo cada dia calculado dentro do intervalo, com o horário zerado (`00:00:00.000`). 
* A ordem das datas no array respeita o sentido do intervalo e o sinal do passo (`step`).
* Caso `step` seja avaliado como `0` (falsy), a função retorna um array vazio (`[]`).

## Gabarito oficial (date-fns)

- **summary**: Return the array of dates within the specified time interval.
- **description**: Return the array of dates within the specified time interval.
