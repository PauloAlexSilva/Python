"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por
mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}

    print(type({}))
    <class 'dict'>

OBS: Sobre os dicionários
    - Chave e valor são separados por dois pontos 'chave : valor';
    - Tanto chave como valor ser de qualquer tipo de dados;
    - Podemos misturar tipos de dados;


# Criação de Dicionários


# Forma 1 (mais comum)

    paises = {'pt': 'Portugal', 'br': 'Brasil', 'usa': 'Estados Unidos'}

    print(paises)
    print(type(paises))


# Forma 2 (menos comum)

paises = dict(pt='Portugal', br='Brasil', usa='Estados Unidos')

    print(paises)
    print(type(paises))


# Acessar elementos


# Forma 1 - Acessar via chave, da mesma forma que lista/tupla
    print(paises['pt'])
    # print(paises['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe,
# teremos o erro KeyError


# Forma 2 - Acessarvia get - Recomendado

    print(paises.get('pt'))
    print(paises.get('ru'))


# Caso o get não encontre o objecto com a chave informada será retornado o valor None
# e não será gerado Key Error

    pais = paises.get('ru')

    if pais:
        print(f'Encontrei o país {pais}!')
    else:
        print(f'Não encontrei o país {pais}!')


# Podemos definir um valor padrão para caso não seja encontrado o objeto com a chave
informada

    pais = paises.get('pt', 'Não encontrado!')

    print(f'Encontrei o país {pais}!')


# Podemos verificar se determinada chave se encontra num dicionário

    print('br' in paises)
    print('ru' in paises)
    print('Estados Unidos' in paises)

    if 'ru' in paises:
        russia = paises['ru']


# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista,
# tupla dicionário, como chaves de dicionários.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários,
# pois as mesmas são imutáveis.

    localidades = {
        (35.6895, 39.6917): 'Escritórios em Tókio',
        (40.7128, 74.0060): 'Escritórios em Nova York',
        (35.7749, 122.4194): 'Escritórios em São Paulo'
    }

    print(localidades)
    print(type(localidades))


# Adicionar elementos em um dicionário

    receita = {'jan': 100, 'fev': 120, 'mar': 300}

    print(receita)
    print(type(receita))

# Forma 1 - Mais comum

    receita['abr'] = 350
    print(receita)

# Forma 2

    novo_dado = {'mai': 500}
    receita.update(novo_dado)  # receita.update({'mai': 500})
    print(receita)

# Actualizar dados num dicionário

# Forma 1

    receita['mai'] = 550
    print(receita)

# Forma 2

    receita.update({'mai': 600})
    print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é
# a mesma
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.


# Remover dados de um dicionário

    receita = {'jan': 100, 'fev': 120, 'mar': 300}
    print(receita)

# Forma 1 - Mais comum

    retorno = receita.pop('mar')
    print(retorno)
    print(receita)

# OBS 1: Aquie é preciso SEMPRE informar a chave, e caso não encontre o elemento,
# um KeyError é retornado

# OBS 2: Ao remover um objecto o valor deste objecto é sempre retornado

# Forma 2

    del receita['fev']
    print(receita)

# del receita['fev']
# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.

"""

# Imagine que tem um comércio eletrónico, onde temos um carrinho de compras no qual
# adicionamos produtos.
"""
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço.
    Produto 2:
        - nome;
        - quantidade;
        - preço.
"""

# 1 - Poderíamos utilizar uma Lista para isso? Sim

carrinho = []

produto_1 = ['Playstation 4', 1, 300.00]
produto_2 = ['Go of war 4', 1, 50.00]

carrinho.append(produto_1)
carrinho.append(produto_2)
print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma tupla para isso? Sim

produto_1 = ('Playstation 4', 1, 300.00)
produto_2 = ('God of War 4', 1, 50.00)

carrinho = (produto_1, produto_2)
print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderiamos utilizar um dicionário para isso? Sim

carrinho = []

produto_1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 230.00}
