<!-- STATUS: OK -->
# CT21 — getOverlappingDaysInIntervals (google/gemini-3.8-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido:

**1. Requisito funcional:**
Calcular o número de dias de sobreposição (interseção temporal) entre dois intervalos de datas, arredondando qualquer fração de dia para cima (de modo a incluir dias parciais) e retornando zero caso os intervalos não se cruzem.

**2. Parâmetros de entrada:**
* `intervalLeft`: O primeiro intervalo de tempo (`Interval`), composto por uma data inicial (`start`) e uma data final (`end`).
* `intervalRight`: O segundo intervalo de tempo (`Interval`), também composto por uma data inicial (`start`) e uma data final (`end`).

**3. Retorno da função:**
Retorna um valor numérico (`number`) representando a quantidade de dias (arredondada para cima) em que os dois intervalos coincidem no tempo, ou `0` caso não haja sobreposição entre eles.

## Gabarito oficial (date-fns)

- **summary**: Get the number of days that overlap in two time intervals
- **description**: Get the number of days that overlap in two time intervals. It uses the time between dates to calculate the number of days, rounding it up to include partial days.
