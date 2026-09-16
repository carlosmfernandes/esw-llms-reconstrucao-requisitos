<!-- STATUS: OK -->
# CT17 — areIntervalsOverlapping (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional
Verificar se dois intervalos de datas se sobrepõem, permitindo configurar se o contato entre suas extremidades conta como sobreposição.

A função considera o menor dos dois valores de cada intervalo como início e o maior como fim, mesmo que tenham sido fornecidos em ordem inversa.

### 2. Parâmetros de entrada
- **`intervalLeft: Interval`**: primeiro intervalo, com os campos `start` e `end` representando suas extremidades.
- **`intervalRight: Interval`**: segundo intervalo, também com `start` e `end`.
- **`options?: AreIntervalsOverlappingOptions`**: configurações opcionais:
  - **`inclusive?: boolean`**: quando verdadeiro, permite igualdade nas comparações das extremidades. Quando falso ou omitido, as comparações são estritas.
  - **`in`**: valor repassado a `toDate` na conversão de cada extremidade. Seu significado específico não pode ser determinado pelo trecho, pois as definições de `ContextOptions` e `toDate` não foram fornecidas.

### 3. Retorno
Um **`boolean`**, calculado após converter e ordenar as extremidades:

- Com `inclusive` verdadeiro: retorna `true` se **início esquerdo ≤ fim direito** e **início direito ≤ fim esquerdo**.
- Caso contrário: retorna `true` se **início esquerdo < fim direito** e **início direito < fim esquerdo**.

Retorna `false` quando a condição correspondente não é satisfeita.

## Gabarito oficial (date-fns)

- **summary**: Is the given time interval overlapping with another time interval?
- **description**: Is the given time interval overlapping with another time interval? Adjacent intervals do not count as overlapping unless `inclusive` is set to `true`.
