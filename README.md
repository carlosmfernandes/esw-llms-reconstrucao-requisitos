# Reconstrução de Requisitos de Software a partir de Código-Fonte — Avaliação Comparativa entre Quatro Condições Experimentais de LLMs

Artefatos do Projeto Final da disciplina **DFS03007 — Engenharia de Software**
(Pós-graduação Full Stack, IF Sudeste MG, T02 2026.2).

O relatório completo (metodologia, resultados, discussão, ameaças à
validade) está no PDF entregue via SIGAA. Este repositório contém **todos
os artefatos usados para produzir aqueles resultados**: o prompt aplicado,
as 30 unidades de código-fonte, o gabarito oficial, as respostas brutas
das quatro condições experimentais, e os scripts de classificação e de
testes estatísticos.

## Resumo do estudo

Trinta funções da biblioteca [date-fns](https://github.com/date-fns/date-fns)
(TypeScript, licença MIT) foram extraídas do código-fonte oficial —
mantendo seus nomes reais de função e identificadores (sem ofuscação) —
e estratificadas em três níveis de complexidade (fácil / médio / difícil,
10 unidades cada), por um proxy de complexidade `LOC + 2 × branches`.

Cada unidade foi apresentada, em uma única interação (sem ciclo de
refinamento), a quatro condições experimentais de LLM:

| Condição | Modelo |
|---|---|
| `openai` | GPT-6 Astra |
| `anthropic` | Claude Sonnet 5 |
| `google-gemini-3.6-flash` | Gemini 3.6 Flash |
| `google-gemini-3.8-flash` | Gemini 3.8 Flash |

As duas condições Google são duas versões do mesmo modelo subjacente —
uma limitação assumida e discutida no relatório (Seção 6.2), não um
quarto modelo independente. DeepSeek foi cogitado mas excluído do desenho
final por restrição de financiamento (ver relatório); por isso não há
scripts nem resultados dessa condição neste repositório.

Cada resposta foi classificada (correto / parcialmente correto /
incorreto) contra o gabarito oficial — o `@summary`/`@description`
originais do date-fns — e comparada entre as quatro condições com o teste
Q de Cochran, McNemar par a par com correção de Holm, teste de Friedman
(global e por nível de dificuldade) e W de Kendall. Resultado: nenhuma
diferença estatisticamente significativa entre as quatro condições
(Q de Cochran = 4,7143; df = 3; p = 0,194), com um efeito-teto acentuado
(28 a 30 de 30 unidades classificadas como corretas em todas as
condições) — discutido no relatório como provável decorrência de os
nomes de função não terem sido ofuscados.

## Estrutura deste repositório

```
prompt/
  prompt_padrao.md          Prompt único aplicado a cada unidade x condição

unidades/                   As 30 unidades de código-fonte (TypeScript),
                             extraídas verbatim do date-fns (ver LICENSE-date-fns)

gabarito/
  manifest.json              Metadados completos das 30 unidades: id, função,
                              tier, loc, branches, score de complexidade, e o
                              gabarito oficial (summary/description/params/returns
                              extraídos do JSDoc original do date-fns)
  manifest_resumo.csv         Versão tabular resumida do manifest acima

resultados/
  openai/                     30 respostas brutas (.md), uma por unidade
  anthropic/
    _tentativas_anteriores/   4 respostas truncadas por limite de output do
                              provedor em tentativas anteriores (mantidas para
                              transparência; as respostas válidas usadas na
                              análise são os 30 arquivos no nível acima)
  google-gemini-3.6-flash/    30 respostas brutas (.md)
  google-gemini-3.8-flash/    30 respostas brutas (.md)

analise/
  classificacao.py            Script de classificação das respostas contra o gabarito
  classificacao.csv           Resultado da classificação (correto/parcial/incorreto)
  testes_estatisticos.py      Cochran's Q, McNemar+Holm, Friedman, Kendall's W
  resultados_estatisticos.md  Saída/relatório dos testes estatísticos

scripts/
  executar_experimento.py     Execução das condições OpenAI e Anthropic
  executar_google_36.py       Execução da condição Gemini 3.6 Flash
  executar_google_38.py       Execução da condição Gemini 3.8 Flash
  select_and_extract.py       Ver seção "Reprodutibilidade da seleção de unidades" abaixo

LICENSE                       Licença dos scripts e textos originais deste estudo
LICENSE-date-fns               Atribuição MIT do código de terceiros em unidades/
```

## Reprodutibilidade da seleção de unidades (`scripts/select_and_extract.py`)

O script que originalmente selecionou e extraiu as 30 unidades não foi
preservado durante a execução do experimento. `select_and_extract.py` é
uma **reconstrução**, escrita posteriormente, com um limite claramente
documentado no próprio arquivo:

- A fórmula de complexidade (`score = LOC + 2 × branches`) foi deduzida
  por engenharia reversa a partir de `manifest_resumo.csv` e **validada
  empiricamente com 100% de correspondência** nas 30 unidades conhecidas
  (rodar `python3 scripts/select_and_extract.py --validar --repo
  <clone-do-date-fns>` reproduz essa validação).
- O procedimento exato que escolheu, dentre o universo de funções
  candidatas do date-fns, quais 30 específicas compuseram a amostra
  (amostragem aleatória, curadoria manual, etc.) **não pôde ser
  recuperado** e não é reconstruído por este script — ele recebe a lista
  já definida como entrada.
- O levantamento do pool de candidatas feito por este script encontra
  245 funções top-level em `pkgs/core/src`, enquanto a documentação
  interna do projeto registrava 242 — divergência de 3 funções (~1,2%)
  não resolvida com certeza, documentada no próprio script.

Repositório e commit usados como fonte: `date-fns/date-fns` @
`18cbd436f1428d0f45f89f710df65f62546c42f0` (30/08/2026).

## Como reproduzir a classificação e os testes estatísticos

```bash
cd analise
python3 classificacao.py          # gera/atualiza classificacao.csv
python3 testes_estatisticos.py    # gera resultados_estatisticos.md
```

## Licenciamento

- O código em `unidades/` é extraído verbatim da biblioteca `date-fns`
  (MIT, Copyright (C) 2020 Sasha Koss e Lesha Koss) — ver `LICENSE-date-fns`.
- Os scripts e textos originais deste estudo (`scripts/`, `analise/`,
  `prompt/`) estão sob a licença em `LICENSE`.
