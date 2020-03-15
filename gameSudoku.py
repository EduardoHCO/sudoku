import os
from PIL import Image

listaX = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
listaY = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matriz = []
matrizDeAjuda = []
bloqColor = []
posicBloq = []
xPosicaoValor = -1
yPosicaoValor = -1
valor = 0
condicao = False
ganhou = False
ganhouMesmo = False


f = open("config-teste.txt", "r")
texto = f.readlines()


def lerAquivo():
    for i in range(len(texto)):
        lista = []
        listaAjuda = []
        for c in range(len(texto)):
            lista.append(texto[i][c])
            listaAjuda.append(0)
        # print(lista)
        matriz.append(lista)
        matrizDeAjuda.append(listaAjuda)
    bloqPosic()


def bloqPosic():
    for i in range(9):
        listaAjuda = []
        for c in range(9):
            if(matriz[i][c] != ' '):
                listaAjuda.append(1)
                posicBloq.append(listaX[i]+str(c+1))
            else:
                listaAjuda.append(0)
        bloqColor.append(listaAjuda)


def montarQuadrante():
    x = 3
    y = 3
    ii = 0
    jj = 0
    global xPosicaoValor
    global yPosicaoValor
    global condicao

    for n in range(3):
        for c in range(3):
            for i in range(ii, x):
                for j in range(jj, y):
                    if(xPosicaoValor == i and yPosicaoValor == j):
                        for p in range(ii, x):
                            for q in range(jj, y):
                                if(str(valor) == matriz[p][q]):
                                    matrizDeAjuda[p][q] = 1
                                    condicao = True
                                else:
                                    matrizDeAjuda[p][q] = 0
            ii += 3
            x += 3
        y += 3
        jj += 3
        ii = 0
        x = 3


def validarLinha(linha, coluna, valor):
    for i in range(coluna):
        if(matriz[linha][i] == str(valor)):
            matrizDeAjuda[linha][i] = 1
            return True
        else:
            matrizDeAjuda[linha][i] = 0


def validarColuna(linha, coluna, valor):
    for i in range(linha):
        if(matriz[i][coluna] == str(valor)):
            matrizDeAjuda[i][coluna] = 1
            return True
        else:
            matrizDeAjuda[i][coluna] = 0


def validarErro():
    global ganhou
    for i in matrizDeAjuda:
        if(1 in i):
            ganhou = True
    return ganhou


def validarFinalDeJogo():
    global ganhouMesmo
    if(validarErro() == False):
        for i in range(9):
            for c in range(9):
                if(matriz[i][c] != ' '):
                    ganhouMesmo = True
                else:
                    ganhouMesmo = False
        return ganhouMesmo


def printarMatriz():
    a = ' '
    print(a*5, end="")
    for i in range(len(listaY)-1):
        print(str('\033[95m'+str(listaY[i])+'\033[0;0m')+a*3, end="")
    print(str('\033[95m'+str(listaY[8])+'\033[0;0m'))
    print(a*3, end="")
    print(str(chr(9487)), end="")
    print(str((chr(9473)+chr(9473)+chr(9473)+chr(9523)))*8, end="")
    print(str(chr(9473)+chr(9473)+chr(9473)+chr(9491)))
    for c in range(9):
        print(str('\033[95m'+str(listaX[c])+'\033[0;0m') + a + a, end="")
        print(str(chr(9475)), end="")
        for i in range(9):
            if(i == 8):
                if(matrizDeAjuda[c][i] == 1):
                    print(str(a+'\033[1;31m'+matriz[c]
                              [i]+'\033[0;0m'+a+chr(9475)))
                else:
                    if(bloqColor[c][i]):
                        print(str(a+'\033[1;32m'+matriz[c]
                                  [i]+'\033[0;0m'+a+chr(9475)))
                    else:
                        print(str(a+matriz[c][i]+a+chr(9475)))
            else:
                if(matrizDeAjuda[c][i] == 1):
                    print(str(a+'\033[1;31m'+matriz[c][i] +
                              '\033[0;0m'+a+chr(9475)), end="")
                else:
                    if(bloqColor[c][i]):
                        print(str(a+'\033[1;32m'+matriz[c]
                                  [i]+'\033[0;0m'+a+chr(9475)), end="")
                    else:
                        print(str(a+matriz[c][i]+a+chr(9475)), end="")
        if(c == 8):
            break
        else:
            print(a*3, end="")
            print(str(chr(9507)), end="")
            print(str(chr(9473)+chr(9473)+chr(9473)+chr(9547))*8, end="")
            print(str(chr(9473)+chr(9473)+chr(9473)+chr(9515)))
    print(a*3, end="")
    print(str(chr(9495)), end="")
    print(str(chr(9473)+chr(9473)+chr(9473)+chr(9531))*8, end="")
    print(str(chr(9473)+chr(9473)+chr(9473)+chr(9499)))


def verificarMatriz():
    for i in range(9):
        for c in range(9):
            if(matriz[i][c] == ' '):
                return False


def inputarDados():
    lerAquivo()
    printarMatriz()
    global xPosicaoValor
    global yPosicaoValor
    global valor
    global condicao
    finaliza = False
    while(verificarMatriz() == False):
        print('Escolha uma posição válida: ')
        ent = input()
        for i in range(9):
            for c in range(9):
                if(ent in posicBloq):
                    print(
                        '\033[31m'+'Posição escolhida não pode ser Mudada'+'\033[0;0m')
                    break
                else:
                    if(ent == listaX[i]+str(listaY[c])):
                        print('Insira um número de 1 a 9: ')
                        valor = input()
                        if(int(valor) <= 9 and int(valor) >= 1):
                            xPosicaoValor = i
                            yPosicaoValor = c
                            validarLinha(i, 9, valor)
                            validarColuna(9, c, valor)
                            montarQuadrante()
                            if(validarLinha(i, 9, valor) or validarColuna(9, c, valor)):
                                matrizDeAjuda[i][c] = 1
                            if(condicao):
                                matrizDeAjuda[i][c] = 1
                                condicao = False
                            matriz[i][c] = valor
                            if(validarFinalDeJogo()):
                                os.system('cls')
                                f = open("YES.txt", "r")
                                texto = f.readlines()
                                for i in range(len(texto)):
                                    print(texto[i])
                                finaliza = True
                                break

                        else:
                            print('\033[31m' +
                                  'Número deve ser de 1 a 9'+'\033[0;0m')
                            break
                if(finaliza):
                    break
            if(finaliza):
                break
        if(finaliza):
            break
        printarMatriz()


print(inputarDados())
