'''
Exemplo 1: Pilha usando listas.
'''

pilha = []  # Minha lista

# Empilhando elementos
pilha.append(10)
pilha.append(20)
pilha.append(30)

# Verificando o topo da pilha
print("Topo da pilha:", pilha[-1])  # Saída: Topo da pilha: 30

# Desempilhando elementos
print("Desempilhando:", pilha.pop())  # Saída: Desempilhando: 30
print("Pilha após desempilhar:", pilha)  # Saída: [10, 20]
