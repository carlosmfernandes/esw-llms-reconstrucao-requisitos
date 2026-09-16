<!-- STATUS: OK -->
# CT17 — areIntervalsOverlapping (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise do código

## 1. Requisito funcional

A função implementa a verificação de **sobreposição (overlap) entre dois intervalos de tempo/datas**. Ou seja, dado dois intervalos (cada um definido por uma data de início e uma data de fim), a função determina se eles se cruzam em algum ponto no tempo.

O comportamento contempla duas variações:
- **Modo exclusivo (padrão)**: os intervalos se sobrepõem apenas se houver uma interseção estrita (não basta que um termine exatamente quando o outro começa).
- **Modo inclusivo** (via opção `inclusive: true`): os intervalos são considerados sobrepostos mesmo que se toquem apenas nas extremidades (início de um coincide com o fim do outro).

Além disso, a função é tolerante quanto à ordem em que `start` e `end` são fornecidos em cada intervalo — ela normaliza os valores (ordenando-os) antes de comparar, então não assume que `start` seja necessariamente anterior a `end`.

## 2. Parâmetros de entrada

- **`intervalLeft: Interval`** — o primeiro intervalo a ser comparado, contendo propriedades `start` e `end` (valores que podem ser convertidos em datas via `toDate`).
- **`intervalRight: Interval`** — o segundo intervalo a ser comparado, com a mesma estrutura (`start` e `end`).
- **`options?: AreIntervalsOverlappingOptions`** — objeto opcional de configuração, contendo:
  - **`inclusive?: boolean`** — indica se os limites dos intervalos (extremidades coincidentes) devem ser considerados como sobreposição.
  - Propriedades herdadas de `ContextOptions<Date>` (como `in`), usadas para especificar um contexto/fuso ou construtor de data a ser usado na conversão via `toDate`.

## 3. Retorno

A função retorna um **`boolean`**:
- `true` se os dois intervalos se sobrepõem (de acordo com o critério inclusivo ou exclusivo definido);
- `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Is the given time interval overlapping with another time interval?
- **description**: Is the given time interval overlapping with another time interval? Adjacent intervals do not count as overlapping unless `inclusive` is set to `true`.
