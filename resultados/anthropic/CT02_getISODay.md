<!-- STATUS: OK -->
# CT02 — getISODay (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `getISODay`

## 1. Requisito funcional

A função implementa a obtenção do **dia da semana no padrão ISO 8601** para uma data fornecida. 

No padrão ISO 8601, os dias da semana são numerados de 1 (segunda-feira) a 7 (domingo), diferentemente do padrão JavaScript nativo (`Date.getDay()`), que numera de 0 (domingo) a 6 (sábado).

A função converte a data para um objeto `Date` válido e ajusta o valor retornado por `getDay()`: quando o dia nativo é `0` (domingo), converte para `7`; para os demais valores (1 a 6, segunda a sábado), mantém o mesmo número, já que coincidem com a numeração ISO.

## 2. Parâmetros de entrada

- **`date: DateArg<Date> & {}`**: representa a data da qual se deseja extrair o dia da semana ISO. Pode ser um valor aceito pela função `toDate` (provavelmente um `Date`, string, número ou outro tipo compatível, conforme definido em `DateArg`).

- **`options?: GetISODayOptions`** (opcional): objeto de opções que estende `ContextOptions<Date>`. Contém uma propriedade `in`, usada para especificar um contexto (por exemplo, fuso horário ou "engine" de data) que será repassado à função `toDate` para a conversão da data de entrada.

## 3. Retorno

A função retorna um **`number`** representando o dia da semana no formato ISO 8601:
- `1` = segunda-feira
- `2` = terça-feira
- `3` = quarta-feira
- `4` = quinta-feira
- `5` = sexta-feira
- `6` = sábado
- `7` = domingo

## Gabarito oficial (date-fns)

- **summary**: Get the day of the ISO week of the given date.
- **description**: Get the day of the ISO week of the given date, which is 7 for Sunday, 1 for Monday etc.
