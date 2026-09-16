<!-- STATUS: OK -->
# CT01 — isLeapYear (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise do código

## 1. Requisito funcional

A função verifica se o ano correspondente a uma data fornecida é um **ano bissexto**, seguindo a regra do calendário gregoriano:
- É bissexto se for divisível por 400, **ou**
- É bissexto se for divisível por 4 mas **não** for divisível por 100.

## 2. Parâmetros de entrada

- **`date: DateArg<Date> & {}`**: representa a data a ser avaliada. Pode ser um valor compatível com `Date` (como um objeto `Date`, string ou timestamp, dependendo do tipo `DateArg`). É convertida internamente através da função `toDate` para garantir um objeto `Date` válido.

- **`options?: IsLeapYearOptions | undefined`** (opcional): objeto de configuração que estende `ContextOptions<Date>`. Permite especificar um contexto (`options.in`) usado na conversão da data (por exemplo, para lidar com fuso horário ou "contexto" de data conforme definido pela função `toDate`).

## 3. Retorno

A função retorna um **`boolean`**:
- `true` se o ano da data fornecida for um ano bissexto;
- `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Is the given date in the leap year?
- **description**: Is the given date in the leap year?
