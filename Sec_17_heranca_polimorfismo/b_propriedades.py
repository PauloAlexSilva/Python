"""
 POO - Propriedades

"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do Cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Paulo', 3000, 5000)
conta2 = Conta('Ana', 2000, 4000)

print(conta1. extrato())
print(conta2.extrato())

soma = conta1
