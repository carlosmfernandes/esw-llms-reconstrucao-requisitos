<!-- STATUS: OK -->
# CT06 — getDayOfYear (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise do código

## 1. Requisito funcional

A função implementa o cálculo do **dia do ano** (day of year) correspondente a uma data fornecida — ou seja, determina qual é o número sequencial do dia dentro do ano ao qual a data pertence (variando de 1 a 365 ou 366, dependendo se o ano é bissexto).

Por exemplo: 1º de janeiro retorna 1; 1º de fevereiro retorna 32 (em ano não bissexto); 31 de dezembro retorna 365 ou 366.

O cálculo é feito determinando a diferença em dias de calendário entre a data informada e o início do ano correspondente, somando 1 ao resultado (já que o próprio primeiro dia do ano deve ser contado como dia 1, não dia 0).

## 2. Parâmetros de entrada

- **`date`**: `DateArg<Date> & {}` — a data para a qual se deseja calcular o dia do ano. Representa o valor de entrada a ser convertido/normalizado internamente via `toDate`.
- **`options`** (opcional): `GetDayOfYearOptions | undefined` — objeto de opções que estende `ContextOptions<Date>`. Permite especificar um contexto (`options?.in`), provavelmente utilizado para definir o fuso horário ou o tipo de objeto de data a ser usado na conversão via `toDate`.

## 3. Retorno

A função retorna um **`number`**, representando o dia do ano correspondente à data fornecida (um inteiro positivo, tipicamente entre 1 e 366).

## Gabarito oficial (date-fns)

- **summary**: Get the day of the year of the given date.
- **description**: Get the day of the year of the given date.
