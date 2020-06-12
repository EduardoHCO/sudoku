def validarLinha(linha, coluna, matriz, valor):
    for i in range(coluna):
        if(matriz[linha][i] == str(valor)):
            return True


def validarColuna(linha, coluna, matriz, valor):
    for i in range(linha):
        if(matriz[i][coluna] == str(valor)):
            return True


def validarQuadrante(matriz, linha, coluna, valor):
    auxLinha = 0
    auxColuna = 0
    if linha < 3:
        auxLinha = 0
    else:
        if linha < 6:
            auxLinha = 3
        else:
            auxLinha = 6
    if coluna < 3:
        auxColuna = 0
    else:
        if coluna < 6:
            auxColuna = 3
        else:
            auxColuna = 6
    for i in range(3):
        for j in range(3):
            if matriz[i+auxLinha][j+auxColuna] == valor:
                print(i+auxLinha)
                print(j+auxColuna)
                return True


def teste():
    tabela = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    print(validarQuadrante(tabela, 4, 4, 2))


print(teste())
