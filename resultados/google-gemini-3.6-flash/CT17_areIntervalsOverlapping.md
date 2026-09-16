<!-- STATUS: OK -->
# CT17 — areIntervalsOverlapping (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas:

### 1. Requisito Funcional
A função verifica se dois intervalos de tempo se sobrepõem (possuem interseção). Ela permite determinar se o limite exato onde um intervalo termina e outro começa deve ser considerado como uma sobreposição (modo inclusivo) ou não (modo exclusivo/padrão).

---

### 2. Parâmetros de Entrada
A função aceita três parâmetros:

1. **`intervalLeft`** (`Interval`): O primeiro intervalo de tempo a ser comparado (objeto que possui as propriedades `start` e `end`).
2. **`intervalRight`** (`Interval`): O segundo intervalo de tempo a ser comparado com o primeiro.
3. **`options`** (`AreIntervalsOverlappingOptions`, opcional): Objeto para configurações adicionais que pode conter:
   * `inclusive` (booleano opcional): Se `true`, define que intervalos que apenas se tocam nas extremidades (ex: o fim de um é exatamente o início do outro) são considerados sobrepostos.
   * `in` (herdado de `ContextOptions<Date>`): Opção de contexto repassada para a conversão interna das datas (`toDate`).

---

### 3. Retorno da Função
Retorna um **valor booleano** (`boolean`):
* **`true`**: Se os dois intervalos se sobrepõem.
* **`false`**: Se os intervalos não se sobrepõem.

## Gabarito oficial (date-fns)

- **summary**: Is the given time interval overlapping with another time interval?
- **description**: Is the given time interval overlapping with another time interval? Adjacent intervals do not count as overlapping unless `inclusive` is set to `true`.
