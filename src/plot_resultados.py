"""
Gera os dois graficos obrigatorios do trabalho a partir de data/resultados.csv:

  1. figuras/grafico1_tempo_x_n.png
     Tempo de execucao x tamanho da entrada n, para cada algoritmo.

  2. figuras/grafico2_empirico_x_teorico.png
     Comparacao do crescimento empirico com a funcao de crescimento
     esperada (O(n^2)), ajustada por minimos quadrados (c * n^2).
"""

import csv
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "..", "data", "resultados.csv")
FIG_DIR = os.path.join(BASE_DIR, "..", "figuras")
os.makedirs(FIG_DIR, exist_ok=True)


def carregar_dados():
    dados = {}
    with open(CSV_PATH, encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            alg = linha["algoritmo"]
            dados.setdefault(alg, {"n": [], "tempo": [], "desvio": []})
            dados[alg]["n"].append(int(linha["n"]))
            dados[alg]["tempo"].append(float(linha["tempo_medio_s"]))
            dados[alg]["desvio"].append(float(linha["desvio_padrao_s"]))
    return dados


def grafico1_tempo_x_n(dados):
    plt.figure(figsize=(8, 5.5))
    for alg, serie in dados.items():
        plt.errorbar(
            serie["n"], serie["tempo"], yerr=serie["desvio"],
            marker="o", capsize=3, label=alg,
        )
    plt.xlabel("Tamanho da entrada (n = comprimento de cada sequencia)")
    plt.ylabel("Tempo medio de execucao (s)")
    plt.title("Tempo de execucao x tamanho da entrada n")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    caminho = os.path.join(FIG_DIR, "grafico1_tempo_x_n.png")
    plt.savefig(caminho, dpi=150)
    plt.close()
    print(f"Salvo: {caminho}")


def grafico2_empirico_x_teorico(dados):
    fig, eixos = plt.subplots(1, len(dados), figsize=(6 * len(dados), 5), squeeze=False)
    eixos = eixos[0]

    for eixo, (alg, serie) in zip(eixos, dados.items()):
        n = np.array(serie["n"], dtype=float)
        t = np.array(serie["tempo"], dtype=float)

        # Ajuste por minimos quadrados de t = c * n^2 (modelo teorico O(n^2))
        c = np.sum(t * n ** 2) / np.sum(n ** 4)
        n_suave = np.linspace(n.min(), n.max(), 200)
        t_teorico = c * n_suave ** 2

        eixo.plot(n, t, "o", label="Tempo observado (experimental)")
        eixo.plot(n_suave, t_teorico, "--", label=f"Curva teorica c*n^2 (c={c:.3e})")
        eixo.set_xlabel("Tamanho da entrada n")
        eixo.set_ylabel("Tempo (s)")
        eixo.set_title(alg)
        eixo.legend()
        eixo.grid(True, alpha=0.3)

    fig.suptitle("Crescimento empirico x crescimento teorico esperado O(n^2)")
    fig.tight_layout()
    caminho = os.path.join(FIG_DIR, "grafico2_empirico_x_teorico.png")
    fig.savefig(caminho, dpi=150)
    plt.close(fig)
    print(f"Salvo: {caminho}")


if __name__ == "__main__":
    dados = carregar_dados()
    grafico1_tempo_x_n(dados)
    grafico2_empirico_x_teorico(dados)
