<!-- STATUS: OK -->
# CT23 — intervalToDuration (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional
Converter um intervalo entre duas datas em uma duração decomposta em **anos, meses, dias, horas, minutos e segundos**.

A decomposição é sequencial: cada unidade é calculada sobre o que resta do intervalo após considerar as unidades anteriores. Assim, os componentes não são totais independentes de cada unidade.

### 2. Parâmetros de entrada
- **`interval: Interval`**: intervalo que fornece as datas de início (`start`) e fim (`end`), obtidas por meio de `normalizeInterval`.
- **`options?: IntervalToDurationOptions`**: opções opcionais de contexto. Neste trecho, apenas `options.in` é utilizado, sendo repassado à normalização do intervalo. Seu comportamento específico não pode ser determinado sem a definição dos elementos importados.

### 3. Retorno
Um objeto do tipo **`Duration`**, que pode conter as propriedades:
```typescript
{ years, months, days, hours, minutes, seconds }
```
Cada propriedade só é incluída se o valor calculado passar no respectivo `if`; em particular, **valores zero são omitidos**. Se nenhum componente for incluído, retorna `{}`. O código não inclui um componente de milissegundos.

Detalhes como tratamento de datas inválidas, intervalos invertidos e regras exatas de cálculo das diferenças dependem das funções importadas e não estão explícitos neste trecho.

## Gabarito oficial (date-fns)

- **summary**: Convert interval to duration
- **description**: Convert an interval object to a duration object.
