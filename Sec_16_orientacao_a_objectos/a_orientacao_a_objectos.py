"""
Programação Orientada a Objectos - POO

- POO é um paradigma de programação que utiliza mapeamento de objetos
do mundo real para modelos computacionais.

- Paradigma de progamação é a forma/metodologia utilizada para
pensar/desenvolver sistemas.

Principais Elementos da Orientação a Objetos

    - Classe -> Modelo do objeto do mundo real sendo representado
    computacionalmente;

    - Atributo -> Características do objeto;

    - Método -> Comportamento do objeto (funções);

    - Construtor -> Método especial utilizado para criar os objetos;

    - Objeto -> Instância da classe.



Class Produto
    - nome
    - preco
    - desconto

Objeto / Instância
        - Notebook
        - 1000€
        - 15%

        - Caneta Bic
        - 0.5€
        - 5%


"""

numero = 10

print(numero)
print(type(numero))

nome = 'Paulo'

print(nome)
print(type(nome))


class Produto:
    pass


ps4 = Produto()
print(ps4)
print(type(ps4))

# tESTE