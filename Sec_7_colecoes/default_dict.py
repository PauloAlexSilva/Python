"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recapitulando dicionários

    dicionario = {'curso': 'Programação em Python'}

    print(dicionario)
    print(dicionario['curso'])

    print(dicionario['outro']) # ??? KeyError


Default Dict -> Ao criar um dicionário com o Default Dict, nós informamos um valor default
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuido.

OBS: lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e
devolver valores.

"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python'

print(dicionario)

print(dicionario['outro'])  # KeyError no dicionário comum, mas aqui não

print(dicionario)
