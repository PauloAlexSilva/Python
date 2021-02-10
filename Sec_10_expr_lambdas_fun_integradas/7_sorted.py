"""
Sorted

OBS: Não confundir, apesar do nome, com a função sort() que já foi estudada em listas.
O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar elementos.

OBS: O sorted, SEMPRE retorna uma Lista com os elementos do iterável ordenados

# Exemplo

numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)  #


numeros = [6, 1, 8, 2]
print(numeros)

print(tuple(sorted(numeros)))
print(set(sorted(numeros)))

# Adicionado parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor


# Podemos utilizar o sorted() para coisas mais complexas

utilizadores = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "paulo", "tweets": []},
    {"username": "alexandre", "tweets": [], "cor": "amarelo"},
    {"username": "nunes", "tweets": ["Eu gosto de cães", "Vou sair hoje"]},
    {"username": "silva", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(utilizadores)

# Ordenando pelo username - Ordem Alfabética
print(sorted(utilizadores, key=lambda utilizador: utilizador['username']))

# Ordenando pelo username - Ordem Alfabética Inversa
print(sorted(utilizadores, key=lambda utilizador: utilizador['username'], reverse=True))

# Ordenando pelo número de tweets
print(sorted(utilizadores, key=lambda utilizador: len(utilizador['tweets'])))

# Ordenando pelo número de tweets inverso
print(sorted(utilizadores, key=lambda utilizador: len(utilizador['tweets']), reverse=True))


"""

# Exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old rock 'in' rool, too ynoung to die", "tocou": 32}
]

# Ordena de menos tocada para a mais tocada
print(sorted(musicas, key=lambda muscia: muscia['tocou']))

# Ordena de mais tocada para a menos tocada
print(sorted(musicas, key=lambda muscia: muscia['tocou'], reverse=True))
