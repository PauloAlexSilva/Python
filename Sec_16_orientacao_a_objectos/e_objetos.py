"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para
sua representação computacionakl, devemos poder criar quantos objetos forem necessários.
Podemos pensar nos objetos/instâncias de uma classe como variáveis do tipo definido na classe.

"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Utilizador:

    def __init__(self, nome, sobrenome, email, password):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__password = password


# Instâncias ou Objetos

lamp1 = Lampada('Branca', '220', '60')

cc1 = ContaCorrente('5000', '20000')

user1 = Utilizador('Paulo', 'Silva', 'paulo@gmail.com', '12345')
