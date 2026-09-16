<!-- STATUS: OK -->
# CT10 — endOfISOWeek (google/gemini-3.8-flash)

## Resposta do LLM

Com base estritamente no código fornecido:

1. **Requisito funcional:**
   A função calcula e determina o final da semana no padrão ISO para uma data informada (considerando a segunda-feira como o primeiro dia da semana, indicado por `weekStartsOn: 1`).

2. **Parâmetros de entrada:**
   * `date` (`DateArg<DateType>`): A data de referência a partir da qual o final da semana ISO será calculado.
   * `options` (`EndOfISOWeekOptions<ResultDate> | undefined`, opcional): Objeto de opções e configurações de contexto adicionais repassadas para o cálculo.

3. **Retorno:**
   * Retorna um objeto de data (`ResultDate`, subtipo de `Date`) que representa a data correspondente ao fim da semana ISO para a data fornecida.

## Gabarito oficial (date-fns)

- **summary**: Return the end of an ISO week for the given date.
- **description**: Return the end of an ISO week for the given date. The result will be in the local timezone.
