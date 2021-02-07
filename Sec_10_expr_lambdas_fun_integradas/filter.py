"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção


valores = 1, 2, 3, 4, 5, 6

media = (sum(valores)) / len(valores)

print(media)


# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')
# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função
# e um iterável

res = filter(lambda valor: valor > media, dados)
print(type(res))
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são
# excluidos da memória


paises = ['', 'Argentina', '', 'Portugal', 'Chile', '', 'Brasil', '', 'Equador', '', '', 'França']

print(paises)

res = filter(None, paises)

print(list(res))


paises = ['', 'Argentina', '', 'Portugal', 'Chile', '', 'Brasil', '', 'Equador', '', '', 'França']

# res = filter(lambda pais: len(pais) > 0, paises)
res = filter(None, paises)
# res = filter(lambda pais: pais != '', paises)

print(list(res))


# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objecto mapeando a
# função para cada elemento do iterável

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objecto filtrando
# apenas os elementos de acordo com a função.


# Exemplo

utilizadores = [
    {"usarname": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"usarname": "carla", "tweets": ["Eu amo meu gato"]},
    {"usarname": "paulo", "tweets": []},
    {"usarname": "alexandre", "tweets": []},
    {"usarname": "nunes", "tweets": ["Eu gosto de cães", "Vou sair hoje"]},
    {"usarname": "silva", "tweets": []}
]

print(utilizadores)

# Filtar os utilizadores que não têm tweets

# Forma 1
# inativos = list(filter(lambda user: len(user['tweets']) == 0, utilizadores))
# print(inativos)

# Forma 2
inativos = list(filter(lambda user: not user['tweets'], utilizadores))
print(inativos)


"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutura é' + nome, desde que cada nome
# tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
