"""
Decoradores com Diferentes Assinaturas

"""


# Relembrar

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()

    return aumentar
