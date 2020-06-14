import random


class ProblemaSudoku():

    def __init__(self, s):
        self.inicial = s
        self.valores_fixos = []

    def acoes(self, s):
        acoes_possiveis = []

        for i in range(9):
            for j in range(9):
                if (i, j) not in self.valores_fixos:
                    acoes_possiveis.append((i, j))
        return acoes_possiveis

    @staticmethod
    def resultado(s, a):
        pos, mov = a
        aleatorio = random.randint(1, 9)

        while s[pos][mov] == str(aleatorio):
            aleatorio = random.randint(1, 9)

        s[pos][mov] = str(aleatorio)

        return s

        # return [rainha + (0 if pos != id else mov)
        #         for id, rainha in enumerate(s)]

    @staticmethod
    def objetivo(s):
        if avaliacao(s) == 0:
            return True

    @staticmethod
    def custo(s, a, sl):
        return 1

    @classmethod
    def heuristica(cls, no):
        return cls.avaliacao(no.s)

    @staticmethod
    def avaliacao(s):
        return avaliacao(s)

    def fixar_valores(self, s):
        for i in range(9):
            for j in range(9):
                if matriz[i][j] != " ":
                    self.valores_fixos.append((i, j))


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


def lerAquivo():
    for i in range(len(texto)):
        lista = []
        listaAjuda = []
        for c in range(len(texto)):
            lista.append(texto[i][c])
            listaAjuda.append(0)
        # print(lista)
        matriz.append(lista)
    return matriz


def printar_matriz(matriz):
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
    for k in range(3):
        for l in range(3):
            if(k+auxi != i and l+auxj != j):
                if matriz[i][j] == matriz[k+auxi][l+auxj]:
                    contador += 1
    return contador


def validarQuadrante(matriz):
    contador = 0
    for n in range(0, 9, 3):
        for m in range(0, 9, 3):
            for i in range(n, n+3):
                contQuadrante = 0
                for j in range(m, m+3):
                    contQuadrante += validarDiagonais(matriz, i, j)
                contador += (contQuadrante/2)
    return int(contador)


def subida_encosta(problema):
    ''' s é o estado inicial, problema é o gerador e avaliacao é uma funcao
    de avaliação, onde avaliacao(s) == 0 é a solução ótima. Sempre retorna uma
    solução, mas não é ótimo.
    '''
    melhor = problema.inicial
    while True:
        vizinhos = (problema.resultado(melhor, acao)
                    for acao in problema.acoes(melhor))
        melhor_vizinho = min(vizinhos, key=problema.avaliacao)
        if problema.avaliacao(melhor_vizinho) < problema.avaliacao(melhor):
            melhor = melhor_vizinho
        else:
            return melhor


def subida_encosta_repeticoes(problema, estados, limite):
    problema_sudoku = ProblemaSudoku(lerAquivo())
    problema_sudoku.fixar_valores(problema_sudoku.inicial)
    problema_sudoku.inicial = preencher_matriz()
    for estado in estados:
        problema.inicial = estado
        resultado = subida_encosta(problema)
        if problema.avaliacao(resultado) <= limite:
            return resultado

    raise LimiteNaoAtingidoError()


class LimiteNaoAtingidoError(Exception):
    pass


if __name__ == "__main__":
    problema_sudoku = ProblemaSudoku(lerAquivo())
    problema_sudoku.fixar_valores(problema_sudoku.inicial)
    problema_sudoku.inicial = preencher_matriz()
    # sol = subida_encosta(problema_sudoku)
    # print(printar_matriz(sol), problema_sudoku.avaliacao(sol))

    # Subida de encosta com reinicios, não deterministico por causa da função
    # geradora de estados iniciais
    try:
        sol = subida_encosta_repeticoes(
            ProblemaRainhas([None]*8),
            estados_gen(8, 8, 'r'),
            0)
        print(sol, ataques_rainhas(sol))
    except:
        pass

    # sol = feixe_local(
    #     ProblemaRainhas([None]*8),
    #     estados_gen(8, 8, 'r'))
    # print(sol, ataques_rainhas(sol))
