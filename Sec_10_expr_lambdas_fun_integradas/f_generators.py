""""
Generator Expression

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


# O que faz a função de getsizeof()? -> retorna a quantidade de bytes em memória do elemento
# passado como parâmetro

from sys import getsizeof

# Mostra quantos bytes a string 'Paulo' está ocupando em memória.
# Quanto maior a string mais espaço ocupa.

print(getsizeof('Paulo'))
print(getsizeof('Quanto maior a string mais espaço ocupa.'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(12345667890))
print(getsizeof(True))


from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes!')
print(f'Set Comprehension: {set_comp} bytes!')
print(f'Dictionary Comprehension: {dic_comp} bytes!')
print(f'Generator Expression: {gen} bytes!')


Para fazer a mesma gastamos em memória:
List Comprehension: 8856 bytes!
Set Comprehension: 32984 bytes!
Dictionary Comprehension: 36960 bytes!
Generator Expression: 112 bytes!


"""

# Posso iterar no Generator Expression? Sim

gen = (x * 10 for x in range(1000))

print(gen)
print(type(gen))

for num in gen:
    print(num)
