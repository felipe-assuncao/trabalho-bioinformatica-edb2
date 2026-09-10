"""
Algoritmo A: Smith-Waterman (alinhamento local de sequencias).

Fonte: Smith, T.F. & Waterman, M.S. (1981).
"Identification of common molecular subsequences."
Journal of Molecular Biology, 147(1), 195-197.

Problema resolvido: encontrar a melhor sub-regiao de similaridade (alinhamento
local) entre duas sequencias biologicas (ex.: DNA ou proteinas).

Adaptacao para o experimento: a implementacao original permite reconstruir o
alinhamento (traceback). Para o experimento de tempo, mantemos apenas o
preenchimento da matriz de programacao dinamica e o calculo do max_score,
pois e essa etapa (O(m*n)) que domina o custo assintotico do algoritmo; o
traceback custa O(m+n) e nao influencia o crescimento observado.
"""


def alinhamento_local(seq1, seq2, match=2, mismatch=-1, gap=-1):
    m, n = len(seq1), len(seq2)

    # Criacao da matriz de pontuacao preenchida com zeros
    matriz = [[0] * (n + 1) for _ in range(m + 1)]
    max_score = 0

    # Preenchimento da matriz (Programacao Dinamica)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calcula a pontuacao para a diagonal (match ou mismatch)
            if seq1[i - 1] == seq2[j - 1]:
                diagonal = matriz[i - 1][j - 1] + match
            else:
                diagonal = matriz[i - 1][j - 1] + mismatch

            # Calcula a pontuacao para delecao ou insercao (gaps)
            delecao = matriz[i - 1][j] + gap
            insercao = matriz[i][j - 1] + gap

            # O alinhamento local nao aceita valores negativos (reseta para 0)
            matriz[i][j] = max(0, diagonal, delecao, insercao)

            # Rastreia a maior pontuacao encontrada
            if matriz[i][j] > max_score:
                max_score = matriz[i][j]

    return max_score
