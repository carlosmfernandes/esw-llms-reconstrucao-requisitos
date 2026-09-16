<!-- STATUS: OK -->
# CT23 — intervalToDuration (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `intervalToDuration`

## 1. Requisito funcional

A função converte um **intervalo de tempo** (definido por uma data de início e uma data de fim) em uma **duração decomposta em unidades de calendário** (anos, meses, dias, horas, minutos e segundos).

O comportamento esperado é calcular, de forma cumulativa e hierárquica, quanto tempo se passou entre `start` e `end`, expressando o resultado da forma mais "humana" possível — por exemplo, em vez de retornar apenas "400 dias", retorna algo como "1 ano, 1 mês e 5 dias".

A lógica segue uma abordagem sequencial:
- Calcula a diferença em anos completos entre `start` e `end`.
- Soma esses anos a `start` e calcula a diferença em meses completos restante.
- Soma os meses ao resultado anterior e calcula os dias restantes.
- Repete o processo para horas, minutos e segundos.

Cada unidade só é incluída no resultado (`duration`) se seu valor for diferente de zero (truthy), ou seja, unidades com valor 0 são omitidas do objeto retornado.

## 2. Parâmetros de entrada

- **`interval: Interval`** — Um objeto representando o intervalo de tempo, contendo (presumivelmente, com base no uso via `normalizeInterval`) as propriedades `start` e `end`, que demarcam o início e o fim do período a ser medido.

- **`options?: IntervalToDurationOptions`** — Objeto opcional de configuração que estende `ContextOptions<Date>`. Com base no uso (`options?.in`), permite especificar um contexto (provavelmente um fuso horário ou uma função de conversão de data) usado na normalização do intervalo antes dos cálculos.

## 3. Retorno

A função retorna um objeto do tipo **`Duration`**, contendo as propriedades opcionais `years`, `months`, `days`, `hours`, `minutes` e `seconds` — cada uma presente somente se seu valor calculado for diferente de zero. O objeto representa a duração total do intervalo decomposta nessas unidades.

## Gabarito oficial (date-fns)

- **summary**: Convert interval to duration
- **description**: Convert an interval object to a duration object.
