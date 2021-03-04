"""
Funçoes de Maior Grandeza - Higher Order Functions - HOF

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam
outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras funções,
e até mesmo criar variáveis do tipo de funções nos nossos porgramas.

OBS: Na secção de funções foi usado isto.



"""


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
