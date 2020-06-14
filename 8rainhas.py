class ProblemaRainhas():

    def __init__(self, s):
        self.inicial = s

    @staticmethod
    def acoes(s):
        return [(id, nova_pos - rainha_pos)
                for id, rainha_pos in enumerate(s)
                for nova_pos in range(1, 9)
                if nova_pos != id]

    @staticmethod
    def resultado(s, a):
        pos, mov = a

        return [rainha + (0 if pos != id else mov)
                for id, rainha in enumerate(s)]

    @staticmethod
    def objetivo(s):
        if ataques_rainhas(s) == 0:
            return True

    @staticmethod
    def custo(s, a, sl):
        return 1

    @classmethod
    def heuristica(cls, no):
        return cls.avaliacao(no.s)

    @staticmethod
    def avaliacao(s):
        return ataques_rainhas(s)


def ataques_rainhas(s):
    ''' s é uma lista de inteiros entre 1 e len(s)
    '''
    return sum(1
               for i, rainha in enumerate(s, 1)
               for dist, alvo in enumerate(s[i:], 1)
               if alvo - rainha == 0 or abs(alvo - rainha) == dist)


def estados_gen(dim, qtde_estados, seed=None):
    import random
    random.seed(seed)

    for _ in range(qtde_estados):
        tabuleiro = list(range(1, dim+1))
        random.shuffle(tabuleiro)
        yield tabuleiro


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
    for estado in estados:
        problema.inicial = estado
        resultado = subida_encosta(problema)
        if problema.avaliacao(resultado) <= limite:
            return resultado

    raise LimiteNaoAtingidoError()

# Excessões desse pacote


class LimiteNaoAtingidoError(Exception):
    pass


def feixe_local(problema, estados_iniciais):
    avaliacao = problema.avaliacao  # alias

    melhores_estados = sorted(estados_iniciais, key=avaliacao)
    k = len(melhores_estados)
    while True:
        vizinhos = [problema.resultado(estado, acao)
                    for estado in melhores_estados
                    for acao in problema.acoes(estado)]
        vizinhos.sort(key=problema.avaliacao)
        if avaliacao(vizinhos[0]) < avaliacao(melhores_estados[0]):
            melhores_estados = vizinhos[:k]
        else:
            return melhores_estados[0]


if __name__ == "__main__":
    # Subida de encosta simples, para um único caso, determinístico
    sol = subida_encosta(ProblemaRainhas([2, 3, 1, 4, 8, 6, 5, 7]))
    print(sol, ataques_rainhas(sol))

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
