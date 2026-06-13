from estruturas import NodoLista

class Album:
    def __init__(self):
        self._cabeca = None
        self._tamanho = 0
        self.total_album = 100  # Tamanho estimado para calcular a % 

    def adicionar(self, figurinha):
        novo_nodo = NodoLista(figurinha)
        if self._cabeca is None:
            self._cabeca = novo_nodo
            self._tamanho += 1
            return True
            
        atual = self._cabeca
        anterior = None
        while atual is not None:
            # Validação: se o ID informado já existir no álbum, o sistema barra
            if atual.figurinha.id == figurinha.id:
                return False  # Já tem no álbum, então é repetida! 
            anterior = atual
            atual = atual.proximo
            
        anterior.proximo = novo_nodo
        # Incrementa o contador de figurinhas coladas no álbum
        self._tamanho += 1
        return True

    def remover(self, id_fig):
        atual = self._cabeca
        anterior = None
        # Percore a Lista Encadeada em busca do ID da figurinha a ser removida
        while atual is not None:
            if atual.figurinha.id == id_fig:
                if anterior is None:
                    self._cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def buscar_por_id(self, id_fig):
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.id == id_fig:
                return atual.figurinha
            atual = atual.proximo
        return None

    def buscar_por_jogador(self, nome_jogador):
        atual = self._cabeca
        encontrou = False
        while atual is not None:
            # O operador "in" permite achar o jogador digitando apenas parte do nome
            if nome_jogador.lower() in atual.figurinha.nome.lower():
                print(f"-> [{atual.figurinha.id}] {atual.figurinha.nome} - {atual.figurinha.pais}")
                encontrou = True
            atual = atual.proximo
        if not encontrou:
            print("Nenhum jogador encontrado.")

    def buscar_por_selecao(self, nome_pais):
        atual = self._cabeca
        encontrou = False
        while atual is not None:
            if nome_pais.lower() == atual.figurinha.pais.lower():
                print(f"-> [{atual.figurinha.id}] {atual.figurinha.nome} ({atual.figurinha.raridade})")
                encontrou = True
            atual = atual.proximo
        if not encontrou:
            print("Nenhuma figurinha encontrada para essa seleção.")

    def exibir_album(self):
        if self._cabeca is None:
            print("\nSeu álbum está completamente vazio!")
            return
        atual = self._cabeca
        print("\n--- FIGURINHAS COLADAS NO ÁLBUM ---")
        # Percoree a lista e exibe os dados de cada figurinha
        while atual is not None:
            f = atual.figurinha
            print(f"ID: {f.id} | {f.nome} | {f.pais} | {f.posicao} | {f.raridade}")
            atual = atual.proximo

    def calcular_porcentagem(self):
        porcentagem = (self._tamanho / self.total_album) * 100
        return round(porcentagem, 2)