"""
Funçoes de Maior Grandeza - Higher Order Functions - HOF

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam
outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras funções,
e até mesmo criar variáveis do tipo de funções nos nossos porgramas.

OBS: Na secção de funções foi usado isto.

Em Python, as funções são First Class Citizen(Cidadão de primeira classe).


# Exemplos - Definindo as funções

def somar(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Teste das funções

print(calcular(4, 3, somar))

print(calcular(4, 3, subtracao))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))


# Nested Functions - Funções Aninhadas


# Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
# ou também Inner Functions (Funções internas)

# Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('Tudo bem ', 'Vai embora ', 'Olá '))
    return humor() + pessoa


# Teste

print(cumprimento('Paulo'))
print(cumprimento('Maria'))


# Devolvendo funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('ahah', 'ahahahahahahaha', 'aaaaaaaaa'))
    return rir


# Teste

rindo = faz_me_rir()
print(rindo())



"""

# Inner Functions (Funções Internas / Nested Functions) podem aceder o escopo de funções mais externas

from random import choice


def faz_me_rir_novamente(pessoa):
    def rir_rir():
        risada = choice(('ahah', 'ahahahahahaha', 'aaaa'))
        return f'{risada} {pessoa}'

    return rir_rir


# Testar

rindo = faz_me_rir_novamente('Paulo')

print(rindo())
print(rindo())
print(rindo())
