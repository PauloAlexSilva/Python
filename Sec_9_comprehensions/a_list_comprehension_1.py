"""
List Comprehension Parte 1

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados
a partir de outro iterável.


# Sintaxe da List Comprehension

[ dado for dado in iterável ]


# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

res2 = [numero / 2 for numero in numeros]
print(res2)


def funcao(valor):
    return valor * valor


res3 = [funcao(numero) for numero in numeros]
print(res3)


Para entender melhor o que está a acontecer devemos dividir a expressão em duas partes

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10


# List Comprehension versos Loop

numeros_dobrados = []

for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)


# List Comprehension

print([numero * 2 for numero in [1, 2, 3, 4, 5]])


"""

# Outros Exemplos

nome = 'Paulo Silva'

print([letra.upper() for letra in nome])


# Exemplo 2


def letra_grande(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Carlos']

print([letra_grande(amigo) for amigo in amigos])

# Exemplo 3

print([numero * 3 for numero in range(1, 10)])

# Exemplo 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
"""
['P', 'A', 'U', 'L', 'O', ' ', 'S', 'I', 'L', 'V', 'A']
['Maria', 'Julia', 'Pedro', 'Guilherme', 'Carlos']
[3, 6, 9, 12, 15, 18, 21, 24, 27]
[False, False, False, True, True, True]
"""

# Exemplo 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])
