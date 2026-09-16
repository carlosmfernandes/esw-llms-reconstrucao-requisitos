<!-- STATUS: OK -->
# CT24 — eachDayOfInterval (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas para os três pontos solicitados:

### 1. Requisito Funcional
A função gera uma lista (array) de datas correspondente a todos os dias compreendidos dentro de um intervalo de tempo determinado (entre uma data inicial e uma final). 

A especificação inclui:
* Ajuste automático dos horários para o início do dia (`00:00:00.000`).
* Suporte a um incremento personalizável de dias entre cada elemento gerado.
* Tratamento de ordenação automática: lida com intervalos informados em ordem cronológica inversa ou com incrementos negativos, ajustando a sequência de datas resultante adequadamente.
* Suporte à normalização de contexto/fuso horário do intervalo.

---

### 2. Parâmetros de Entrada

1. **`interval`** (`IntervalType`): 
   Objeto representando o intervalo de tempo de onde os dias serão extraídos. Contém as propriedades de data inicial (`start`) e data final (`end`).

2. **`options`** (`Options`, opcional): 
   Objeto de configurações opcionais que pode conter:
   * **`step`** (`number`): O tamanho do passo/incremento em dias entre cada data da lista (o valor padrão é `1`). Se for `0`, a função interrompe a geração; se for negativo, inverte o sentido da ordenação.
   * **`in`** (origem: `ContextOptions`): Identificador de contexto ou fuso passado para a função auxiliar `normalizeInterval` para ajustar/normalizar as datas do intervalo.

---

### 3. Retorno da Função

Retorna um **array de objetos de data** (do tipo `Date` ou do tipo de data estendido `DateType` informado no contexto). 

* Cada item do array representa um dia dentro do intervalo especificado com o horário fixado em meia-noite (`00:00:00.000`).
* A ordem dos elementos (cronológica direta ou decrescente) depende da relação entre `start` e `end` e do sinal do parâmetro `step`.
* Retorna um array vazio (`[]`) caso o parâmetro `step` seja igual a `0`.

## Gabarito oficial (date-fns)

- **summary**: Return the array of dates within the specified time interval.
- **description**: Return the array of dates within the specified time interval.
