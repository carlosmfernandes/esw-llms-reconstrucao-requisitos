<!-- STATUS: OK -->
# CT18 — sub (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `sub`

## 1. Requisito funcional

A função implementa a **subtração de um intervalo de tempo (duração composta) de uma data**. Ela permite subtrair simultaneamente múltiplos componentes de tempo (anos, meses, semanas, dias, horas, minutos e segundos) de uma data de referência, retornando uma nova data resultante.

Ou seja, do ponto de vista de especificação: "dado um ponto no tempo e uma duração (podendo conter várias unidades ao mesmo tempo), retornar a data resultante após subtrair essa duração completa da data original."

A lógica trata unidades de calendário (anos/meses) de forma diferenciada de unidades de tempo fixo (dias/horas/minutos/segundos):
- Anos e meses são convertidos em meses e subtraídos via `subMonths` (que provavelmente lida com peculiaridades de calendário, como dias inválidos em meses diferentes).
- Semanas e dias são convertidos em dias e subtraídos via `subDays`.
- Horas, minutos e segundos são convertidos em milissegundos e subtraídos diretamente por aritmética simples.

## 2. Parâmetros de entrada

- **`date: DateArg<DateType>`** — a data de referência da qual a duração será subtraída (pode ser um objeto `Date` ou algo compatível, conforme o tipo `DateArg`).
- **`duration: Duration`** — um objeto contendo as quantidades a subtrair, com propriedades opcionais: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, `seconds` (todas com valor padrão `0` se não informadas).
- **`options?: SubOptions<ResultDate>`** — objeto opcional de configuração que estende `ContextOptions<DateType>`. Contém, entre outras coisas, uma propriedade `in`, usada para determinar o "contexto" (tipo/fábrica) da data de retorno.

## 3. Retorno

A função retorna um valor do tipo **`ResultDate`** — uma nova instância de data, construída a partir do contexto definido por `options?.in` (ou da `date` original, caso `options.in` não seja fornecido), representando a data original com a duração completa subtraída.

## Gabarito oficial (date-fns)

- **summary**: Subtract the specified years, months, weeks, days, hours, minutes and seconds from the given date.
- **description**: Subtract the specified years, months, weeks, days, hours, minutes and seconds from the given date.
