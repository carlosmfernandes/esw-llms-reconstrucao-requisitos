<!-- STATUS: OK -->
# CT28 — eachWeekOfInterval (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas para cada uma das perguntas:

---

### 1. Requisito funcional
A função gera uma **lista (array) contendo as datas de início de cada semana** contidas dentro de um determinado intervalo de tempo (entre uma data inicial e uma data final). 

Do ponto de vista funcional, ela permite:
* Iterar sobre as semanas de um intervalo com um incremento customizado (ex.: a cada 1 semana, 2 semanas, etc.).
* Lidar com intervalos inversos (data inicial posterior à final) ou passos negativos, retornando as datas na ordem cronológica correspondente.
* Considerar regras de início de semana e fuso horário/contexto configuráveis pelo usuário.

---

### 2. Parâmetros de entrada

A função aceita dois parâmetros:

1. **`interval`** (obrigatório, do tipo `IntervalType`):
   * Objeto que representa o intervalo de tempo desejado, contendo as propriedades de data de início (`start`) e data de fim (`end`).

2. **`options`** (opcional, do tipo `EachWeekOfIntervalOptions`):
   * Objeto de opções para customizar o comportamento da função, podendo incluir:
     * **`step`**: O intervalo de semanas a ser pulado a cada passo (o valor padrão é 1).
     * **`in`**: Opção de contexto/fuso para normalização do intervalo.
     * **Opções de semana/localização** (herdadas de `WeekOptions` e `LocalizedOptions`): Parâmetros para definir como o "início da semana" é calculado (ex.: qual dia da semana inicia a contagem).

---

### 3. Retorno da função

A função retorna um **array de objetos de data** (`EachWeekOfIntervalResult`), onde cada elemento representa o início de uma semana no intervalo processado.

* **Caso especial:** Retorna um array vazio (`[]`) se o parâmetro `step` for igual a `0`.
* **Ordenação:** Se o intervalo for decrescente (início maior que o fim) ou o `step` for negativo, a lista de datas é retornada em ordem invertida.

## Gabarito oficial (date-fns)

- **summary**: Return the array of weeks within the specified time interval.
- **description**: Return the array of weeks within the specified time interval.
