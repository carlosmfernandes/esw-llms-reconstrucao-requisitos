# Resultados — Comparação de LLMs na Reconstrução de Requisitos a partir do Código

## Correção ao gabarito original
RNF05 (Boas práticas de desenvolvimento) foi reclassificado de "não implementado" para **parcialmente implementado**: o protótipo separa corretamente estrutura (`index.html`), apresentação (`style.css`) e comportamento (`app.js`) em arquivos distintos — boa prática atendida — mas o conteúdo de `app.js` é denso e pouco comentado — boa prática não atendida nesse aspecto. Não entra na contagem binária de 17 itens para não distorcer os totais já calculados.

## Tabela de resultados

| Métrica | ChatGPT | DeepSeek | Gemini | Claude |
|---|---|---|---|---|
| Quantidade de requisitos identificados | 30 (23 RF + 7 RNF) | 23 (16 RF + 7 RNF) | 15 (11 RF + 4 RNF) | 21 (14 RF + 7 RNF) |
| Recall (dos 7 itens implementados) | 7/7 — 100% | 7/7 — 100% | 7/7 — 100% | 7/7 — 100% |
| Precisão | 100% | 100% | 100% | 100% |
| F1-Score | 100% | 100% | 100% | 100% |
| Taxa de alucinação (dos 10 itens não implementados) | 0/10 — 0% | 0/10 — 0% | 0/10 — 0% | 0/10 — 0% |

## Leitura dos resultados

Os quatro LLMs empataram nas métricas binárias (Recall, Precisão, F1, alucinação): todos identificaram corretamente os 7 requisitos realmente implementados no protótipo e nenhum afirmou existir qualquer um dos 10 requisitos que são apenas planejados (autenticação real, persistência, CRUD de usuários/cursos/disciplinas/materiais, segurança, acessibilidade). Esse é um resultado legítimo — não uma falha do desenho experimental — mas, isoladamente, não diferencia os modelos.

A diferenciação real aparece em duas dimensões complementares, que o próprio TCC da UFU usado como molde também mediu (Quantidade, além de Precisão/Recall/F1):

**Quantidade de itens identificados**: ChatGPT (30) > DeepSeek (23) > Claude (21) > Gemini (15). ChatGPT foi o mais granular, decompondo cada tela/interação em um requisito próprio. Gemini foi o mais consolidado, agrupando itens relacionados sob um mesmo requisito.

**Profundidade qualitativa da análise**: ChatGPT foi o único a comparar explicitamente os próprios textos/rótulos presentes no código (ex.: o subtítulo "Cadastro e gerenciamento dos usuários", escrito dentro de `app.js`) com o comportamento real da tela correspondente, apontando a inconsistência entre o que o rótulo sugere e o que o código de fato faz — um raciocínio de verificação cruzada dentro do próprio código fornecido, não informação externa. Claude se destacou por nomear explicitamente, como requisitos não funcionais à parte, a ausência de autenticação real e a ausência de persistência de dados. DeepSeek e Gemini foram mais diretos e concisos, sem essa camada extra de verificação cruzada, mas sem nenhum erro.

## Achado central para a Discussão

Nenhum dos quatro LLMs testados superestimou as funcionalidades de um protótipo front-end simples a partir de convenções típicas de nomes/estrutura de um LMS (ex.: não presumiram banco de dados, API ou autenticação real só porque o sistema "parece" um LMS completo). Isso sugere, nesta amostra, boa capacidade de fundamentação (grounding) dos modelos testados ao código fornecido — mas a variação de granularidade (Quantidade) mostra que "acertar" não significa "analisar com a mesma profundidade": ChatGPT entregou uma análise 2x mais granular que o Gemini, mesmo cobrindo exatamente os mesmos fatos corretos.
