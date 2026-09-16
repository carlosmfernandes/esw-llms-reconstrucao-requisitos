<!-- STATUS: OK -->
# CT18 — sub (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional
Subtrair de uma data uma duração composta por anos, meses, semanas, dias, horas, minutos e segundos, produzindo a data resultante.

A operação aplica primeiro anos e meses (convertendo anos em 12 meses), depois semanas e dias (convertendo semanas em 7 dias) e, por fim, horas, minutos e segundos convertidos em milissegundos. Componentes omitidos da duração assumem zero.

### 2. Parâmetros de entrada
- **`date: DateArg<DateType>`**: data de referência da qual será subtraída a duração. Os formatos aceitos por `DateArg` não estão definidos no trecho.
- **`duration: Duration`**: duração a subtrair. A função utiliza os campos `years`, `months`, `weeks`, `days`, `hours`, `minutes` e `seconds`.
- **`options?: SubOptions<ResultDate>`**: opções de contexto, opcionais, repassadas a `subMonths` e `subDays`. Na construção do resultado, `options.in`, quando não nulo nem indefinido, é usado como referência; caso contrário, usa-se `date`. A definição completa dessas opções não aparece no trecho.

### 3. Retorno
Uma data do tipo **`ResultDate`**, que estende `Date`, representando o resultado da subtração.

O trecho não permite determinar detalhes como o tratamento de fim de mês, datas inválidas ou alterações na data original, pois as implementações das funções auxiliares não foram fornecidas.

## Gabarito oficial (date-fns)

- **summary**: Subtract the specified years, months, weeks, days, hours, minutes and seconds from the given date.
- **description**: Subtract the specified years, months, weeks, days, hours, minutes and seconds from the given date.
