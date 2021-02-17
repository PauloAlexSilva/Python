"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anónimas.


# Função em Python

def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# Expressão Lambda

lambda x: 3 * x + 1

# Como utlizar a expressão lambda?

calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))


# Podemos ter expressões lambdas com múltiplas entradas

nome_compelto = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_compelto(' paulo', ' SILVA '))
print(nome_compelto('  MARIA ', ' albertina  '))


# Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também

hello = lambda: 'Hello World!'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / 7 + 1 / z)

# n = lambda x1, x2, ..., xn: <expressão>

print(hello())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError


# Exemplo

autores = ['Paulo Silva', 'Maria Albertina', 'Luis Marques Nunes', 'Carlos Nunes',
           'Ana S. Leitão', 'Inês Garcia', 'Claudia Sofia', 'I. L. Antunes',
           'Américo Silva']

print(autores)
# ['Paulo Silva', 'Maria Albertina', 'Luis Marques Nunes', 'Carlos Nunes',
# 'Ana S. Leitão', 'Inês Garcia', 'Claudia Sofia', 'I. L. Antunes', 'Américo Silva']


# Ordenar pelo sobrenome

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# ['Maria Albertina', 'I. L. Antunes', 'Inês Garcia', 'Ana S. Leitão',
# 'Luis Marques Nunes', 'Carlos Nunes', 'Paulo Silva', 'Américo Silva', 'Claudia Sofia']


"""


# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """
    Retorna a função f(x) = a * x ** 2 + b * x + c
    """
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))