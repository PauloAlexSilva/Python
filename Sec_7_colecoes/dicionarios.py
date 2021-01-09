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
"""

paises = {'pt': 'Portugal', 'br': 'Brasil', 'usa': 'Estados Unidos'}
