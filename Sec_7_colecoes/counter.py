"""
Módulo Collections - Counter (contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objecto do tipo Collections Counter que é
parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como
valor a quantidade de ocorrências desse elemento.


# Utilizando o Counter

from collections import Counter

# Exemplo 1

    # Podemos qualquer iteravel, aqui usamos uma lista
    lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 45, 66, 66, 43, 34]

    res = Counter(lista)

    print(type(res))  # <class 'collections.Counter'>
    print(res)  # Counter({1: 5, 2: 4, 3: 4, 5: 4, 4: 3, 66: 2, 45: 1, 43: 1, 34: 1})

    # Para cada elemento da lista, o Counter criou uma chave e colocou como valor a
    # quantidade de ocorrências

# Exemplo 2

    print(Counter('Boa tarde'))
    # Counter({'a': 2, 'B': 1, 'o': 1, ' ': 1, 't': 1, 'r': 1, 'd': 1, 'e': 1})

"""

from collections import Counter

# Exemplo 3

texto = """A demanda por programadores Python nunca esteve tão alta, afinal, Python é uma das 
linguagens mais utilizadas no mundo e requisito para se trabalhar com Ciência de Dados e 
Inteligência Artificial. Além disso, a demanda por profissionais Python para trabalhar com a 
Internet utilizando algum dos frameworks web mais populares como Django, Flask ou Tornado tem
 crescido muito nos últimos anos. Por ser uma linguagem de programação versátil, simples de 
 aprender e muito poderosa, Python possui recursos que, apesar de simples de se utilizar, 
 tornam o aprendizado muito divertido."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)
print(res)

# Encontrar as 5 palavras com mais ocorrências no texto
print(res.most_common(5))

