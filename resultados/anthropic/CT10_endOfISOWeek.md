<!-- STATUS: OK -->
# CT10 — endOfISOWeek (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise do código: `endOfISOWeek`

## 1. Requisito funcional

A função implementa o cálculo do **final da semana ISO 8601** para uma data fornecida. 

De acordo com o padrão ISO 8601, a semana começa na **segunda-feira** (dia 1) e termina no **domingo**. Esta função retorna o momento correspondente ao último instante do domingo (fim do dia) da semana em que a data informada se encontra, seguindo essa convenção.

Ela reutiliza a função genérica `endOfWeek`, fixando o parâmetro `weekStartsOn` como `1` (segunda-feira), garantindo o comportamento específico do padrão ISO, independentemente de outras configurações padrão de localidade.

## 2. Parâmetros de entrada

- **`date: DateArg<DateType>`**  
  A data de referência a partir da qual será calculado o fim da semana ISO. Pode ser um objeto `Date` (ou subtipo `DateType`) ou outro formato aceito pelo tipo `DateArg`.

- **`options?: EndOfISOWeekOptions<ResultDate> | undefined`** *(opcional)*  
  Objeto de opções que estende `ContextOptions<DateType>`. Não define propriedades próprias além das herdadas — presumivelmente inclui configurações de contexto (como fuso horário ou "context" de cálculo), conforme definido em `ContextOptions`. Note que o `weekStartsOn` **não** pode ser sobrescrito por este parâmetro, pois é forçado para `1` internamente.

## 3. Retorno

A função retorna um valor do tipo **`ResultDate`** (que por padrão é o mesmo tipo de `DateType`), representando a data/hora correspondente ao **fim do domingo** da semana ISO que contém a data de entrada — ou seja, o resultado delegado pela chamada a `endOfWeek(date, { ...options, weekStartsOn: 1 })`.

## Gabarito oficial (date-fns)

- **summary**: Return the end of an ISO week for the given date.
- **description**: Return the end of an ISO week for the given date. The result will be in the local timezone.
