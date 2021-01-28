"""
Módulo Collections - Named Tuple

# Recap tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tuplas, deferenciadas, onde, especificamos um nome para a mesma
e também parâmetros.


"""

# Import
from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple

cao = namedtuple('cao', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cao_2 = namedtuple('cao', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cao_3 = namedtuple('cao', ['idade', 'raca', 'nome'])

# Usar

ray = cao(idade=2, raca='Labrador', nome='Stors')

print(ray)

# Acessar o dados

# Forma 1

print(ray[0])  # idade
print(ray[1])  # nome
print(ray[2])  # raca

# Fomra 2

print(ray.idade)  # idade
print(ray.nome)  # nome
print(ray.raca)  # raca

print(ray.index('Stors'))

print(ray.count('Stors'))
