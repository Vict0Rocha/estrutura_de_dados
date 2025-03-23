""""
Estrutura de uma empresa com departamentos e funcionários.
"""


class No:
    """
    Representa um nó em uma árvore .
    """

    def __init__(self, dado):
        self.dado = dado  # Valor armazenado no nó
        self.filhos = []  # Lista de filhos do nó

    def adicionar_filho(self, filho):
        """Adiciona um novo filho ao nó atual."""
        self.filhos.append(filho)

    def remover_filho(self, dado):
        """Remove um filho com um determinado valor."""
        for filho in self.filhos:
            if filho.dado == dado:
                self.filhos.remove(filho)
                return True
        return False

    def buscar(self, dado):
        """Busca um nó com o valor especificado na árvore."""
        if self.dado == dado:
            return self
        for filho in self.filhos:
            resultado = filho.buscar(dado)
            if resultado:
                return resultado

        return None

    def exibir_arvore(self, nivel=0):
        """Exibe a estrutura da árvore de forma hierárquica."""
        print("  " * nivel + str(self.dado))
        for filho in self.filhos:
            filho.exibir_arvore(nivel + 1)


if __name__ == "__main__":
    # Criando a árvore
    raiz = No("Empresa")
    dep1 = No("Departamento de Vendas")
    dep2 = No("Departamento de TI")
    dep3 = No("Departamento de RH")

    raiz.adicionar_filho(dep1)
    raiz.adicionar_filho(dep2)
    raiz.adicionar_filho(dep3)

    dep1.adicionar_filho(No("Vendedor 1"))
    dep1.adicionar_filho(No("Vendedor 2"))
    dep1.adicionar_filho(No("Vendedor 3"))
    dep1.adicionar_filho(No("Vendedor 4"))

    dep2.adicionar_filho(No("Desenvolvedor 1"))
    dep2.adicionar_filho(No("Desenvolvedor 2"))
    dep2.adicionar_filho(No("Desenvolvedor 3"))

    dep3.adicionar_filho(No("Recrutador 1"))
    dep3.adicionar_filho(No("Recrutador 2"))

    # Exibindo a árvore
    raiz.exibir_arvore()
    print(35*'-')

    # Buscando um nó na árvore
    resultado = raiz.buscar("Desenvolvedor 3")
    if resultado:
        print("Nó encontrado:", resultado.dado)
    else:
        print("Nó não encontrado.")
    print(35*'-')

    # Removendo um nó
    raiz.remover_filho("Departamento de RH")
    raiz.exibir_arvore()
    print(35*'-')
    raiz.remover_filho("Departamento de Vendas")
    raiz.exibir_arvore()
