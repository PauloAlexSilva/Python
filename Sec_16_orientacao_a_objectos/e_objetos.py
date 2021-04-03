"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para
sua representação computacionakl, devemos poder criar quantos objetos forem necessários.
Podemos pensar nos objetos/instâncias de uma classe como variáveis do tipo definido na classe.



# Instâncias ou Objetos

lamp1 = Lampada('Branca', '220', '60')

lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente('5000', '20000')

user1 = Utilizador('Paulo', 'Silva', 'paulo@gmail.com', '12345')


nome = 'Paulo'
sobrenome = 'Silva'
email = 'paulo@gmail.com'
senha = '1234'

user = Utilizador(nome, sobrenome, email, senha)

print(str(user))



"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, nif):
        self.__nome = nome
        self.__nif = nif

    def diz(self):
        print(f'O cliente {self.__nome} diz olá.')


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


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
