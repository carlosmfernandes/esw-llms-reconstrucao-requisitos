<!-- STATUS: OK -->
# CT23 — intervalToDuration (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no trecho de código fornecido, aqui estão as respostas para cada uma das perguntas:

---

### 1. Requisito Funcional
A função converte um intervalo de tempo (delimitado por uma data inicial e uma data final) em um objeto de duração decomposto em unidades de tempo consecutivas (anos, meses, dias, horas, minutos e segundos). 

Ela calcula a diferença acumulada entre o início e o fim do intervalo, atribuindo a duração restante a cada unidade temporal da maior (anos) para a menor (segundos), omitindo as unidades que resultarem em zero.

---

### 2. Parâmetros de Entrada
* **`interval`** (tipo `Interval`): O intervalo de tempo a ser convertido, contendo os pontos de início e fim.
* **`options`** (tipo `IntervalToDurationOptions | undefined`, opcional): Objeto opcional com opções de contexto/configuração, utilizado especificamente para passar a propriedade `in` para a função de normalização do intervalo (`normalizeInterval`).

---

### 3. Retorno da Função
Retorna um objeto do tipo **`Duration`** contendo as propriedades numéricas correspondentes a cada unidade de tempo calculada (`years`, `months`, `days`, `hours`, `minutes`, `seconds`). Apenas as unidades com valores diferentes de zero (ou seja, equivalentes a *truthy*) são incluídas no objeto retornado.

## Gabarito oficial (date-fns)

- **summary**: Convert interval to duration
- **description**: Convert an interval object to a duration object.
