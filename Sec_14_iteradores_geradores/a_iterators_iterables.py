"""
Iterators e Iterables

Iterator:
    - É um objeto que pode ser iterado;
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterable:
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.


nome = 'Paulo'  # É um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5]  # É um iterable mas não é um iterator

it_1 = iter(nome)
it_2 = iter(numeros)

print(next(it_1)) # P
print(next(it_1)) # A
print(next(it_1)) # U
print(next(it_1)) # L
print(next(it_1)) # O


"""

nome = 'Paulo'

for letra in nome: # transforma o nome que é iterable num iterator
    print(f'{letra}')
