import array

# Array de assentos (0 = livre, 1 = ocupado)
assentos = array.array('i', [0, 1, 0, 1, 0])

# Verificando se o assendo 3 está ocupado.
if assentos[2] == 0:
    print("O assento está livre!")
else:
    print("O assento está ocupado.")
