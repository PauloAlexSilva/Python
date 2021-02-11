"""
Reversed

OBS: Não confundir com a função reverse() que foi abordado nas listas

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função reversed(9 retorna um iterável chamado List Reverse Iterator

"""

# Exemplos

lista = [1, 2, 3, 4, 5]
res = reversed(lista)

print(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos não definimos a ordem dos elementos
# Conjunto (Set)
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Paulo Silva'):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Paulo Silva'))))

# Fazer isto de forma mais fácil com o slice de strings
print('Paulo Silva'[::-1])

# Podemos usar também o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Também já vimos como fazer isto utilizando o proprio range()
for n in range(9, -1, -1):
    print(n)