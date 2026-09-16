<!-- STATUS: OK -->
# CT28 — eachWeekOfInterval (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas:

---

### 1. Qual é o requisito funcional que esta função implementa?
A função gera uma lista (array) contendo as datas correspondentes ao **início de cada semana** compreendida dentro de um determinado intervalo de datas. 

Do ponto de vista funcional, ela permite:
- Obter todas as semanas de um período com um intervalo de avanço customizável (passo/step de semanas).
- Lidar com intervalos em ordem cronológica direta ou inversa (quando o início é posterior ao fim ou o passo é negativo), retornando as datas na direção temporal apropriada.

---

### 2. Quais são os parâmetros de entrada e o que cada um representa?

1. **`interval`** (`IntervalType extends Interval`):
   - Representa o intervalo de datas a ser avaliado. Possui internamente as propriedades de início (`start`) e fim (`end`).
2. **`options`** (`Options extends EachWeekOfIntervalOptions | undefined`, opcional):
   - Objeto de configurações adicionais para o cálculo, que inclui:
     - **`step`**: Define o incremento de semanas a cada iteração (padrão é 1; se negativo inverte a ordem; se igual a 0 retorna vazio).
     - **`in`**: Parâmetro de contexto utilizado para normalizar o intervalo.
     - Opções herdadas de semana e localização (`WeekOptions`, `LocalizedOptions`), repassadas para a função `startOfWeek` para determinar regras sobre o início da semana.

---

### 3. O que a função retorna?
Retorna um **array de objetos de data** (do tipo `Date` padrão ou do tipo customizado determinado pelas opções/intervalo). Cada item do array corresponde à data de início de uma semana dentro do intervalo, ajustada para a hora inicial (00:00). 
- Caso `step` seja avaliado como `0` (falso), retorna um array vazio (`[]`).
- Se o intervalo for decrescente ou o `step` for negativo, o array é retornado em ordem invertida.

## Gabarito oficial (date-fns)

- **summary**: Return the array of weeks within the specified time interval.
- **description**: Return the array of weeks within the specified time interval.
