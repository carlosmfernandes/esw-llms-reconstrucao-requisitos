# Prompt padronizado — Experimento expandido (30 unidades de código)

Este é o prompt único, isolado (sem ciclo de correção/refinamento), a ser
enviado para cada uma das 30 unidades de código, para cada um dos LLMs
avaliados — mantendo o mesmo princípio metodológico do experimento
original (interação única, sem refinamento).

## Template

```
Você receberá um trecho de código-fonte extraído de uma biblioteca real de
manipulação de datas (TypeScript). Analise o código e responda, de forma
objetiva:

1. Qual é o requisito funcional que esta função implementa? (o que ela
   faz, do ponto de vista de quem especificou o software — não uma
   descrição linha a linha do código)
2. Quais são os parâmetros de entrada e o que cada um representa?
3. O que a função retorna?

Não presuma nada além do que está no código abaixo. Não pesquise o nome
da função em nenhuma fonte externa — baseie-se exclusivamente na leitura
do código fornecido.

Código:
\`\`\`typescript
<CONTEÚDO DO ARQUIVO unidades/<funcao>.ts>
\`\`\`
```

## Por que este formato

- Pede explicitamente o requisito "funcional" (não um resumo do código
  linha a linha) — é isso que será comparado ao gabarito (`@summary` +
  `@description` oficiais do date-fns).
- Pede parâmetros e retorno separadamente porque o gabarito também tem
  `@param`/`@returns` — permite avaliar por partes (requisito central x
  detalhes de assinatura), assim como a rubrica de "causas de falha" do
  colega (Jackson) separa esses aspectos.
- Proíbe explicitamente pesquisar o nome da função — o ponto do
  experimento é reconstrução a partir do código-fonte, não busca externa
  (o nome da função nas unidades médias/difíceis não é ofuscado
  propositalmente, ver `README.md`, mas a instrução evita que o LLM
  simplesmente cite a documentação pública do date-fns de memória em vez
  de ler o código).
- Interação única por unidade por LLM = mesmo princípio "sem
  refinamento" do experimento original.

## Avaliação (correto / parcialmente correto / incorreto)

Sugestão de rubrica objetiva, para manter a mesma classe de rigor do
colega Jackson (que usou testes estatísticos formais):

- **Correto**: a resposta do LLM ao item 1 (requisito funcional) é
  semanticamente equivalente ao `summary` oficial, sem afirmar nada que o
  gabarito contradiga.
- **Parcialmente correto**: captura a ideia geral mas erra ou omite um
  aspecto relevante (ex.: não menciona o tratamento de exceções — DST,
  NaN, dias úteis — que o `description`/código deixam claro).
- **Incorreto**: descreve um comportamento diferente do real, ou inventa
  comportamento não presente no código.

Essa classificação binarizável (correto=1 / não-correto=0, ou
correto=1/parcial=0.5/incorreto=0) é o que viabiliza os mesmos testes que
o colega aplicou (Cochran's Q entre LLMs, McNemar par a par com correção
de Holm, e testes por tier de dificuldade).
