"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, assim como atributos, em 2 grupos: Métodos de instância
e Métodos de Classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor. A sua função
é construir o objeto a partir da classe.

OBS: Todo o elemento em Python que inicia e finaliza com duplo underline é chamado de dunder
(Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO: Não usar dunder (underline no início e no fim) para criar as nossas funções. Pois,
são funções do Python internas.

# Métodos são escritos em letras minusculas. Se o nome for composto, o nome terá as palavras
separadas por underline.


p1 = Produto('PlayStation', 'Jogos', 500)

print(p1.desconto(50))


user1 = Utilizador('Paulo', 'Silva', 'teste@gmail.com', '1234')
user2 = Utilizador('Ana', 'Nunes', 'teste2@gmail.com', '4321')

print(user1.nome_completo())
print(user2.nome_completo())

print(f'Password User 1: {user1._Utilizador__senha}')  # Acesso de forma errada de um atributo de classe
print(f'Password User 2: {user2._Utilizador__senha}')


"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):  # Método construtor
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


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, percentagem):
        """Devolve o valor do produto com o desconto"""
        return (self.__valor * (100 - percentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Utilizador:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


nome = input('Introduza o Nome: ')
sobrenome = input('Introduza o Sobrenome: ')
email = input('Introduza o email: ')
senha = input('Introduza a Password: ')
confirma_senha = input('Confirme a Password: ')

if senha == confirma_senha:
    user = Utilizador(nome, sobrenome, email, senha)
else:
    print('Password Errada!')
    exit(1)

print('Utilizador criado com sucesso')

senha = input('Introduza a password para acesso: ')

if user.checa_senha(senha):
    print('Acesso Permitido!')
else:
    print('Acesso Negado!')

print(f'A senha do utilizador Criptografada: {user._Utilizador__senha}')  # Acesso errado

