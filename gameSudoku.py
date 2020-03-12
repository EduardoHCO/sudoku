import os

listaX = ['a','b','c','d','e','f','g','h','i','j']
listaY = [1,2,3,4,5,6,7,8,9]
matriz = []
matrizDeAjuda = []
posicBloq = []
listaQuadrantes = []

f = open("demofile.txt", "r")
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
        for c in range(9):
            if(matriz[i][c] != ' '):
                posicBloq.append(listaX[i]+str(c+1))

def validarQuadrante():
    x = 3
    y = 3
    ii = 0
    jj = 0

    for n in range(3):
        for c in range(3):
            quadrante = []
            for i in range(ii, x):
                for j in range(jj, y):
                    quadrante.append(matriz[i][j])
            listaQuadrantes.append(quadrante)
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

# def validarQuadrante(linha, coluna):
    
    

def printarMatriz():
    a = ' '
    print(a*5, end="")
    for i in range(len(listaY)-1):
        print(str('\033[95m'+str(listaY[i])+'\033[0;0m')+a*3, end="")
    print(str('\033[95m'+str(listaY[8])+'\033[0;0m'))
    print(a*3, end="")
    print(str(chr(9487)), end="")
    print(str((chr(9473)+chr(9473)+chr(9473)+chr(9523)))*9)
    for c in range(9):
        print(listaX[c] + a + a, end="")
        print(str(chr(9475)), end="")
        for i in range(9):
            if(i == 8):
                if(matrizDeAjuda[c][i] == 1): 
                    print(str(a+'\033[31m'+matriz[c][i]+'\033[0;0m'+a+chr(9475)))
                else:
                    print(str(a+matriz[c][i]+a+chr(9475)))
            else: 
                if(matrizDeAjuda[c][i] == 1):
                    print(str(a+'\033[31m'+matriz[c][i]+'\033[0;0m'+a+chr(9475)), end="")
                else:
                    print(str(a+matriz[c][i]+a+chr(9475)), end="")
        if(c == 8):
            break
        else:
            print(a*3, end="")
            print(str(chr(9507)), end="")
            print(str(chr(9473)+chr(9473)+chr(9473)+chr(9547))*9)
    print(a*3, end="")
    print(str(chr(9495)), end="") 
    print(str(chr(9473)+chr(9473)+chr(9473)+chr(9499))*9)
    
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
    while(verificarMatriz() == False):
        print('Escolha uma posição válida: ')
        ent = input()
        for i in range(9):
            for c in range(9):
                if(ent in posicBloq):
                    print('\033[31m'+'Posição escolhida não pode ser Mudada'+'\033[0;0m')
                    break
                else:
                    if(ent == listaX[i]+str(listaY[c])):
                        print('Insira um número de 1 a 9: ')
                        valor = input()
                        if(int(valor) <= 9 and int(valor) >= 1):
                            validarLinha(i,9,valor)
                            validarColuna(9,c,valor)
                            if(validarLinha(i,9,valor) or validarColuna(9,c,valor)):
                                matrizDeAjuda[i][c] = 1
                            xPosicaoValor = i
                            yPosicaoValor = c
                            matriz[i][c] = valor
                            print(matrizDeAjuda)
                            
                        else:
                            print('Número deve ser entre 1 e 9')
                            break                   
        # os.system('cls')    
        printarMatriz()
 
print(inputarDados())



