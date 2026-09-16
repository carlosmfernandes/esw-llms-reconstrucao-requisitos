<!-- STATUS: OK -->
# CT20 — startOfWeek (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise do código

## 1. Requisito funcional

A função implementa o cálculo do **início da semana** para uma data fornecida. Ou seja, dada uma data qualquer, ela retorna a data correspondente ao primeiro dia da semana à qual essa data pertence, com o horário zerado (00:00:00.000).

O requisito permite configurar **qual dia é considerado o início da semana** (por exemplo, domingo, segunda-feira, etc.), seja através de uma opção explícita, de um locale (localização/idioma) que define essa convenção, ou de opções padrão configuradas globalmente na biblioteca. Caso nenhuma dessas fontes especifique o dia de início, o padrão assumido é domingo (valor `0`).

## 2. Parâmetros de entrada

- **`date: DateArg<DateType>`**: a data de referência a partir da qual se deseja calcular o início da semana. Pode ser um objeto `Date` ou outro tipo compatível aceito pela função `toDate`.

- **`options?: StartOfWeekOptions<ResultDate>`** (opcional): objeto de configuração que pode conter:
  - **`weekStartsOn`**: um número indicando qual dia da semana é considerado o início (ex.: 0 = domingo, 1 = segunda-feira, etc.), com prioridade mais alta.
  - **`locale`**: um objeto de localização que pode definir seu próprio `weekStartsOn` padrão (usado se `weekStartsOn` não for passado diretamente).
  - **`in`**: contexto/opção repassada para a função `toDate`, provavelmente para especificar o tipo/fuso da data resultante.

## 3. Retorno

A função retorna um objeto do tipo **`ResultDate`** (que estende `Date`), representando a data do **primeiro dia da semana** que contém a data de entrada, com o horário ajustado para **00:00:00.000** (meia-noite).

## Gabarito oficial (date-fns)

- **summary**: Return the start of a week for the given date.
- **description**: Return the start of a week for the given date. The result will be in the local timezone.
