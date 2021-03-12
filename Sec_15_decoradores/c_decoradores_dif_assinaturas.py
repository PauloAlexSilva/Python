"""
Decoradores com Diferentes Assinaturas

# Para resolver utilizamos um padrão de projeto chamado Decorator Pattern

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


"""

# Refatorando com a Decorator Pattern

def gritar

