class Figurinha:
    def __init__(self, id_fig, nome, pais, posicao, raridade):
        self.id = int(id_fig)
        self.nome = str(nome)
        self.pais = str(pais)
        self.posicao = str(posicao)
        self.raridade = str(raridade)

class NodoLista:
    def __init__(self, figurinha):
        self.figurinha = figurinha
        self.proximo = None

class NodoFila:
    def __init__(self, figurinha):
        self.figurinha = figurinha
        self.proximo = None