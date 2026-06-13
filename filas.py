from estruturas import NodoFila

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
        # Guarda dos dados da figurinha que está saindo (a primeira do início)
        removido = self._inicio.figurinha
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        return removido

    def peek(self):
        # Apenas espia quem está no início da fila das repetidas, sem remover.
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
        # Retorna a quantidade total de elementos que estavam na fila.
        return contador