<!-- STATUS: OK -->
# CT14 — setYear (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `setYear`

## 1. Requisito funcional

A função implementa a capacidade de **definir (substituir) o ano de uma data específica**, retornando uma nova data com o ano alterado, mantendo mês, dia e horário originais.

Um requisito adicional tratado explicitamente é a **preservação da semântica de "Invalid Date"**: caso a data de entrada seja inválida, a função deve retornar uma data inválida (em vez de tentar aplicar o ano, já que o método nativo `setFullYear` do JavaScript ignora silenciosamente uma data inválida e produz efeitos inesperados).

Há também suporte a um **contexto de data customizado** (via `options.in`), permitindo que o tipo/construtor da data resultante seja controlado externamente (útil para trabalhar com bibliotecas que estendem `Date`, como datas com fuso horário).

## 2. Parâmetros de entrada

- **`date: DateArg<DateType>`** — a data original sobre a qual a alteração de ano será aplicada. Pode ser um objeto `Date`, timestamp ou outro formato aceito por `DateArg`.
- **`year: number`** — o valor numérico do ano que deve ser atribuído à data.
- **`options?: SetYearOptions<ResultDate>`** — objeto opcional de configuração, que estende `ContextOptions`. Contém a propriedade `in`, usada para especificar o contexto/construtor da data resultante (ex.: para preservar fuso horário ou classe customizada de data).

## 3. Retorno

A função retorna um **novo objeto de data (`ResultDate`)** com o ano substituído pelo valor informado.

- Se a data de entrada for inválida (`NaN`), retorna uma **data inválida** construída a partir do contexto (`options?.in`) ou da data original, preservando o tipo esperado.
- Caso contrário, retorna a data original modificada (mesma referência de objeto retornada por `toDate`), com o novo ano aplicado via `setFullYear`.

## Gabarito oficial (date-fns)

- **summary**: Set the year to the given date.
- **description**: Set the year to the given date.
