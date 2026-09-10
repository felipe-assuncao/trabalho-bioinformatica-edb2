"""
Script de experimento: mede o tempo de execucao do Smith-Waterman (local) e
do Needleman-Wunsch (global) para sequencias de DNA de tamanho n crescente.

Definicao de n: n = comprimento de cada uma das duas sequencias de entrada,
que sao geradas com o mesmo tamanho (m = n) sobre o alfabeto {A, C, G, T}.

Metodologia:
  - Para cada n, geram-se REPETICOES pares de sequencias aleatorias novas
    (para evitar viés de uma unica instancia).
  - A geracao das sequencias NAO entra no tempo medido (nao faz parte do
    algoritmo).
  - Mede-se o tempo de cada execucao com time.perf_counter() e calcula-se a
    media e o desvio padrao.
  - Resultados sao salvos em data/resultados.csv.
"""

import csv
import random
import statistics
import time
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from smith_waterman import alinhamento_local
from needleman_wunsch import alinhamento_global

ALFABETO = "ACGT"
TAMANHOS_N = [50, 100, 200, 400, 800, 1200, 1600, 2000]
REPETICOES = 8
SEED = 42


def gerar_sequencia(tamanho, rng):
    return "".join(rng.choice(ALFABETO) for _ in range(tamanho))


def medir(algoritmo, seq1, seq2):
    inicio = time.perf_counter()
    algoritmo(seq1, seq2)
    fim = time.perf_counter()
    return fim - inicio


def rodar_experimento():
    rng = random.Random(SEED)
    algoritmos = {
        "Smith-Waterman (local)": alinhamento_local,
        "Needleman-Wunsch (global)": alinhamento_global,
    }

    linhas = []
    for n in TAMANHOS_N:
        tempos = {nome: [] for nome in algoritmos}

        for _ in range(REPETICOES):
            seq1 = gerar_sequencia(n, rng)
            seq2 = gerar_sequencia(n, rng)

            for nome, func in algoritmos.items():
                dt = medir(func, seq1, seq2)
                tempos[nome].append(dt)

        for nome, valores in tempos.items():
            media = statistics.mean(valores)
            desvio = statistics.stdev(valores) if len(valores) > 1 else 0.0
            linhas.append({
                "algoritmo": nome,
                "n": n,
                "tempo_medio_s": media,
                "desvio_padrao_s": desvio,
                "repeticoes": REPETICOES,
            })
            print(f"{nome:28s} n={n:5d}  tempo_medio={media:.6f}s  desvio={desvio:.6f}s")

    caminho_saida = os.path.join(os.path.dirname(__file__), "..", "data", "resultados.csv")
    with open(caminho_saida, "w", newline="", encoding="utf-8") as f:
        campos = ["algoritmo", "n", "tempo_medio_s", "desvio_padrao_s", "repeticoes"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(linhas)

    print(f"\nResultados salvos em: {os.path.abspath(caminho_saida)}")


if __name__ == "__main__":
    rodar_experimento()
