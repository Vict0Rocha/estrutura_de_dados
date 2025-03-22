from typing import Optional


class Imovel:
    """
    Classe que representa um imóvel na imobiliária.
    """

    def __init__(self, id: int, endereco: str, proprietario: str, preco: float):
        self.id = id  # Identificador único do imóvel
        self.endereco = endereco  # Endereço do imóvel
        self.proprietario = proprietario  # Nome do proprietário
        self.preco = preco  # Valor do aluguel do imóvel
        # Ponteiro para o próximo imóvel na pilha
        self.proximo: Optional[Imovel] = None


class Pilha:
    """
    Implementação de uma Pilha (LIFO - Last In, First Out) para armazenar imóveis.
    """

    def __init__(self):
        # Último imóvel inserido (topo da pilha)
        self.topo: Optional[Imovel] = None

    def empilhar(self, id: int, endereco: str, proprietario: str, preco: float):
        """Adiciona um novo imóvel no topo da pilha."""
        novo_imovel = Imovel(id, endereco, proprietario, preco)
        novo_imovel.proximo = self.topo  # O novo imóvel aponta para o antigo topo
        self.topo = novo_imovel  # Atualiza o topo da pilha
        print(f"Imóvel {id} empilhado.")

    def desempilhar(self):
        """Remove o imóvel do topo da pilha."""
        if not self.topo:
            print("A pilha está vazia, nada para desempilhar.")
            return
        print(f"Imóvel {self.topo.id} desempilhado.")
        self.topo = self.topo.proximo  # O novo topo será o próximo imóvel na pilha

    def buscar_topo(self):
        """Retorna o imóvel no topo da pilha sem removê-lo."""
        if not self.topo:
            print("A pilha está vazia.")
            return None
        print(
            f"Topo da pilha: {self.topo.endereco}, Proprietário: {self.topo.proprietario}, Aluguel: R${self.topo.preco}")
        return self.topo

    def listar_imoveis(self):
        """Exibe todos os imóveis da pilha."""
        if not self.topo:
            print("A pilha está vazia.")
            return
        atual = self.topo
        print("Imóveis na pilha:")
        while atual:
            print(
                f"ID: {atual.id}, Endereço: {atual.endereco}, Proprietário: {atual.proprietario}, Aluguel: R${atual.preco}")
            atual = atual.proximo


if __name__ == "__main__":
    # Exemplo de uso
    corretor_imoveis = Pilha()
    corretor_imoveis.empilhar(1, "Rua A, 123", "Vitão", 1500)
    corretor_imoveis.empilhar(2, "Av. B, 456", "Raul", 2000)
    corretor_imoveis.empilhar(3, "Rua C, 789", "Jeferson", 1800)
    corretor_imoveis.listar_imoveis()
    corretor_imoveis.buscar_topo()
    corretor_imoveis.desempilhar()
    corretor_imoveis.listar_imoveis()
