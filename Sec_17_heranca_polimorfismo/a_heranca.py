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


"""


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
