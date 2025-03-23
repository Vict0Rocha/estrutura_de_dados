class NoBST:
    """
    Classe que representa um nó na Árvore Binária de Busca (BST).
    """

    def __init__(self, chave):
        self.chave = chave  # Valor armazenado no nó
        self.esquerda = None  # Filho à esquerda
        self.direita = None  # Filho à direita


class ArvoreBST:
    """
    Implementação de uma Árvore Binária de Busca.
    """

    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        """Insere um novo nó na árvore."""
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if no is None:
            return NoBST(chave)
        if chave < no.chave:
            no.esquerda = self._inserir_recursivo(no.esquerda, chave)
        else:
            no.direita = self._inserir_recursivo(no.direita, chave)
        return no

    def buscar(self, chave):
        """Busca um nó na árvore pelo valor da chave."""
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no, chave):
        if no is None or no.chave == chave:
            return no
        if chave < no.chave:
            return self._buscar_recursivo(no.esquerda, chave)
        return self._buscar_recursivo(no.direita, chave)

    def remover(self, chave):
        """Remove um nó da árvore pelo valor da chave."""
        self.raiz = self._remover_recursivo(self.raiz, chave)

    def _remover_recursivo(self, no, chave):
        if no is None:
            return no
        if chave < no.chave:
            no.esquerda = self._remover_recursivo(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover_recursivo(no.direita, chave)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            temp = self._encontrar_minimo(no.direita)
            no.chave = temp.chave
            no.direita = self._remover_recursivo(no.direita, temp.chave)
        return no

    def _encontrar_minimo(self, no):
        """Encontra o nó com o menor valor na árvore."""
        while no.esquerda is not None:
            no = no.esquerda
        return no

    def exibir_em_ordem(self):
        """Exibe os valores da árvore em ordem crescente."""
        self._exibir_em_ordem_recursivo(self.raiz)
        print()

    def _exibir_em_ordem_recursivo(self, no):
        if no is not None:
            self._exibir_em_ordem_recursivo(no.esquerda)
            print(no.chave, end=" ")
            self._exibir_em_ordem_recursivo(no.direita)


if __name__ == "__main__":
    # Exemplo de uso da Árvore BST
    arvore = ArvoreBST()
    arvore.inserir(50)
    arvore.inserir(30)
    arvore.inserir(70)
    arvore.inserir(20)
    arvore.inserir(40)
    arvore.inserir(60)
    arvore.inserir(80)

    print("Árvore em ordem crescente.")
    arvore.exibir_em_ordem()
    print(30*'-')

    # Buscando um valor
    busca = 40
    no_encontrado = arvore.buscar(busca)
    print(
        f"Nó {busca} encontrado." if no_encontrado else f"Nó {busca} não encontrado.")
    print(30*'-')

    # Removendo um nó
    arvore.remover(50)
    print("Árvore após remover 50.")
    arvore.exibir_em_ordem()
