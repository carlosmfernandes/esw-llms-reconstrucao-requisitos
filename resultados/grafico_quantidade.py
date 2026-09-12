import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Dados (Tabela de Resultados do relatório)
llms = ["ChatGPT", "DeepSeek", "Gemini", "Claude"]
rf = [23, 16, 11, 14]
rnf = [7, 7, 4, 7]
total = [r + n for r, n in zip(rf, rnf)]

fig, ax = plt.subplots(figsize=(6.0, 3.6))

x = range(len(llms))
bar_rf = ax.bar(x, rf, color="0.35", edgecolor="black", label="Requisitos Funcionais (RF)")
bar_rnf = ax.bar(x, rnf, bottom=rf, color="0.75", edgecolor="black",
                  hatch="///", label="Requisitos Não Funcionais (RNF)")

# Rótulos de valor total no topo de cada barra
for i, t in enumerate(total):
    ax.text(i, t + 0.6, str(t), ha="center", va="bottom", fontsize=10, fontweight="bold")

# Rótulos internos (RF / RNF) em cada segmento
for i, (r, n) in enumerate(zip(rf, rnf)):
    ax.text(i, r / 2, str(r), ha="center", va="center", fontsize=9, color="white")
    ax.text(i, r + n / 2, str(n), ha="center", va="center", fontsize=9, color="black")

ax.set_xticks(list(x))
ax.set_xticklabels(llms, fontsize=11)
ax.set_ylabel("Quantidade de requisitos identificados", fontsize=10)
ax.set_ylim(0, max(total) + 4)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(loc="upper right", fontsize=8, frameon=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color="0.9", linewidth=0.8)

plt.tight_layout()
plt.savefig("grafico-quantidade.pdf")
plt.savefig("grafico-quantidade.png", dpi=200)
print("ok")
