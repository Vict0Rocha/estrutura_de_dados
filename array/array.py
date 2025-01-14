import array

# Criando um array de inteiros
numeros = array.array('i', [10, 20, 30, 40])

# Acessando elementos por índice
print("Primeiro elemento:", numeros[0])  # Saída: Primeiro elemento: 10

# Adicionando um elemento
numeros.append(50)
# Saída: array('i', [10, 20, 30, 40, 50])
print("Array após adicionar 50:", numeros)

# Removendo um elemento
numeros.remove(20)
print("Array após remover 20:", numeros)  # Saída: array('i', [10, 30, 40, 50])

# Percorrendo o array com um loop
print("Elementos no array:")
for num in numeros:
    print(num)
