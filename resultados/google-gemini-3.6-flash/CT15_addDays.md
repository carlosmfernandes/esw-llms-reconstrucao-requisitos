# CT15 — addDays (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas:

---

### 1. Requisito Funcional
A função tem como objetivo **adicionar um determinado número de dias a uma data fornecida**. 

Do ponto de vista de especificação:
* Adiciona a quantidade especificada de dias à data inicial.
* Se a quantidade de dias for `0`, a data deve ser mantida inalterada.
* Se a quantidade de dias não for um número válido (`NaN`), deve retornar uma representação de data inválida.
* Suporta a especificação de um contexto de data personalizado para o cálculo e retorno através de opções.

---

### 2. Parâmetros de Entrada

1. **`date`** (`DateArg<DateType>`): A data inicial (ou valor conversível em data) que servirá como base para a adição dos dias.
2. **`amount`** (`number`): A quantidade de dias a ser adicionada à data base (pode ser positivo, negativo ou zero).
3. **`options`** (`AddDaysOptions<ResultDate> | undefined`, opcional): Objeto de configurações adicionais que permite definir o contexto de data desejado para o processamento e o resultado (utilizando a propriedade `in`).

---

### 3. Retorno da Função

Retorna um objeto do tipo data (`ResultDate`) contendo:
* A nova data resultante da soma dos dias à data inicial; **ou**
* A própria data convertida e inalterada (caso `amount` seja `0`); **ou**
* Uma data inválida (representada internamente com `NaN`), caso o parâmetro `amount` seja `NaN`.

## Gabarito oficial (date-fns)

- **summary**: Add the specified number of days to the given date.
- **description**: Add the specified number of days to the given date.
