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
        # Ponteiro para o próximo imóvel na lista
        self.proximo: Optional[Imovel] = None


class ListaSimplesmenteEncadeada:
    """
    Lista Simplesmente Encadeada para armazenar imóveis.
    """

    def __init__(self):
        self.cabeca: Optional[Imovel] = None  # Primeiro elemento da lista

    def inserir(self, id: int, endereco: str, proprietario: str, preco: float):
        """Insere um novo imóvel no início da lista."""
        novo_imovel = Imovel(id, endereco, proprietario, preco)
        novo_imovel.proximo = self.cabeca  # O novo imóvel aponta para a antiga cabeça
        self.cabeca = novo_imovel  # Atualiza a cabeça da lista
        print(f"Imóvel {id} inserido.")

    def remover(self, id: int):
        """Remove um imóvel pelo ID."""
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.id == id:
                if anterior:
                    anterior.proximo = atual.proximo  # Remove o imóvel intermediário
                else:
                    self.cabeca = atual.proximo  # Remove a cabeça da lista
                print(f"Imóvel {id} removido.")
                return
            anterior = atual
            atual = atual.proximo
        print("Imóvel não encontrado.")

    def buscar(self, id: int):
        """Busca um imóvel pelo ID."""
        atual = self.cabeca
        while atual:
            if atual.id == id:
                print(
                    f"Imóvel encontrado: {atual.endereco}, Proprietário: {atual.proprietario}, Aluguel: R${atual.preco}")
                return atual
            atual = atual.proximo
        print("Imóvel não encontrado.")
        return None

    def listar_imoveis(self):
        """Exibe todos os imóveis cadastrados na lista."""
        if not self.cabeca:
            print("Nenhum imóvel cadastrado.")
            return
        atual = self.cabeca
        print("Lista de imóveis cadastrados:")
        while atual:
            print(
                f"ID: {atual.id}, Endereço: {atual.endereco}, Proprietário: {atual.proprietario}, Aluguel: R${atual.preco}")
            atual = atual.proximo


if __name__ == "__main__":
    # Exemplo de uso
    corretor_imoveis = ListaSimplesmenteEncadeada()
    corretor_imoveis.inserir(1, "Rua A, 123", "Victor Cordeiro", 3500)
    corretor_imoveis.inserir(2, "Av. B, 456", "Raul", 2000)
    corretor_imoveis.inserir(3, "Rua C, 789", "Luiz Oliveira", 1800)
    print(80*'-')
    corretor_imoveis.listar_imoveis()
    print(80*'-')
    corretor_imoveis.buscar(2)
    print(80*'-')
    corretor_imoveis.remover(2)
    print(80*'-')
    corretor_imoveis.listar_imoveis()
