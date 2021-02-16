"""
Set Comprehension

lista = [1, 2, 3, 4]
set = {1, 2, 3, 4}


"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo

numeros_2 = {x ** 2 for x in range(10)}
print(numeros_2)

# ALTERAÇÃO: transformar a estrutura acima num dicionário

numeros_3 = {x: x **2 for x in range(10)}
print(numeros_3)

# Outro exemplo

letras = {letra for letra in 'Paulo Silva'}
print(letras)
