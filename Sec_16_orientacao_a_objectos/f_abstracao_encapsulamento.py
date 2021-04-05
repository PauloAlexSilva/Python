"""
POO - Abstração e Encapsulamento


"""

class Utilizador:

    def __init__(self, nome, sobrenome, email, password):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__password = password


cliente1 = Cliente('Paulo', '33223232')

cc = ContaCorrente('5000', '10000', cliente1)

cc.mostra_cliente()
cliente1.diz()
cc._ContaCorrente__cliente.diz()