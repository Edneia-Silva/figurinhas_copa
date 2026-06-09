# Importa os nós e a entidade do arquivo estruturas.py
from estruturas import Figurinha, NodoLista, NodoFila

class Album:
    def __init__(self):
        self._cabeca = None
        self._tamanho = 0
        self.total_album = 100

    def adicionar(self, figurinha):
        novo_nodo = NodoLista(figurinha)
        if self._cabeca is None:
            self._cabeca = novo_nodo
            self._tamanho += 1
            return True
            
        atual = self._cabeca
        anterior = None
        while atual is not None:
            if atual.figurinha.id == figurinha.id:
                return False  # Repetida!
            anterior = atual
            atual = atual.proximo
            
        anterior.proximo = novo_nodo
        self._tamanho += 1
        return True

    def remover(self, id_fig):
        atual = self._cabeca
        anterior = None
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
        while atual is not None:
            f = atual.figurinha
            print(f"ID: {f.id} | {f.nome} | {f.pais} | {f.posicao} | {f.raridade}")
            atual = atual.proximo

    def calcular_porcentagem(self):
        porcentagem = (self._tamanho / self.total_album) * 100
        return round(porcentagem, 2)


class Fila:
    def __init__(self):
        self._inicio = None
        self._fim = None

    def enqueue(self, figurinha):
        novo_nodo = NodoFila(figurinha)
        if self._fim is None:
            self._inicio = novo_nodo
            self._fim = novo_nodo
        else:
            self._fim.proximo = novo_nodo
            self._fim = novo_nodo

    def dequeue(self):
        if self._inicio is None:
            return None
        removido = self._inicio.figurinha
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        return removido

    def peek(self):
        if self._inicio is None:
            return None
        return self._inicio.figurinha

    def exibir_fila(self):
        if self._inicio is None:
            print("Nenhuma figurinha aqui.")
            return
        atual = self._inicio
        while atual is not None:
            f = atual.figurinha
            print(f"-> [{f.id}] {f.nome} - {f.pais}")
            atual = atual.proximo

    def contar_elementos(self):
        contador = 0
        atual = self._inicio
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador