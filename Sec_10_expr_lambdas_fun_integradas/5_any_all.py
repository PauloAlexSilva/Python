"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda
         se o iterável está vazio.

"""

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False -> o '0' é false

print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True

print(all([]))  # Todos os números são verdadeiros? True

print(all((1, 2, 3, 4)))  # Todos os números são verdadeiros? True

print(all({1, 2, 3, 4}))  # Todos os números são verdadeiros? True

print(all('Paulo'))  # False or True? True

nomes = ['Carla', 'Carlos', 'Cristina',' Camila']

print(all([nomes[0] == 'C']))
