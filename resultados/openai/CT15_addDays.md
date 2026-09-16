<!-- STATUS: OK -->
# CT15 — addDays (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional**  
   Acrescentar uma quantidade de **dias de calendário** a uma data de referência, ou retroceder dias quando a quantidade for negativa. O ajuste é feito pelo dia do mês (`getDate`/`setDate`), e não pela soma de uma duração fixa em milissegundos.  
   Se a quantidade for zero, retorna a data obtida na conversão inicial, sem ajustar seu dia, evitando a alteração de horário mencionada no comentário sobre horário de verão.

2. **Parâmetros de entrada**
   - **`date: DateArg<DateType>`**: data de referência, passada a `toDate` antes do cálculo. Os formatos aceitos por `DateArg` não podem ser determinados pelo trecho, pois sua definição não foi fornecida.
   - **`amount: number`**: quantidade de dias a acrescentar; valores negativos representam retrocesso.
   - **`options?: AddDaysOptions<ResultDate>`**: opções opcionais de contexto. A propriedade `in` é usada na conversão inicial e, quando aplicável, na construção do resultado para uma quantidade inválida. O funcionamento específico desse contexto não está definido no trecho.

3. **Retorno**  
   Um resultado tipado como **`ResultDate`**, que estende `Date`:
   - normalmente, a data obtida por `toDate`, ajustada pela quantidade informada;
   - para zero, essa mesma data sem ajuste;
   - se `isNaN(amount)` for verdadeiro, o resultado de `constructFrom(options?.in || date, NaN)`. O comportamento exato dessa construção depende da implementação de `constructFrom`, não incluída no código.

## Gabarito oficial (date-fns)

- **summary**: Add the specified number of days to the given date.
- **description**: Add the specified number of days to the given date.
