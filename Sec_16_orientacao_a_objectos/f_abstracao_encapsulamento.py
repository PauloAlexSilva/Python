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


"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')
