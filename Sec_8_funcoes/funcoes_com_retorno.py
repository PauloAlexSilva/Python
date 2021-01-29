"""
Funções com Retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Em Python quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores devem retornar estes valores com a palavra
reservada return.

OBS: Não é preciso necessariamente criar uma variável para receber o retorno de uma função.
Podemos passar a execução da função para outras funções.

# Vamos refatorar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7


# Criamos uma variável para receber o retorno da função

ret = quadrado_de_7()
print(f'Retorno: {ret}')
print(f'Retorno: {quadrado_de_7() + 1}')


# Refatorando a primeira função

def diz_ola():
    return 'Hello '


alguem = 'Pedro!'

print(diz_ola() + alguem)

OBS: Sobre a palavra reservada retrun

    1 -  Finaliza a função, ou seja sai da execução da função;
    2 - Podemos ter, em uma função diferentes returns;
    3 - Podemos, numa função retornar qualquer tipo de dado e até mesmo múltiplos valores;


# Exemplo 1

    def hello():
        print('Antes do return.')
        return 'Hello!'
        print('Apos return.') # Nunca é executado


    print(hello())

# Exemplo 2

    def nova_funcao():
        variavel = False
        if variavel:
            return 4
        elif variavel is None:
            return 3.2
        return 'b'


    print(nova_funcao())

# Exemplo 3

    def outra_funcao():
        return 2, 3, 4, 5


    # num1, num2, num3, num4 = outra_funcao()
    # print(num1, num2, num3, num4)

    print(outra_funcao())
    print(type(outra_funcao()))


# Vamos criar uma função para jogar a moeda

from random import random


def cara_coroa():
    # Gera um número pseudo-randômico entre 0 e 1
    # valor = random()
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(cara_coroa())


"""


# Erros comuns na utilização do retorno, que na verdade não é erro, mas sim codificação
# desnecessária.

def impar():
    numero = 2
    if numero % 2 != 0:
        return True
    # else: apenas tendo um else não vale a pena colocar o else mas sim o return no fim
    return False


print(impar())
