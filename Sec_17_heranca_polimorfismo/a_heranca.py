"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender as classes criadas pelo
utilizador.

OBS: Com a herença, a partir de uma classe existente, é extendida outra classe que passa
a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - nif;
    - renda.

Funcionario
    - nome;
    - sobrenome;
    - nif;
    - matricula.

Existe alguma entidade genérica o suficiene para encapsular os atributos e métodos comuns
a outras entidades?


class Cliente:

    def __init__(self, nome, sobrenome, nif, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__nif = nif
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, nif, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__nif = nif
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Paulo', 'Silva', '123456', 5000)
func1 = Funcionario('Carlos', 'Nunes', '54321', 1234)

print(cliente1.nome_completo())
print(func1.nome_completo())


OBS: Quando uma classe herda de outra classe ela herda todos os atributos e métodos da
classe herdada.


Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    (Pessoa)
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica.

Qunado uma classe herda de outra classe, ela é chamada:
    (Cliente, Funcionário)
    - Sub Classe;
    - Classe Filha;
    - Classe Específica.


class Pessoa:

    def __init__(self, nome, sobrenome, nif):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__nif = nif

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, nif, renda):
        super().__init__(nome, sobrenome, nif)
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, nif, matricula):
        super().__init__(nome, sobrenome, nif)  # Forma comum de aceder dados da super classe
        # Pessoa.__init__(self, nome, sobrenome, nif) Forma não comum de aceder dados da super classe
        self.__matricula = matricula


cliente1 = Cliente('Paulo', 'Silva', '123456', 5000)
func1 = Funcionario('Carlos', 'Nunes', '54321', 1234)

print(cliente1.nome_completo())
print(func1.nome_completo())

print(func1.__dict__)

"""


class Pessoa:

    def __init__(self, nome, sobrenome, nif):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__nif = nif

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, nif, renda):
        super().__init__(nome, sobrenome, nif)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, nif, matricula):
        super().__init__(nome, sobrenome, nif)  # Forma comum de aceder dados da super classe
        # Pessoa.__init__(self, nome, sobrenome, nif) Forma não comum de aceder dados da super classe
        self.__matricula = matricula


# Sobrescrita de Métodos - (Overriding)

cliente1 = Cliente('Paulo', 'Silva', '123456', 5000)
func1 = Funcionario('Carlos', 'Nunes', '54321', 1234)

cliente1 = Cliente('Paulo', 'Silva', '123456', 5000)
func1 = Funcionario('Carlos', 'Nunes', '54321', 1234)
cliente1 = Cliente('Paulo', 'Silva', '123456', 5000)
func1 = Funcionario('Carlos', 'Nunes', '54321', 1234)