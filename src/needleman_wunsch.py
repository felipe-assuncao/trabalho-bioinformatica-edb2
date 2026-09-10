"""
Algoritmo B: Needleman-Wunsch (alinhamento global de sequencias).

Fonte: Needleman, S.B. & Wunsch, C.D. (1970).
"A general method applicable to the search for similarities in the amino
acid sequence of two proteins."
Journal of Molecular Biology, 48(3), 443-453.

Problema resolvido: encontrar o melhor alinhamento considerando as
sequencias inteiras de ponta a ponta (alinhamento global), diferente do
Smith-Waterman, que busca apenas a melhor sub-regiao local.

Adaptacao para o experimento: assim como no Smith-Waterman, mantemos apenas
o preenchimento da matriz de programacao dinamica e o calculo da pontuacao
final (canto inferior direito), sem o traceback, para isolar o custo
O(m*n) que e o alvo da comparacao de crescimento.
"""


def alinhamento_global(seq1, seq2, match=2, mismatch=-1, gap=-1):
    m, n = len(seq1), len(seq2)

    # Criacao da matriz de pontuacao, com a primeira linha/coluna
    # inicializadas com a penalidade acumulada de gap (diferenca chave
    # em relacao ao Smith-Waterman, que zera a matriz)
    matriz = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        matriz[i][0] = matriz[i - 1][0] + gap
    for j in range(1, n + 1):
        matriz[0][j] = matriz[0][j - 1] + gap

    # Preenchimento da matriz (Programacao Dinamica)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                diagonal = matriz[i - 1][j - 1] + match
            else:
                diagonal = matriz[i - 1][j - 1] + mismatch

            delecao = matriz[i - 1][j] + gap
            insercao = matriz[i][j - 1] + gap

            # Alinhamento global nao reseta para 0: valores negativos sao permitidos
            matriz[i][j] = max(diagonal, delecao, insercao)

    # A pontuacao do alinhamento global e o valor no canto inferior direito
    return matriz[m][n]
