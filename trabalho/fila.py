from typing import Optional


class Senha:
    """
    Classe que representa uma senha no sistema de espera de um banco.
    """

    def __init__(self, numero: int):
        self.numero = numero  # Número da senha
        # Ponteiro para a próxima senha na fila
        self.proximo: Optional[Senha] = None


class SistemaEspera:
    """
    Lista Simplesmente Encadeada para gerenciar senhas em um banco.
    """

    def __init__(self):
        self.primeira: Optional[Senha] = None  # Primeira senha na fila
        self.ultima: Optional[Senha] = None  # Última senha na fila

    def gerar_senha(self, numero: int):
        """Gera uma nova senha e a adiciona ao final da fila."""
        nova_senha = Senha(numero)
        if not self.ultima:  # Se a fila estiver vazia, a nova senha será a única
            self.primeira = self.ultima = nova_senha
        else:
            self.ultima.proximo = nova_senha  # A última senha aponta para a nova senha
            self.ultima = nova_senha  # Atualiza a última senha
        print(f"Senha {numero} gerada e adicionada à fila.")

    def chamar_senha(self):
        """Chama a próxima senha da fila e a remove."""
        if not self.primeira:
            print("Nenhuma senha na fila.")
            return
        print(f"Senha {self.primeira.numero} chamada para atendimento.")
        self.primeira = self.primeira.proximo  # Atualiza a cabeça da fila
        if not self.primeira:
            self.ultima = None  # Se a fila ficar vazia, a última também é atualizada

    def listar_senhas(self):
        """Exibe todas as senhas na fila."""
        if not self.primeira:
            print("Nenhuma senha na fila.")
            return
        atual = self.primeira
        print("Senhas na fila.")
        while atual:
            print(f"Senha {atual.numero}")
            atual = atual.proximo


if __name__ == "__main__":
    # Exemplo de uso
    sistema = SistemaEspera()
    sistema.gerar_senha(1)
    sistema.gerar_senha(2)
    sistema.gerar_senha(3)
    print(40*'-')
    sistema.listar_senhas()
    print(40*'-')
    sistema.chamar_senha()
    print(40*'-')
    sistema.listar_senhas()
    print(40*'-')
    sistema.chamar_senha()
    print(40*'-')
    sistema.listar_senhas()
