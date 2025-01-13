class PilhaHistorico:
    def __init__(self):
        self.historico = []  # Inicializa uma pilha vazia

    def visitar_pagina(self, pagina):
        """Adiciona uma nova página ao histórico."""
        self.historico.append(pagina)
        print(f"Visitou: {pagina}")

    def voltar(self):
        """Remove a página atual e retorna à anterior."""
        if not self.historico:
            print("Nenhuma página para voltar.")
        else:
            pagina_removida = self.historico.pop()
            print(f"Voltando da página: {pagina_removida}")

    def mostrar_historico(self):
        """Exibe o histórico completo."""
        print("Histórico de navegação:", self.historico)


# Exemplo de uso:
navegador = PilhaHistorico()
navegador.visitar_pagina("google.com")
navegador.visitar_pagina("github.com")
navegador.visitar_pagina("stackoverflow.com")
navegador.mostrar_historico()

navegador.voltar()
navegador.mostrar_historico()


# Saída
'''
Visitou: google.com
Visitou: github.com
Visitou: stackoverflow.com
Histórico de navegação: ['google.com', 'github.com', 'stackoverflow.com']
Voltando da página: stackoverflow.com
Histórico de navegação: ['google.com', 'github.com']

'''
