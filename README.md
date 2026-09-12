# Reconstrução de Requisitos de Software a partir de Código-Fonte: uma Avaliação Comparativa entre Quatro LLMs

Artefatos do Projeto Final da disciplina **Engenharia de Software (DFS03007)**,
Especialização em Desenvolvimento Full Stack — IF Sudeste MG, Campus Manhuaçu.

**Autor:** Carlos Marques Fernandes

## Sobre este repositório

Este repositório reúne os artefatos utilizados no experimento descrito no
relatório técnico: a comparação de quatro *Large Language Models* (ChatGPT,
Gemini, DeepSeek e Claude) na reconstrução de requisitos funcionais e não
funcionais a partir da leitura exclusiva do código-fonte de um protótipo de
Sistema Web de Gestão da Aprendizagem (EduLMS).

O relatório técnico completo (LaTeX/SBC), com a descrição detalhada da
metodologia, do gabarito de requisitos e dos resultados, está no Overleaf do
autor (link abaixo).

## Artefatos deste repositório

```
.
├── prompt/
│   └── prompt-mestre.txt        # Prompt padronizado enviado aos 4 LLMs
├── prototipo/                   # Código-fonte do protótipo avaliado (EduLMS)
│   ├── index.html
│   ├── style.css
│   └── app.js
├── respostas-llms/               # Respostas brutas dos 4 LLMs ao prompt
│   ├── chatgpt.md
│   ├── deepseek.md
│   ├── gemini.md
│   └── claude.md
├── resultados/
│   ├── resultados-experimento.md # Tabela consolidada e análise qualitativa
│   ├── grafico_quantidade.py      # Script que gera o gráfico de resultados
│   └── grafico-quantidade.pdf     # Gráfico (Quantidade de RF+RNF por LLM)
└── screenshots/
    ├── gerar-screenshots.py       # Script Playwright que gera as capturas abaixo
    ├── tela-login.png
    ├── tela-dashboard.png
    └── tela-usuarios.png
```

## Links relacionados

- Relatório técnico completo: [a adicionar]
- Vídeo de apresentação (~10 min): https://drive.google.com/file/d/1Xm_HKWTmrJvzvJHgTwOW2EHTkrLBVGM_/view?usp=sharing
