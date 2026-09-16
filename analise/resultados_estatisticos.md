# Resultados estatísticos — Projeto Final ESW (DFS03007)

N = 30 unidades de código por condição; 4 condições independentes (OpenAI, Anthropic, Google gemini-3.6-flash, Google gemini-3.8-flash). DeepSeek fora do estudo (não financiado).

## 1. Resumo descritivo

| Condição | Correto | Parcial | Incorreto | Score total (máx. 30) |
|---|---|---|---|---|
| OpenAI (gpt-6-astra) | 28 | 2 | 0 | 29.0 |
| Anthropic (claude-sonnet-5) | 30 | 0 | 0 | 30.0 |
| Google (gemini-3.6-flash) | 30 | 0 | 0 | 30.0 |
| Google (gemini-3.8-flash) | 29 | 1 | 0 | 29.5 |

## 2. Cochran's Q (diferença global entre as 4 condições)

Binarização usada: `correto` (score=1.0) = 1; `parcial` ou `incorreto` (score<1.0) = 0 — exigida pelo teste, que só aceita dados binários.

- Q = 4.7143, df = 3, p = 0.1940

- **Não significativo** ao nível de 5%. Com apenas 2 das 30 unidades (CT10, CT11) apresentando qualquer discordância entre as 4 condições, o teste tem poder estatístico extremamente baixo — a hipótese nula de que as condições têm a mesma taxa de acerto não pode ser rejeitada, mas isso reflete um **efeito-teto** nos dados, não necessariamente ausência real de diferença entre os modelos.

## 3. McNemar pareado (6 comparações) com correção de Holm

| Par | Discordâncias (A só / B só) | p (McNemar exato) | p (Holm) | Rejeita H0 (5%) |
|---|---|---|---|---|
| OpenAI (gpt-6-astra) vs Anthropic (claude-sonnet-5) | 0 / 2 | 0.5000 | 1.0000 | não |
| OpenAI (gpt-6-astra) vs Google (gemini-3.6-flash) | 0 / 2 | 0.5000 | 1.0000 | não |
| OpenAI (gpt-6-astra) vs Google (gemini-3.8-flash) | 0 / 1 | 1.0000 | 1.0000 | não |
| Anthropic (claude-sonnet-5) vs Google (gemini-3.6-flash) | 0 / 0 | 1.0000 | 1.0000 | não |
| Anthropic (claude-sonnet-5) vs Google (gemini-3.8-flash) | 1 / 0 | 1.0000 | 1.0000 | não |
| Google (gemini-3.6-flash) vs Google (gemini-3.8-flash) | 1 / 0 | 1.0000 | 1.0000 | não |

Nenhuma comparação par a par tem poder estatístico real aqui: o número de unidades discordantes entre qualquer par de condições é 0, 1 ou 2 em 30 — muito pouco para um teste de McNemar detectar diferença, mesmo antes da correção de Holm.

## 4. Friedman global (todas as 30 unidades, score 0/0.5/1)

- Friedman χ² = 4.7143, p = 0.1940

## 5. Friedman + Wilcoxon post-hoc, por tier de dificuldade

### Tier: facil (n=10)

- Friedman χ² = 3.0000, p = 0.3916

  - OpenAI (gpt-6-astra) vs Anthropic (claude-sonnet-5): W=0.00, p=1.0000
  - OpenAI (gpt-6-astra) vs Google (gemini-3.6-flash): W=0.00, p=1.0000
  - OpenAI (gpt-6-astra) vs Google (gemini-3.8-flash): W=0.00, p=1.0000
  - Anthropic (claude-sonnet-5) vs Google (gemini-3.6-flash): idênticos neste tier, Wilcoxon não computável.
  - Anthropic (claude-sonnet-5) vs Google (gemini-3.8-flash): idênticos neste tier, Wilcoxon não computável.
  - Google (gemini-3.6-flash) vs Google (gemini-3.8-flash): idênticos neste tier, Wilcoxon não computável.

### Tier: medio (n=10)

- Friedman χ² = 3.0000, p = 0.3916

  - OpenAI (gpt-6-astra) vs Anthropic (claude-sonnet-5): W=0.00, p=1.0000
  - OpenAI (gpt-6-astra) vs Google (gemini-3.6-flash): W=0.00, p=1.0000
  - OpenAI (gpt-6-astra) vs Google (gemini-3.8-flash): idênticos neste tier, Wilcoxon não computável.
  - Anthropic (claude-sonnet-5) vs Google (gemini-3.6-flash): idênticos neste tier, Wilcoxon não computável.
  - Anthropic (claude-sonnet-5) vs Google (gemini-3.8-flash): W=0.00, p=1.0000
  - Google (gemini-3.6-flash) vs Google (gemini-3.8-flash): W=0.00, p=1.0000

### Tier: dificil (n=10)

- Todas as respostas idênticas entre condições e unidades — Friedman não é computável (variância zero). Efeito-teto total neste tier.

## 6. Kendall's W (tamanho de efeito, concordância de postos entre condições)

- W = 0.0024 (0 = nenhuma concordância de postos além do acaso, 1 = concordância perfeita)

- **Atenção à interpretação**: W saiu baixo (perto de 0), não perto de 1. Isso NÃO significa que os modelos discordam entre si — significa o oposto: em 28 das 30 unidades todas as condições empatam no mesmo valor (todas 'correto'), e postos empatados não contribuem variância nenhuma à estatística de Kendall's W. Como o cálculo de W depende de haver variação de postos entre as unidades para detectar concordância, e só 2 das 30 unidades (CT10, CT11) têm qualquer variação, W fica artificialmente baixo por falta de dados informativos — não por desacordo real entre os modelos. Reportar este resultado citando W isoladamente, sem esta ressalva, seria enganoso.

## 7. Limitação central destes resultados (leia antes de interpretar)

Das 30 unidades, 28 tiveram concordância unânime ("correto") entre as 4 condições; apenas CT10 (`endOfISOWeek`, OpenAI parcial) e CT11 (`isSameWeek`, OpenAI e Gemini-3.8-flash parciais) mostraram qualquer variação. Isso é consistente com uma limitação já registrada no desenho do experimento (`prompt_padrao.md`): os nomes das funções não foram ofuscados nas unidades de tier médio/difícil, e o date-fns é uma biblioteca extremamente popular e bem documentada — é plausível que os 4 modelos tenham memorizado ou reconhecido essas funções em vez de reconstruir o requisito puramente a partir da leitura do código. Isso reduz drasticamente a variância disponível para os testes estatísticos e deve ser discutido como limitação explícita na seção de Discussão do relatório.
