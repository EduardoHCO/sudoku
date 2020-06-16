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
                if s[i][j] != " ":
                    self.valores_fixos.append((i, j))


def questionador():
    print('Qual nível deseja jogar?')
    print('1 - Fácil')
    print('2 - Intermediário')
    print('3 - Difícil')
    nivel = input()

    return nivel


def escolher_jogador():
    print('Quem vai jogar?')
    print('1 - Humano')
    print('2 - Agente Inteligente')
    jogador = input()

    return jogador


if(int(questionador()) == 1):
    f = open("nivel11.txt", "r")
    texto = f.readlines()
elif(int(questionador()) == 2):
    f = open("nivel2.txt", "r")
    texto = f.readlines()
elif(int(questionador()) == 3):
    f = open("nivel3.txt", "r")
    texto = f.readlines()
else:
    f = open("nivel1.txt", "r")
    texto = f.readlines()


def lerAquivo():
    matriz = []
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


def preencher_matriz(matriz):
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
            if(estado[linha][i] != " "):
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
            if(numeros_coluna[i] != " "):
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
            if matriz[i][j] != " ":
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


def subida_encosta_repeticoes(quantidade, limite):
    for _ in range(quantidade):
        problema_sudoku = ProblemaSudoku(lerAquivo())
        problema_sudoku.fixar_valores(problema_sudoku.inicial)
        problema_sudoku.inicial = preencher_matriz(problema_sudoku.inicial)
        resultado = subida_encosta(problema_sudoku)
        if problema_sudoku.avaliacao(resultado) <= limite:
            return resultado

    # for estado in estados:
    #     problema.inicial = estado
    #     resultado = subida_encosta(problema)
    #     if problema.avaliacao(resultado) <= limite:
    #         return resultado

    raise LimiteNaoAtingidoError()


class LimiteNaoAtingidoError(Exception):
    pass


def estados_gen(dim, qtde_estados, seed=None):
    import random
    random.seed(seed)

    for _ in range(qtde_estados):
        tabuleiro = list(range(1, dim+1))
        random.shuffle(tabuleiro)
        yield tabuleiro


def feixe_local(quantidade, k):
    estados_iniciais = []

    for _ in range(quantidade):
        problema_sudoku = ProblemaSudoku(lerAquivo())
        problema_sudoku.fixar_valores(problema_sudoku.inicial)
        problema_sudoku.inicial = preencher_matriz(problema_sudoku.inicial)
        estados_iniciais.append(problema_sudoku.inicial)

    avaliacao = problema_sudoku.avaliacao  # alias

    melhores_estados = sorted(estados_iniciais, key=avaliacao)

    while True:
        vizinhos = [problema_sudoku.resultado(estado, acao)
                    for estado in melhores_estados
                    for acao in problema_sudoku.acoes(estado)]
        vizinhos.sort(key=problema_sudoku.avaliacao)
        if avaliacao(vizinhos[0]) < avaliacao(melhores_estados[0]):
            melhores_estados = vizinhos[:k]
        else:
            return melhores_estados[0]


def busca_local_retrocesso(s):
    estado = s
    estado_copia = estado

    pos = posicao_preenchida(estado)
    print(len(pos))

    if pos[0] == 0 and len(pos) == 1:
        return True

    linha = pos[0]
    coluna = pos[1]

    for i in range(1, 10):
        estado_copia[linha][coluna] = str(i)
        printar_matriz(estado_copia)

        if(avaliacao(estado_copia) == 0):
            estado[linha][coluna] = str(i)
            if busca_local_retrocesso(estado):
                return estado
            
        estado_copia[linha][coluna] = " "
        
    return False

def posicao_preenchida(matriz):
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == " ":
                return [i, j]
    return [0]


if __name__ == "__main__":

    # problema_sudoku = ProblemaSudoku(lerAquivo())
    # problema_sudoku.fixar_valores(problema_sudoku.inicial)
    # problema_sudoku.inicial = preencher_matriz()
    # sol = subida_encosta(problema_sudoku)
    # print(printar_matriz(sol), problema_sudoku.avaliacao(sol))

    # Subida de encosta com reinicios, não deterministico por causa da função
    # geradora de estados iniciais
    # try:
    #     sol = subida_encosta_repeticoes(4, 0)
    #     print(sol, ataques_rainhas(sol))
    # except:
    #     pass

    # sol = feixe_local(8, 4)
    # print(sol, avaliacao(sol))
    problema = ProblemaSudoku(lerAquivo())
    sol = busca_local_retrocesso(problema.inicial)
    print(printar_matriz(sol))
    # print(sol)
