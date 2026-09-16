<!-- STATUS: OK -->
# CT28 — eachWeekOfInterval (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional

**Listar datas que representam o início das semanas abrangidas por um intervalo**, com um espaçamento configurável em semanas.

- A geração começa na semana que contém o limite cronologicamente menor e pode incluir a semana do limite maior, se o passo chegar até ela.
- Como as datas representam inícios de semana, a primeira pode ser anterior ao limite inicial do intervalo.
- Se `interval.start > interval.end`, a lista é devolvida em ordem decrescente.
- Um passo negativo inverte a ordem de saída; seu módulo é usado como espaçamento.
- Um passo igual a zero produz uma lista vazia.

### 2. Parâmetros de entrada

- **`interval`**: intervalo com os campos `start` e `end`, que representam seus dois limites. Ambos são processados por `normalizeInterval` antes da geração.

- **`options`** *(opcional)*:
  - **`step`**: espaçamento entre as datas geradas, em semanas. O padrão é `1` quando ausente ou `null`.
  - **`in`**: contexto passado a `normalizeInterval`. Seu funcionamento específico não está definido no trecho.
  - **Configurações de semana e localização**: previstas pelos tipos `WeekOptions` e `LocalizedOptions<"options">` e repassadas a `startOfWeek`. O trecho não mostra seus campos nem permite determinar qual dia inicia a semana por padrão.

### 3. Retorno

Um **array de objetos de data**, representando os inícios das semanas selecionadas, na ordem determinada pelo intervalo e pelo sinal do passo. Antes de inserir cada data, o código ajusta seu campo de horas para `0`.

Na tipagem declarada, o tipo dos elementos é escolhido nesta prioridade:

1. Tipo de data associado às opções, quando aplicável;
2. Tipo de `interval.start`, se ele estender `Date`;
3. Tipo de `interval.end`, se ele estender `Date`;
4. `Date`, nos demais casos.

Em execução, cada elemento é criado por `constructFrom(start, currentDate)`, usando o `start` normalizado como referência.

## Gabarito oficial (date-fns)

- **summary**: Return the array of weeks within the specified time interval.
- **description**: Return the array of weeks within the specified time interval.
