# CT01 — isLeapYear (google/gemini-3.6-flash)

## Resposta do LLM

Com base exclusivamente no código fornecido, aqui estão as respostas para os três pontos solicitados:

### 1. Requisito Funcional
A função implementa a verificação de ano bissexto. Do ponto de vista de especificação, ela tem como objetivo determinar se uma determinada data pertence a um ano bissexto (seguindo a regra: divisível por 400 **ou** divisível por 4 e não por 100).

---

### 2. Parâmetros de Entrada
A função aceita dois parâmetros:

1. **`date`** (`DateArg<Date> & {}`): 
   * Representa a data (ou argumento de data) que se deseja analisar para verificar se o seu ano é bissexto.
2. **`options`** (`IsLeapYearOptions | undefined`, opcional): 
   * Representa um objeto de opções/configurações contextuais (estendendo `ContextOptions<Date>`). É utilizado para passar um contexto/fuso ou parâmetro de conversão (propriedade `in`) para a função auxiliar `toDate`.

---

### 3. Retorno da Função
* **Tipo:** `boolean`
* **Descrição:** Retorna `true` se o ano da data informada for bissexto, ou `false` caso contrário.

## Gabarito oficial (date-fns)

- **summary**: Is the given date in the leap year?
- **description**: Is the given date in the leap year?
