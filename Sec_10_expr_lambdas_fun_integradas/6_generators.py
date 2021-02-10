""""
Generators

Em aulas anteriores foi abordado:
    - List Comprehension;
    - Dictionary Comprehension;
    - Set Comprehension.

Não foi abordado:
    - Tuple Comprehension ... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cristiana', 'Cristina', 'Vanessa']

print(any8[nomes[0] == 'C' for nome in nomes])


# Poderia ter sido feito usando os Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cristiana', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension

res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)  # [True, True, True, True, True, False]

# Generator - mais efeciente

res2 = (nome[0] == 'C' for nome in nomes)
print(type(res2))
print(res2)


"""

import sys


