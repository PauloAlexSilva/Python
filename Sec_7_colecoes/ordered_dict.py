"""
Módulo Collecns: Ordered Dict

# Num dicionário a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'Chave={chave}:valor={valor}')

OrderDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.

"""

# Fazer import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'e': 5})

for chave, valor in dicionario.items():
    print(f'Chave={chave}:valor={valor}')

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'b': 2, 'a': 1}

print(dict_1 == dict_2)  # True -> Já que a ordem dos elementos não importa para o dicionário

# Ordered Dict

odict_1 = OrderedDict({'a': 1, 'b': 2})
odict_2 = OrderedDict({'b': 2, 'a': 1})

print(odict_1 == odict_2)  # False -> Já que a ordem dos elementos importa para o OrdereDict

