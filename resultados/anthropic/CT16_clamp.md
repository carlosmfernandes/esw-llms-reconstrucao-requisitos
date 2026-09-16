<!-- STATUS: OK -->
# CT16 — clamp (anthropic/claude-sonnet-5)

## Resposta do LLM

## 1. Requisito funcional

A função implementa a operação de **restringir (clampar) uma data para dentro de um intervalo especificado**. Ou seja: se a data fornecida estiver antes do início do intervalo, ela é ajustada para a data de início; se estiver depois do fim do intervalo, é ajustada para a data de fim; se já estiver dentro do intervalo, a data é retornada inalterada.

## 2. Parâmetros de entrada

- **`date`** (`DateType extends DateArg<Date>`): a data que se deseja limitar/ajustar dentro do intervalo.
- **`interval`** (`IntervalType extends Interval`): objeto contendo `start` e `end`, que definem os limites (inferior e superior) do intervalo permitido.
- **`options`** (opcional, `ClampOptions<ContextDate>`): opções de contexto (via `ContextOptions`), utilizadas por exemplo para definir o fuso horário ou o tipo/contexto de data (`in`) usado para normalizar e construir o resultado.

## 3. Retorno

Retorna a data resultante da restrição: o **maior valor entre a data e o início do intervalo**, limitado então ao **menor valor entre esse resultado e o fim do intervalo** — ou seja, a data "clampada" dentro de `[interval.start, interval.end]`. O tipo de retorno (`ClampResult`) é inferido a partir das opções fornecidas (`options.in`), do tipo da data de entrada, ou dos tipos de `start`/`end` do intervalo, caso nenhum dos anteriores esteja definido.

## Gabarito oficial (date-fns)

- **summary**: Return a date bounded by the start and the end of the given interval.
- **description**: Clamps a date to the lower bound with the start of the interval and the upper bound with the end of the interval.
