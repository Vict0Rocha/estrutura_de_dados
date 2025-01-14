from collections import deque

'''

'''


class Fila:
    def __init__(self):
        self.itens = deque()

    def enfileirar(self, item):
        """ Adiciona um item ao final da fila """
        self.itens.append(item)

    def desenfileirar(self):
        """ Remove e retorna o item do início da fila """
        if self.vazia():
            raise IndexError("A fila está vazia")
        return self.itens.popleft()

    def primeiro(self):
        """ Retorna o primeiro elemento sem removê-lo """
        if self.vazia():
            raise IndexError("A fila está vazia")
        return self.itens[0]

    def vazia(self):
        """ Verifica se a fila está vazia """
        return len(self.itens) == 0

    def tamanho(self):
        """ Retorna o tamanho da fila """
        return len(self.itens)


fila = Fila()
fila.enfileirar("Cliente 1")
fila.enfileirar("Cliente 2")
fila.enfileirar("Cliente 3")

print("Primeiro da fila:", fila.primeiro())  # Saída: Cliente 1
print("Desenfileirando:", fila.desenfileirar())  # Saída: Cliente 1
print("Tamanho da fila:", fila.tamanho())  # Saída: 2
print("Primeiro da fila:", fila.primeiro())  # Saída: Cliente 2
