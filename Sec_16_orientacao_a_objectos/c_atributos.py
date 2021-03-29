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


# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a Linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)

# print(user.__senha)  # AtributeError

print(user._Acesso__senha)  # Temos acesso, mas não deveriamos fazer este acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()


# Atributos de Instância -> Aos  criarmos instâncias de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso('user1@gamil.com', '123456')
user2 = Acesso('user2@gmail.com', '123456')

user1.mostra_email()
user2.mostra_email()


# Atributos de Classe


Atributos de classe, são atributos que são declarados diretamente na classe, ou seja,
fora do construtor. Geralmente é inicializado com um valor, e este valor é partilhado
entre todas as instâncias das classes. Ou seja, ao invés de cada instância da classe
ter seus próprios valores como é o caso dos atributos de instância, com os atributos
de classe todas as instâncias terão o mesmo valor para este atributo.


p1 = Produto2('PlayStation', 'Jogos', 500)
p2 = Produto2('Xbox', 'Jogos', 300)

print(p1.imposto)
print(p2.imposto)

print(p1.valor)  # Acessp possível, mas incorreto de um atributo de classe
print(p2.valor)  # Acessp possível, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto2.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe em Python
# são chamados de atributos estáticos;

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


# Atributos de Classe

# p1 = Produto('PlayStation', 'Jogos', 500)
# p2 = Produto('XBox', 'Jogos', 400)


# Reformular a Classe Produto

class Produto2:
    # Atributo de classe
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto2.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto2.imposto)
        Produto2.contador = self.id


# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução

# OBS: O atributo dinâminco será exclusivo da instância que o criou.

p1 = Produto2('PlayStation', 'Jogos', 500)
p2 = Produto2('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '1kg'  # Na classe Produto2 não existe o atributo peso
