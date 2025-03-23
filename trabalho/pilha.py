class CallStack:
    """
    Simulação de uma Call Stack (pilha de chamadas).
    """

    def __init__(self):
        self.pilha = []  # Pilha de chamadas

    def chamar_funcao(self, funcao: str):
        """Empilha uma nova função na call stack."""
        self.pilha.append(funcao)
        print(f"Chamando função: {funcao}")

    def retornar_funcao(self):
        """Desempilha a função do topo da call stack, simulando um retorno."""
        if not self.pilha:
            print("Nenhuma função em execução.")
            return
        funcao = self.pilha.pop()
        print(f"Retornando da função: {funcao}")

    def exibir_pilha(self):
        """Exibe o estado atual da call stack."""
        if not self.pilha:
            print("Call Stack vazia.")
        else:
            print("Estado atual da Call Stack.")
            for funcao in reversed(self.pilha):
                print(f" -> {funcao}")


if __name__ == "__main__":
    # Simulando chamadas de funções
    call_stack = CallStack()
    call_stack.chamar_funcao("main")
    call_stack.chamar_funcao("processar_dados")
    call_stack.chamar_funcao("calcular_resultado")
    print(45*'-')
    call_stack.exibir_pilha()
    print(45*'-')
    call_stack.retornar_funcao()
    print(45*'-')
    call_stack.exibir_pilha()
    print(45*'-')
    call_stack.retornar_funcao()
    call_stack.retornar_funcao()
    print(45*'-')
    call_stack.exibir_pilha()
