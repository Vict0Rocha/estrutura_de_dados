# Não use uma lista para trabalhar com fila.

'''
Exemplo de uma fila usando listas.
'''

fila = []

fila.append('A')
fila.append('B')
print(fila)  # Saida: ['A', 'B']
fila.append('C')
fila.append('D')

for item in fila:
    print(item)
    # Saida: A B C D

fila.pop(0)
fila.pop(0)

print(10 * '-')
for item in fila:
    print(item)
    # Saida: C D
