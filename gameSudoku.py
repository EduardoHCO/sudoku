import os
from PIL import Image


class Sudoku_Humano():

    def __init__(self):
        self.matriz = []
        self.matriz_ajuda = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], ]
        self.indices = []
        self.texto = ''

    def run(self):
        print('Qual nível deseja jogar?')
        print(' ')
        print('1 - Fácil')
        print('2 - Intermediário')
        print('3 - Difícil')
        nivel = input()
        if(int(nivel) == 1):
            f = open("nivel1.txt", "r")
            self.texto = f.readlines()
        elif(int(nivel) == 2):
            f = open("nivel2.txt", "r")
            self.texto = f.readlines()
        elif(int(nivel) == 3):
            f = open("nivel3.txt", "r")
            self.texto = f.readlines()
        else:
            f = open("nivel1.txt", "r")
            self.texto = f.readlines()

        self.matriz = self.lerAquivo()

        matriz = self.matriz
        posicoes_bloqueadas = self.bloqPosic(matriz, self.matriz_ajuda)
        indice = self.guardar_indices()
        erro = ''

        while(self.is_Fim(self.matriz_ajuda) == False):
            os.system('cls')
            print(str('\033[1;31m' +
                      erro+'\033[0;0m'))
            self.printar_matriz(matriz, self.matriz_ajuda)
            print()
            dado = self.inputar_dado()
            if dado in indice:
                dado = dado[0]-1, dado[1]-1
                if dado not in posicoes_bloqueadas:
                    print('Insira um número de 1 a 9: ')
                    valor = input()
                    if int(valor) >= 1 and int(valor) <= 9:
                        linha, coluna = dado[0], dado[1]
                        matriz[linha][coluna] = valor
                        self.validar_linha(
                            linha, valor, matriz, self.matriz_ajuda)
                        self.validar_coluna(coluna, valor, matriz,
                                            self.matriz_ajuda)
                        self.validarQuadrante(matriz, linha, coluna,
                                              valor, self.matriz_ajuda)
                        erro = ''
                    else:
                        erro = 'Coloque um número válido entre 1 e 9'
                else:
                    erro = 'Não é possível modificar esse número'
            else:
                erro = 'Coloque uma posição válida'
        os.system('cls')
        print('PARABÉNS VOCÊ GANHOU !!!!!!!!!!!!!!!!!!!!!!!!!!')

    def inputar_dado(self):
        print('Qual linha?')
        linha = input()
        print('Qual coluna?')
        coluna = input()

        return (int(linha), int(coluna))

    def lerAquivo(self):
        matriz = []
        for i in range(len(self.texto)):
            lista = []
            listaAjuda = []
            for c in range(len(self.texto)):
                lista.append(self.texto[i][c])
                listaAjuda.append(0)
            matriz.append(lista)
        return matriz

    def is_Fim(self, matriz):
        for i in range(9):
            for j in range(9):
                if matriz[i][j] == 1:
                    return False

    def bloqPosic(self, matriz, matriz_ajuda):
        posicao_bloqueada = []
        for i in range(9):
            for j in range(9):
                if matriz[i][j] != ' ':
                    posicao_bloqueada.append((i, j))
                else:
                    matriz_ajuda[i][j] = 1
        return posicao_bloqueada

    def validarQuadrante(self, matriz, linha, coluna, valor, matriz_ajuda):
        auxLinha = 0
        auxColuna = 0
        conflitos = False
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
                    matriz_ajuda[i+auxLinha][j+auxColuna] = 1
                    conflitos = True

        return conflitos

    def printar_matriz(self, matriz, matriz_ajuda):
        for i in range(9):
            if i == 0:
                print("  " + str('\033[95m'+str(i+1)+'\033[0;0m'), end="")
            elif i < 8:
                print(" " + str('\033[95m'+str(i+1)+'\033[0;0m'), end="")
            else:
                print(" " + str('\033[95m'+str(i+1)+'\033[0;0m'))

        for i in range(9):
            if i == 3:
                print("  –––––+–––––+–––––")
            if i == 6:
                print("  –––––+–––––+–––––")
            for j in range(9):
                if j == 0:
                    if matriz_ajuda[i][j] == 0:
                        print(str('\033[95m'+str(i+1)+'\033[0;0m'),
                              matriz[i][j], end="")
                    else:
                        print(str('\033[95m'+str(i+1)+'\033[0;0m'),
                              str('\033[1;31m'+matriz[i][j]+'\033[0;0m'), end="")
                elif j == 3:
                    if matriz_ajuda[i][j] == 0:
                        print("|" + matriz[i][j], end="")
                    else:
                        print("|" + str('\033[1;31m' +
                                        matriz[i][j]+'\033[0;0m'), end="")
                elif j == 6:
                    if matriz_ajuda[i][j] == 0:
                        print("|" + matriz[i][j], end="")
                    else:
                        print("|" + str('\033[1;31m' +
                                        matriz[i][j]+'\033[0;0m'), end="")

                elif j == 8:
                    if matriz_ajuda[i][j] == 0:
                        print(" " + matriz[i][j] + " ")
                    else:
                        print(" " + str('\033[1;31m' +
                                        matriz[i][j]+'\033[0;0m') + " ")
                else:
                    if matriz_ajuda[i][j] == 0:
                        print(" " + matriz[i][j], end="")
                    else:
                        print(" " + str('\033[1;31m' +
                                        matriz[i][j]+'\033[0;0m'), end="")

    def validar_coluna(self, coluna, valor, matriz, matriz_ajuda):
        for i in range(9):
            if(matriz[i][coluna] == str(valor)):
                matriz_ajuda[i][coluna] = 1
                return True

    def guardar_indices(self):
        indices = []
        for i in range(9):
            for j in range(9):
                indices.append((i+1, j+1))
        return indices

    def validar_linha(self, linha, valor, matriz, matriz_ajuda):
        for i in range(9):
            if(matriz[linha][i] == str(valor)):
                matriz_ajuda[linha][i] = 1
                return True
