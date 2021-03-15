"""
Decoradores com Diferentes Assinaturas

# Para resolver utilizamos um padrão de projeto chamado Decorator Pattern

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.

# Relembrar

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o {nome}.'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}. acompanhamento de {acompanhamento}, por favor.'


# Teste

# print(saudacao('Paulo'))
print(ordenar('Picanha', 'Batata frita'))


# Refatorando com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o {nome}.'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'


print(saudacao('Paulo'))

print(ordenar('Picanha', 'Batata Frita'))


@gritar
def lol():
    return 'lol'


print(lol())

# OBS: Podemos utilizar parâmetros nomeados

print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))

"""

# Decorator

