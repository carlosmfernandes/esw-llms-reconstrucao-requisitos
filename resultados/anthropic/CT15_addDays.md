<!-- STATUS: OK -->
# CT15 — addDays (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `addDays`

## 1. Requisito funcional

A função implementa a **adição (ou subtração, se o valor for negativo) de um número de dias a uma data especificada**. É uma operação comum em manipulação de datas, permitindo calcular uma nova data que está *N* dias à frente (ou atrás) de uma data de referência.

Um requisito adicional explícito no código (via comentário) é que a função deve **evitar alterações indesejadas no horário quando o valor somado é zero**, especialmente próximo a transições de horário de verão (DST) — nesse caso, a função retorna a data original sem executar operações que poderiam causar efeitos colaterais no horário.

A função também trata o caso de entrada inválida: se `amount` não for um número válido (`NaN`), o retorno é uma data inválida (`NaN`), propagando o erro de forma consistente.

## 2. Parâmetros de entrada

- **`date: DateArg<DateType>`**: a data base à qual os dias serão adicionados. Pode ser um objeto `Date` ou outro tipo compatível conforme definido por `DateArg`.

- **`amount: number`**: a quantidade de dias a ser adicionada à data. Pode ser positivo (avança a data), negativo (retrocede a data) ou zero (sem alteração).

- **`options?: AddDaysOptions<ResultDate> | undefined`**: parâmetro opcional que permite configurar o contexto de construção da data resultante (via `ContextOptions`), possivelmente definindo o "construtor" (`in`) usado para criar o objeto de data retornado — útil para suportar bibliotecas de data alternativas ou fusos horários customizados.

## 3. Retorno

A função retorna um valor do tipo **`ResultDate`** (que estende `Date`), representando:

- A **data original acrescida do número de dias especificado**, caso a operação seja válida;
- A **data original inalterada**, caso `amount` seja `0`;
- Uma **data inválida (`NaN`)**, construída a partir do contexto (`options?.in`) ou da data de entrada, caso `amount` não seja um número válido.

## Gabarito oficial (date-fns)

- **summary**: Add the specified number of days to the given date.
- **description**: Add the specified number of days to the given date.
