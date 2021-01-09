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

"""

paises = {'pt': 'Portugal', 'br': 'Brasil', 'usa': 'Estados Unidos'}

# Acessar elementos

# Forma 1 - Acessar via chave, da mesma forma que lista/tupla
print(paises['pt'])
# print(paises['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe,
# teremos o erro KeyError

# Forma 2 - Acessarvia get - Recomendado

print(paises.get('pt'))
print(paises.get('ru'))
