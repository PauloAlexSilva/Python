"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à
Teoria dos Conjuntos da Matemática.

- Em Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:
    - Sets (conjuntos) não possuem valores duplicados;
    - Sets (conjuntos) não possuem valores ordenados;
    - Elementos não são acessados via índice, ou seja, conjuntos não são
    indexados.

Conjuntos são bons para se utilizar quando precisameos armazenar elementos
mas não nos importamos com a ordenação deles.
Quando não precisamos de nos preocupar com chaves, valores e itens duplicados

Os conjuntos (sets) são referênciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas(Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto

# Forma 1

    s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Temos valores repetidos
    print(s)
    print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o
# mesmo será ignorado sem gerar erro e não fará parte do conjunto

# Forma 2 - Mais comum

    s = {1, 2, 3, 4, 5, 5}
    print(s)
    print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

    if 3 in s:
        print('Tem o 3!')
    else:
        print('Não tem o 3!')
"""

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

dados = '99, 2, 34, 23, 2, 12, 1, 44, 5, 34'

lista = list(dados)
print(f'Lista: {lista}')

tupla = tuple(dados)
print(f'Tupla: {tupla}')

dicionario = (dados, 'dict')
print(f'Dicionario: {dicionario}')

conjunto = set(dados)
print(f'Conjunto: {conjunto}')

