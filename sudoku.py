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
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == " ":
                aleatorio = random.randint(1, 9)
                matriz[i][j] = str(aleatorio)
                numeros_gerados = aleatorio
    printar_matriz()


def avaliacao(estado):
    somatoria = 0
    for i in range(9):
        somatoria += validar_linha(i, estado) + validar_coluna(i, estado)
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


# def validar_quadrante(estado, quadrante):
#     for i in range(3):
#         for j in range(3):
#             if estado[]


lerAquivo()
printar_matriz()
fixar_valores()
preencher_matriz()
print(avaliacao(matriz))
