<!-- STATUS: OK -->
# CT24 — eachDayOfInterval (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional

Gerar uma lista de datas que representa os dias de um intervalo, com um espaçamento configurável em dias.

- A geração começa no **dia do extremo cronologicamente menor**, com o horário ajustado para **00:00:00.000**.
- Avança pelo passo configurado enquanto a data gerada não ultrapassar o extremo maior. O dia desse extremo é incluído se for alcançado pelo passo.
- Com passo positivo, a lista é crescente quando `start ≤ end` e decrescente quando `start > end`.
- Um passo negativo inverte essa ordem de saída, usando seu valor absoluto para gerar as datas.
- Se o passo for `0` ou `NaN`, retorna uma lista vazia.

Assim, o resultado representa **dias do calendário**, não necessariamente instantes contidos no intervalo original: a meia-noite do primeiro dia pode anteceder o horário informado nesse extremo.

### 2. Parâmetros de entrada

- **`interval`**: intervalo com os extremos **`start`** e **`end`**. Ambos são processados por `normalizeInterval` antes da geração das datas. A definição completa dos tipos de entrada aceitos não aparece no trecho.
- **`options`** *(opcional)*:
  - **`step`**: passo usado para avançar entre os dias. O padrão é `1` quando ausente ou nulo. Seu sinal também controla a inversão da ordem da lista.
  - **`in`**: contexto passado para `normalizeInterval`. Seu comportamento específico não pode ser determinado sem o código dessa função e a definição de `ContextOptions`.

### 3. Retorno

Um **array de objetos de data**, todos ajustados para **00:00:00.000**, com os dias selecionados e na ordem descrita acima. Cada elemento é criado por `constructFrom(start, date)`.

O tipo declarado dos elementos é escolhido, nesta prioridade:
1. Tipo de data indicado pelas opções;
2. Tipo de `interval.start`, se ele estender `Date`;
3. Tipo de `interval.end`, se ele estender `Date`;
4. `Date`.

## Gabarito oficial (date-fns)

- **summary**: Return the array of dates within the specified time interval.
- **description**: Return the array of dates within the specified time interval.
