<!-- STATUS: OK -->
# CT29 — addBusinessDays (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional
Calcular uma data ao **adicionar ou subtrair uma quantidade de dias úteis** de uma data inicial, desconsiderando sábados e domingos na contagem.

- Quantidades positivas avançam a data; negativas retrocedem.
- Não há tratamento de feriados no trecho.
- Quantidade zero não desloca a data, mesmo que ela caia em um fim de semana.
- A função restaura a hora original após os ajustes, com a intenção explícita de evitar deslocamentos decorrentes do horário de verão.

### 2. Parâmetros de entrada
- **`date: DateArg<DateType>`**: data inicial do cálculo. É convertida por `toDate`. As formas exatas aceitas por `DateArg` não estão definidas no trecho.
- **`amount: number`**: quantidade de dias úteis a adicionar ou subtrair, conforme o sinal.
- **`options?: AddBusinessDaysOptions<ResultDate>`**: opções opcionais de contexto. O campo `in` é passado à conversão e à construção de datas; o objeto de opções também é passado às verificações de fim de semana. A definição detalhada dessas opções não foi fornecida.

### 3. Retorno
Uma data do tipo **`ResultDate`**, que estende `Date`, representando o resultado do deslocamento.

Se `amount` for `NaN`, retorna diretamente o resultado de `constructFrom(options?.in, NaN)`, em vez de realizar o cálculo.

**Observação:** não há validação de que `amount` seja inteiro. Para valores fracionários finitos, uma fração residual faz o laço contar mais um dia útil; portanto, não se deve presumir truncamento simples da quantidade total.

## Gabarito oficial (date-fns)

- **summary**: Add the specified number of business days (mon - fri) to the given date.
- **description**: Add the specified number of business days (mon - fri) to the given date, ignoring weekends.
