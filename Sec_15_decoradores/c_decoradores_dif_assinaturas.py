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


# Decorator com argumentos

def verifica_argumentos(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Pimeiro argumento precisa de ser {valor}.'
            return funcao(*args, **kwargs)

        return outra

    return interna


@verifica_argumentos('pizza')
def comida_favorita(*args):
    print(args)


@verifica_argumentos(10)
def soma_dez(num1, num2):
    return num1 + num2


# Teste

print(soma_dez(10, 12))  # 22
print(soma_dez(2, 10))  # Valor incorreto! Pimeiro argumento precisa de ser 10.

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('Carne', 'churrasco'))  # Valor incorreto! Pimeiro argumento precisa de ser pizza.

