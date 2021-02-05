"""
Dictionary Comprehension

Se quiseremos criar uma lista fazemos:
    lista = [1, 2, 3, 4]

Se quiseremos criar uma tupla:
    tupla = (1, 2, 3, 4) # 1, 2, 3, 4

Se quisermos criar um set (conjunto):
    conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:
    dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 3}


# Sintaxe

{chave: valor for valor in interável}

"""

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)