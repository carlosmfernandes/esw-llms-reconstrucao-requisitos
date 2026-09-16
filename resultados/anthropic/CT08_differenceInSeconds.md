<!-- STATUS: OK -->
# CT08 — differenceInSeconds (anthropic/claude-sonnet-5)

## Resposta do LLM

# Análise da função `differenceInSeconds`

## 1. Requisito funcional

A função implementa o cálculo da **diferença em segundos completos entre duas datas**. O requisito é permitir que o usuário obtenha quantos segundos separam um instante posterior (`laterDate`) de um instante anterior (`earlierDate`), com a possibilidade de configurar o método de arredondamento do resultado (por exemplo, arredondar para cima, para baixo, ou para o valor mais próximo), já que a divisão de milissegundos por 1000 pode gerar um valor fracionário.

## 2. Parâmetros de entrada

- **`laterDate: DateArg<Date> & {}`**: representa a data/instante posterior (mais recente) na comparação.
- **`earlierDate: DateArg<Date> & {}`**: representa a data/instante anterior (mais antigo) na comparação.
- **`options?: DifferenceInSecondsOptions`**: objeto opcional de configuração que estende `RoundingOptions`, contendo a propriedade `roundingMethod`, usada para definir como o valor fracionário de segundos deve ser arredondado (o método concreto de arredondamento é resolvido pela função auxiliar `getRoundingMethod`).

## 3. Retorno

A função retorna um **`number`**, correspondente à diferença entre `laterDate` e `earlierDate` expressa em segundos, já arredondada de acordo com o método especificado em `options.roundingMethod` (ou o método padrão definido por `getRoundingMethod` caso `options` não seja fornecido ou não contenha essa propriedade).

## Gabarito oficial (date-fns)

- **summary**: Get the number of seconds between the given dates.
- **description**: Get the number of seconds between the given dates.
