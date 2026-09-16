<!-- STATUS: OK -->
# CT21 — getOverlappingDaysInIntervals (google/gemini-3.6-flash)

## Resposta do LLM

Com base estritamente no código fornecido, aqui estão as respostas para os itens solicitados:

### 1. Requisito Funcional
A função implementa a **contagem do número de dias em que dois intervalos de datas se sobrepõem**. 
Do ponto de vista funcional:
* Se os intervalos não se cruzam/sobrepõem, o resultado é `0`.
* Se há sobreposição, a função calcula a duração dessa sobreposição em dias, arredondando para cima para incluir dias parciais (qualquer fração de dia sobreposta conta como um dia).
* A função trata a ordenação interna das datas de início e fim de cada intervalo (garantindo o cálculo correto mesmo que sejam informadas invertidas) e ajusta os efeitos de fuso horário/horário de verão.

### 2. Parâmetros de Entrada
* **`intervalLeft`** (tipo `Interval`): Objeto que representa o primeiro intervalo de tempo, contendo as propriedades para a data inicial (`start`) e a data final (`end`).
* **`intervalRight`** (tipo `Interval`): Objeto que representa o segundo intervalo de tempo, também contendo as propriedades para a data inicial (`start`) e a data final (`end`).

### 3. Retorno da Função
* Retorna um número (**`number`**) representando a quantidade inteira de dias (com arredondamento para cima) de sobreposição entre os dois intervalos. Retorna `0` caso não haja sobreposição.

## Gabarito oficial (date-fns)

- **summary**: Get the number of days that overlap in two time intervals
- **description**: Get the number of days that overlap in two time intervals. It uses the time between dates to calculate the number of days, rounding it up to include partial days.
