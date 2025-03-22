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
        # Ponteiro para o imóvel anterior na lista
        self.anterior: Optional[Imovel] = None
        # Ponteiro para o próximo imóvel na lista
        self.proximo: Optional[Imovel] = None


class ListaDuplamenteEncadeada:
    """
    Implementação de uma Lista Duplamente Encadeada para armazenar imóveis.
    Permite inserção e remoção em ambas as extremidades.
    """

    def __init__(self):
        self.cabeca: Optional[Imovel] = None  # Primeiro elemento da lista
        self.cauda: Optional[Imovel] = None  # Último elemento da lista

    def inserir_inicio(self, id: int, endereco: str, proprietario: str, preco: float):
        """Insere um novo imóvel no início da lista."""
        novo_imovel = Imovel(id, endereco, proprietario, preco)
        if not self.cabeca:  # Se a lista estiver vazia, o novo imóvel será o único elemento
            self.cabeca = self.cauda = novo_imovel
        else:
            novo_imovel.proximo = self.cabeca  # O novo imóvel aponta para a antiga cabeça
            self.cabeca.anterior = novo_imovel  # A antiga cabeça aponta para o novo imóvel
            self.cabeca = novo_imovel  # Atualiza a cabeça da lista
        print(f"Imóvel {id} inserido no início.")

    def inserir_fim(self, id: int, endereco: str, proprietario: str, preco: float):
        """Insere um novo imóvel no final da lista."""
        novo_imovel = Imovel(id, endereco, proprietario, preco)
        if not self.cauda:  # Se a lista estiver vazia, o novo imóvel será o único elemento
            self.cabeca = self.cauda = novo_imovel
        else:
            self.cauda.proximo = novo_imovel  # O último imóvel aponta para o novo imóvel
            novo_imovel.anterior = self.cauda  # O novo imóvel aponta para o antigo último
            self.cauda = novo_imovel  # Atualiza a cauda da lista
        print(f"Imóvel {id} inserido no final.")

    def remover_inicio(self):
        """Remove o primeiro imóvel da lista."""
        if not self.cabeca:
            print("Lista vazia, nada para remover.")
            return
        print(f"Imóvel {self.cabeca.id} removido do início.")
        self.cabeca = self.cabeca.proximo  # Atualiza a cabeça para o próximo imóvel
        if self.cabeca:
            self.cabeca.anterior = None  # Remove a referência para o antigo primeiro imóvel
        else:
            self.cauda = None  # Se a lista ficar vazia, a cauda também é atualizada

    def remover_fim(self):
        """Remove o último imóvel da lista."""
        if not self.cauda:
            print("Lista vazia, nada para remover.")
            return
        print(f"Imóvel {self.cauda.id} removido do final.")
        self.cauda = self.cauda.anterior  # Atualiza a cauda para o penúltimo imóvel
        if self.cauda:
            self.cauda.proximo = None  # Remove a referência para o antigo último imóvel
        else:
            self.cabeca = None  # Se a lista ficar vazia, a cabeça também é atualizada

    def buscar(self, id: int):
        """Busca um imóvel pelo ID na lista."""
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
    corretor_imoveis = ListaDuplamenteEncadeada()
    corretor_imoveis.inserir_inicio(1, "Rua A, 123", "Victor Cordeiro", 1500)
    corretor_imoveis.inserir_fim(2, "Av. B, 456", "Henrique", 2000)
    corretor_imoveis.inserir_inicio(3, "Rua C, 789", "Leonardo", 1800)
    corretor_imoveis.listar_imoveis()
    corretor_imoveis.buscar(2)
    corretor_imoveis.remover_inicio()
    corretor_imoveis.remover_fim()
    corretor_imoveis.listar_imoveis()
