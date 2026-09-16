<!-- STATUS: OK -->
# CT24 — eachDayOfInterval (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `eachDayOfInterval`

## 1. Requisito funcional

A função gera uma **lista de datas correspondentes a cada dia contido em um intervalo especificado**, do início ao fim (ou vice-versa, se o intervalo estiver invertido). Opcionalmente, permite pular dias com um passo (step) configurável, retornando apenas os dias correspondentes a esse intervalo de repetição (por exemplo, a cada 2 dias).

Comportamentos específicos observados:
- Se `start > end`, o intervalo é tratado como invertido, e o resultado final é retornado em ordem decrescente (do mais recente ao mais antigo).
- Se `step` for `0`, retorna um array vazio.
- Se `step` for negativo, seu valor absoluto é usado e a lógica de reversão é invertida.
- Cada data gerada tem as horas, minutos, segundos e milissegundos zerados (normalizados para o início do dia).

## 2. Parâmetros de entrada

- **`interval: IntervalType`** — objeto contendo as propriedades `start` e `end`, que definem o intervalo de datas a ser percorrido (podem ser `Date`, string ou número, conforme normalizado por `normalizeInterval`).
- **`options?: Options`** (opcional) — objeto com:
  - **`step?: number`** — de quantos em quantos dias a função deve avançar ao gerar a lista (padrão implícito: `1`).
  - **`in?: ContextOptions["in"]`** — contexto/fábrica usada para construir os objetos de data resultantes (via `normalizeInterval` e `constructFrom`), permitindo customizar o tipo de data retornado (ex.: suporte a bibliotecas de data alternativas).

## 3. Retorno

Um **array de datas** (`EachDayOfIntervalResult`), representando cada dia dentro do intervalo `[start, end]`, com step aplicado quando especificado. O tipo de cada elemento do array é inferido a partir do contexto (`options.in`) ou do tipo de `start`/`end` do intervalo original. Se `step` for `0`, o array retornado é vazio.

## Gabarito oficial (date-fns)

- **summary**: Return the array of dates within the specified time interval.
- **description**: Return the array of dates within the specified time interval.
