import random
print('Qual nível deseja jogar?')
print(' ')
print('1 - Fácil')
print('2 - Intermediário')
print('3 - Difícil')
nivel = input()
if(int(nivel) == 1):
    f = open("nivel1.txt", "r")
    texto = f.readlines()
elif(int(nivel) == 2):
    f = open("nivel2.txt", "r")
    texto = f.readlines()
elif(int(nivel) == 3):
    f = open("nivel3.txt", "r")
    texto = f.readlines()
else:
    f = open("nivel1.txt", "r")
    texto = f.readlines()

matriz = []
numeros_gerados = []
valores_fixos = []


def lerAquivo():
    for i in range(len(texto)):
        lista = []
        listaAjuda = []
        for c in range(len(texto)):
            lista.append(texto[i][c])
            listaAjuda.append(0)
        # print(lista)
        matriz.append(lista)


def fixar_valores():
    for i in range(9):
        for j in range(9):
            if matriz[i][j] != " ":
                valores_fixos.append([matriz[i][j], i, j])
    print(valores_fixos)


def printar_matriz():
    for i in range(9):
        for j in range(9):
            if j == 0:
                print(matriz[i][j], end="")
            elif j == 8:
                print(" " + matriz[i][j] + " ")
            else:
                print(" " + matriz[i][j], end="")


def preencher_matriz():
    lerAquivo()
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == " ":
                aleatorio = random.randint(1, 9)
                matriz[i][j] = str(aleatorio)
    return matriz


def avaliacao(estado):
    somatoria = 0
    for i in range(9):
        somatoria += validar_linha(i, estado) + validar_coluna(i, estado)
    somatoria += validarQuadrante(estado)
    return somatoria


def validar_linha(linha, estado):
    conflitos = 0
    for i in range(len(estado[linha])):
        for j in estado[linha][i+1:]:
            if(estado[linha][i] == j):
                conflitos += 1
    return conflitos


def validar_coluna(coluna, estado):
    numeros_coluna = []
    conflitos = 0

    for i in range(len(estado[coluna])):
        numeros_coluna.append(estado[i][coluna])

    for i in range(len(numeros_coluna)):
        for j in numeros_coluna[i+1:]:
            if(numeros_coluna[i] == j):
                conflitos += 1
    return conflitos


def validarDiagonais(matriz, i, j):
    auxi = 0
    auxj = 0
    if i < 3:
        auxi = 0
    else:
        if i < 6:
            auxi = 3
        else:
            auxi = 6
    if j < 3:
        auxj = 0
    else:
        if j < 6:
            auxj = 3
        else:
            auxj = 6
    contador = 0
    print('j: ' + str(j))
    for k in range(3):
        for l in range(3):
            if(k+auxi != i and l+auxj != j):
                if matriz[i][j] == matriz[k+auxi][l+auxj]:
                    print('Numero para comparar: ' + str(
                        matriz[i][j]) + ' posicao número encontrado: ' + str(k+auxi), str(l+auxj))
                    contador += 1
    return contador


def validarQuadrante(matriz):
    print(printar_matriz())
    contador = 0
    for n in range(0, 9, 3):
        for m in range(0, 9, 3):
            for i in range(n, n+3):
                contQuadrante = 0
                for j in range(m, m+3):
                    print('J ****:' + str(j))
                    contQuadrante += validarDiagonais(matriz, i, j)
                    print('CONTADOR ------- : ' + str(contQuadrante))
                contador += (contQuadrante/2)
            print('QUANTO DEU O QUADRANTE: ' + str(contador))
    return int(contador)


# lerAquivo()
# printar_matriz()
# fixar_valores()
# preencher_matriz()
# print(avaliacao(matriz))

print(validarQuadrante(preencher_matriz()))
