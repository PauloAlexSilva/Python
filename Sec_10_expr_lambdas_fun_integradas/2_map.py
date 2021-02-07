"""
Map

Com map, fazemos mapeamento de valores para função.


import math


def area(r):
    # Calcula a área de um circulo com raio 'r'
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forms comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável
# Retorna um Map Object

areas_2 = map(area, raios)

print(areas_2)
print(type(areas_2))
print(list(areas_2))

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera


# Para fixar - Map

# Temos dados iteráveis

# Dados: a1, a2, ..., an

# Temos uma função

# Função: f(x)

# Uilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função

# O Map Object: f(a1), f(a2), f(...), f(an)


"""

# Exemplo

cidade = [('Lisboa', 29), ('Berlin', 15), ('Los Angeles', 26), ('Tokio', 27), ('Londres', 28)]

print(cidade)

# f = 9/5 * c + 32

# Lamda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidade)))

