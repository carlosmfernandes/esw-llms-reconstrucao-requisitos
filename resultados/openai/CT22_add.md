<!-- STATUS: OK -->
# CT22 — add (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional**  
   Calcular a data resultante da adição de uma duração a uma data de referência. A aplicação ocorre nesta ordem:
   - anos e meses, convertendo cada ano em 12 meses;
   - semanas e dias, convertendo cada semana em 7 dias;
   - horas, minutos e segundos, convertidos em milissegundos e somados ao valor numérico da data intermediária.

   Os componentes da duração que não forem informados assumem zero.

2. **Parâmetros de entrada**
   - **`date: DateArg<DateType>`**: data de referência para o cálculo. O trecho não contém a definição de `DateArg`, portanto não permite enumerar todos os formatos aceitos.
   - **`duration: Duration`**: duração a adicionar. A função utiliza os campos `years`, `months`, `weeks`, `days`, `hours`, `minutes` e `seconds`.
   - **`options?: AddOptions<ResultDate>`**: opções opcionais. O único campo utilizado é `in`, passado à conversão inicial da data e, quando verdadeiro, usado como referência para construir o resultado. A definição completa desse contexto não aparece no trecho.

3. **Retorno**  
   Um objeto do tipo **`ResultDate`**, que estende `Date`, representando a data após essas adições. Ele é produzido por `constructFrom`, usando `options.in || date` como referência de construção.

   As regras específicas de ajuste de calendário, como o tratamento de fins de mês, não podem ser determinadas sem o código das funções auxiliares.

## Gabarito oficial (date-fns)

- **summary**: Add the specified years, months, weeks, days, hours, minutes, and seconds to the given date.
- **description**: Add the specified years, months, weeks, days, hours, minutes, and seconds to the given date.
