"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.


# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))  # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))  # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))  # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 129, 'f': 34}
print(max(dicionario))  # f

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 129, 'f': 34}
print(max(dicionario.values()))  # 129

print(max(3, 34))  # 34


# Faça um programa que receba dois valores do utilizador e mostre o maior

val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

print(max(val1, val2))


print(max(4, 66, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.14, 5.5789))

print(max('Paulo Silva'))


# Min

min() -> retorna o menor valor em um iterável ou o menor de dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))  # 1

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))  # 1

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))  # 1

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 129, 'f': 34}
print(min(dicionario))  # a

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 129, 'f': 34}
print(min(dicionario.values()))  # 1

print(min(3, 34))  # 3


# Faça um programa que receba dois valores do utilizador e mostre o menor

val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

print(min(val1, val2))


print(min(4, 66, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.14, 5.5789))

print(min('Paulo Silva'))  # menor é o espaço


# outros exemplos

nomes = ['Paulo', 'Dora', 'Carlos', 'Ana', 'Albertina']

print(max(nomes))  # Paulo
print(min(nomes))  # Albertina

print(max(nomes, key=lambda nome: len(nome)))  # Albertina
print(min(nomes, key=lambda nome: len(nome)))  # Ana

"""

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old rock 'in' rool, too ynoung to die", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO -> Imprimir apenas o título da música que mais e menos foi tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO -> Como encontrar a musica mais tocada e a menos tocada sem usar max, min e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])


min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
