<!-- STATUS: OK -->
# CT20 — startOfWeek (google/gemini-3.8-flash)

## Resposta do LLM

Com base estritamente no código fornecido:

1. **Requisito funcional:**  
   Calcular e obter a data correspondente ao início da semana (às 00:00:00.000) de uma data de referência informada, permitindo definir qual dia da semana é considerado o primeiro dia (diretamente, via configurações de localidade/*locale* ou assumindo um padrão).

2. **Parâmetros de entrada:**  
   * `date`: A data de referência a ser avaliada para o cálculo do início da semana.
   * `options` *(opcional)*: Objeto de configurações que pode conter:
     * `weekStartsOn`: Valor que define qual dia é considerado o início da semana.
     * `locale`: Objeto com configurações regionais/de localização que também pode especificar o `weekStartsOn`.
     * `in`: Contexto repassado à função `toDate` para a conversão da data.

3. **Retorno:**  
   Um objeto de data (`ResultDate`) ajustado para o primeiro dia da respectiva semana, com o horário zerado em meia-noite (horas, minutos, segundos e milissegundos definidos como `0`).

## Gabarito oficial (date-fns)

- **summary**: Return the start of a week for the given date.
- **description**: Return the start of a week for the given date. The result will be in the local timezone.
