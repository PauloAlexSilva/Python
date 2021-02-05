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


# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)
# {'a': 1, 'b': 4, 'c': 9, 'd': 9, 'e': 25}


numeros = [1, 1, 2, 3, 4, 5, 5]

quadrado = {valor: valor ** 2 for valor in numeros}

print(quadrado)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(mistura)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


"""

# Exemplo com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('Par' if num % 2 == 0 else 'Impar') for num in numeros}
print(res)
