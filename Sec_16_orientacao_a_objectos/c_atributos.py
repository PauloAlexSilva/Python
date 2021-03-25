"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos
representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos Dinâmico.

# Atributo de Instância: São atributos declarados dentro do método construtor.

#OBS: Método construtor: É um método especial utilizado para a construção do objeto.


# Em Java, uma classe Lampada, incluindo atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }

    public int getVoltagem(){
        return this.voltagem;
    }

}

Em Python por convenção, ficou estabelecido que, todo atributo de uma classe é público.
OU seja, pode ser acessado em todo o projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja,
que deva ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ "duplo underscore" no ínicio do seu nome.

Isso é conhecido também como Name Mangling.



"""


# Classes com Atríbuto de Instância PUblico

class Lampada:
    # Método construtor
    def __init__(self, voltagem, cor):
        # atributos
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Utilizador:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a Linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)

# print(user.__senha)  # AtributeError

print(user._Acesso__senha)  # Temos acesso, mas não deveriamos fazer este acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()
