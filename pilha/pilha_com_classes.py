'''
Exemplo 2: Pilha como uma classe
'''


class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        # Adiciona um item ao topo da pilha.
        self.itens.append(item)

    def desempilhar(self):
        #  Remove e retorna o item do topo da pilha.
        if self.vazia():
            raise IndexError("A pilha está vazia")
        return self.itens.pop()

    def topo(self):
        # Retorna o item do topo sem removê-lo.
        if self.vazia():
            raise IndexError("A pilha está vazia")
        return self.itens[-1]

    def vazia(self):
        #  Verifica se a pilha está vazia.
        return len(self.itens) == 0


if __name__ == "__main__":
    minha_pilha = Pilha()
    minha_pilha.empilhar(5)
    minha_pilha.empilhar(15)
    print("Topo da pilha:", minha_pilha.topo())  # Saída: Topo da pilha: 15
    minha_pilha.desempilhar()
    print("Topo da pilha após desempilhar:", minha_pilha.topo())  # Saída: 5
