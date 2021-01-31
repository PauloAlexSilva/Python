"""
Documentando funções com Docstrings

OBS: Podemos ter acesso à documentação de uma função em Python utilizando a
propriedade especial __doc__

Podemos ainda fazer acesso à documentação com a função help()

"""


# Exemplos

def hello():
    """Uma função simples que retorna a string 'hello'"""
    return 'Hello!'


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' à 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Pod padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia


print(hello())
print(help(hello()))
print(hello.__doc__)

print(exponencial.__doc__)