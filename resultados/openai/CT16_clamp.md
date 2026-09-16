<!-- STATUS: OK -->
# CT16 — clamp (openai/gpt-6-astra)

## Resposta do LLM

### 1. Requisito funcional

**Limitar uma data aos limites de um intervalo**, conforme a composição `min(max(data, início), fim)`.

Para um intervalo com início menor ou igual ao fim, isso significa:
- Se a data estiver antes do início, retornar o início.
- Se estiver depois do fim, retornar o fim.
- Se estiver dentro do intervalo, inclusive nos limites, manter seu valor.

O trecho não apresenta validação da ordem dos limites. O tratamento de datas inválidas e os detalhes da normalização dependem das funções importadas, cujas implementações não foram fornecidas.

### 2. Parâmetros de entrada

- **`date: DateType`**: a data que será limitada ao intervalo. Seu tipo deve satisfazer `DateArg<Date>`; os formatos aceitos não podem ser enumerados apenas com este trecho, pois a definição de `DateArg` não está presente.
- **`interval: IntervalType`**: o intervalo delimitador, com **`start`** (início) e **`end`** (fim).
- **`options?: Options`**: opções opcionais do tipo `ClampOptions`, que estende `ContextOptions`. A propriedade `options?.in` é passada à normalização, e o objeto `options` é repassado a `max` e `min`. Seus detalhes não estão definidos no código apresentado.

### 3. Retorno

Retorna a **data resultante da limitação**, com tipo declarado por `ClampResult`.

Esse tipo é escolhido, em ordem de prioridade, a partir:
1. Do tipo de data inferido das opções, quando aplicável.
2. Do tipo de `date`, se estender `Date`.
3. Do tipo de `interval.start`, se estender `Date`.
4. Do tipo de `interval.end`, se estender `Date`.
5. De `Date`, como alternativa final.

O trecho não permite afirmar se o objeto retornado é uma instância original ou uma nova instância.

## Gabarito oficial (date-fns)

- **summary**: Return a date bounded by the start and the end of the given interval.
- **description**: Clamps a date to the lower bound with the start of the interval and the upper bound with the end of the interval.
