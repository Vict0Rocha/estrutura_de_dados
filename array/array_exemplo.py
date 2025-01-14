import array

# Array de assentos (0 = livre, 1 = ocupado)
assentos = array.array('i', [0, 1, 0, 1, 0])

# Verificar se o assento 3 está ocupado
if assentos[2] == 0:
    print("O assento 3 está livre!")
else:
    print("O assento 3 está ocupado.")
