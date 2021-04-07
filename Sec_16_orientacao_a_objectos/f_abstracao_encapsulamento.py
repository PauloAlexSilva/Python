"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular o código dentro de um grupo lógico e hierárquico utilizando
classes.

Encapsular -> Cápsula

# Relembrar Atributos/Métodos privados em Python

Temos uma classe chamada Pessoa, que contem
um atributo privado chamado __nome e um método privado chamado __falar()

Esses elementos privados só devem ser acessados dentro da classe.
Mas em Pyhton não é bloqueado este acesso fora da classe. Com Python acontece um fenómeno chamado
Name Mangling, que faz uma alteração na forma de se acessar os elementos privados, confrome:

_Classe__elemento


Exemplo - Acessar elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()


# Abstração em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos
e métodos privados do utilizador.

Teste 1

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 42
conta1.titular = 'Silva'
conta1.saldo = 9999999999
conta1.limite = 9999999999999999999


Teste 2

print(conta1.__dict__)
conta1.extrato()

print(conta1._Conta__titular)  # Name Mangling - Não usar mas o Python permite o acesso

conta1._Conta__titular = 'Silva'

print(conta1.__dict__)


Teste 3

print(conta1.__dict__)

conta1.depositar(-150)

print(conta1.__dict__)

conta1.sacar(200)

print(conta1.__dict__)


"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}!')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa de ser positivo!')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente!')
        else:
            print('O valor deve ser positivo!')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferência paga por quem realiza a transferência

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor


# Teste

conta1 = Conta('Paulo', 150.00, 1500)
conta2 = Conta('Maria', 300, 2000)

conta1.extrato()
conta2.extrato()

conta1.transferir(100, conta2)

conta1.extrato()
conta2.extrato()
