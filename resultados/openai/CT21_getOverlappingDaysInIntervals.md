<!-- STATUS: OK -->
# CT21 — getOverlappingDaysInIntervals (openai/gpt-6-astra)

## Resposta do LLM

1. **Requisito funcional**  
   Calcular a quantidade de dias de sobreposição entre dois intervalos, **arredondando para cima para incluir frações de dia**. A função:
   - Aceita os extremos de cada intervalo em qualquer ordem, colocando o menor antes do maior.
   - Retorna `0` quando não há sobreposição, inclusive quando os intervalos apenas se tocam em um extremo.
   - Ajusta os extremos da sobreposição pelos respectivos offsets de fuso horário, com a intenção explícita de neutralizar o efeito do horário de verão no cálculo.

2. **Parâmetros de entrada**
   - `intervalLeft: Interval`: primeiro intervalo, com os campos `start` e `end`.
   - `intervalRight: Interval`: segundo intervalo, também com `start` e `end`.

   Esses campos representam os extremos temporais dos intervalos e são convertidos por `toDate`. O trecho não mostra a definição de `Interval` nem os tipos de valores aceitos por essa conversão.

3. **Retorno**  
   Um `number` correspondente à duração da sobreposição, após o ajuste de fuso, dividida por `millisecondsInDay` e arredondada para cima com `Math.ceil`; ou `0` quando não há sobreposição.

   Trata-se de uma **duração expressa em dias arredondados**, não de uma contagem de datas distintas do calendário.

## Gabarito oficial (date-fns)

- **summary**: Get the number of days that overlap in two time intervals
- **description**: Get the number of days that overlap in two time intervals. It uses the time between dates to calculate the number of days, rounding it up to include partial days.
