<!-- STATUS: OK -->
# CT29 — addBusinessDays (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise do código: `addBusinessDays`

## 1. Requisito funcional

A função implementa a **adição (ou subtração) de dias úteis a uma data**, desconsiderando sábados e domingos na contagem.

Comportamentos específicos exigidos:
- Se `amount` for positivo, avança dias úteis; se for negativo, retrocede dias úteis.
- Sábados e domingos são pulados e não contam como dias úteis adicionados.
- Se a data original já cair em um fim de semana, a função garante que o resultado final também não caia em um fim de semana, ajustando para o dia útil mais próximo apropriado (considerando a direção da operação).
- Se `amount` for `NaN`, retorna uma data inválida (`NaN`) em vez de tentar processar o cálculo.
- Preserva o horário (`hours`) original da data, evitando efeitos colaterais de mudança de horário de verão (DST) durante os cálculos com `setDate`.

## 2. Parâmetros de entrada

- **`date: DateArg<DateType>`** — A data base à qual os dias úteis serão adicionados/subtraídos. Pode ser uma instância de `Date` ou outro tipo compatível aceito pela biblioteca (conforme `DateArg`).
- **`amount: number`** — A quantidade de dias úteis a adicionar (se positivo) ou subtrair (se negativo) da data.
- **`options?: AddBusinessDaysOptions<ResultDate>`** — Objeto opcional de configuração que estende `ContextOptions<DateType>`. Permite, entre outras coisas, especificar o contexto (`options.in`) usado para construir a data de retorno (por exemplo, para suportar fusos horários ou tipos de data customizados usados pela biblioteca).

## 3. Retorno

Retorna um valor do tipo `ResultDate` (que por padrão é o mesmo tipo de `DateType`), representando a nova data após adicionar/subtrair o número especificado de dias úteis à data de entrada.

- Se `amount` for `NaN`, retorna uma data inválida construída via `constructFrom(options?.in, NaN)`.
- Caso contrário, retorna a data resultante ajustada, preservando o horário original da data de entrada.

## Gabarito oficial (date-fns)

- **summary**: Add the specified number of business days (mon - fri) to the given date.
- **description**: Add the specified number of business days (mon - fri) to the given date, ignoring weekends.
