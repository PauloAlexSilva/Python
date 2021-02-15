"""
Debug com PDB

PDB - Python Debugger

Bug -> Inseto


# OBS: A utilização do print() para debugar código é uma práritca ruim.

def dividir(a, b):
    print(f'a={a}', f'b={b}')
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}!'


print(dividir(4, 7))


# Existem formas mais profissionais de se fazer esse 'debug' utilizando o debbuger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# o PDB - Python Debugger

# Exemplo com o PyCharm

def divisao(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}!'


print(divisao(4, 0))



# Exemplo com o PDB - Python Debugger - Exemplo 1

# Para utilizar o Python Debugger precisamos* importar a biblioteca pdb e então utilizar a função
# set_trace()

# Comandos básicos do PDB:
# l - listar onde estamos no código;
# n - próxima linha;
# p - imprime variável;
# c - continua a execução - finaliza o debugging

import pdb

nome = 'Paulo'
sobrenome = 'Silva'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)


# Exemplo com o PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger precisamos* importar a biblioteca pdb e então utilizar a função
# set_trace()

# Comandos básicos do PDB:
# l - listar onde estamos no código;
# n - próxima linha;
# p - imprime variável;
# c - continua a execução - finaliza o debugging

nome = 'Paulo'
sobrenome = 'Silva'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Porquê utilizar este formato?
# o debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no início do arquivo. Por isso, ao invés de colocarmos o import do pdb no início do arquivo.
# nós colocamos somente onde vamor debuggar, e ao finalizar já fazemos a remoção.


# Exemplo com o PDB - Python Debugger - Exemplo 3

# Para utilizar o Python Debugger precisamos* importar a biblioteca pdb e então utilizar a função
# set_trace()

# * A partir do Python 3.7, não é necessário importar a biblioteca pdb, pois o comando de debug
# foi incorporado como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB:
# l - listar onde estamos no código;
# n - próxima linha;
# p - imprime variável;
# c - continua a execução - finaliza o debugging

nome = 'Paulo'
sobrenome = 'Silva'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)


"""


# OBS: Cuidado com conflitos entres nomes de variáveis e os comandos do pdb.

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))


# Como os nomes das variáveis são os mesmos dos comandos do pdb, devemos utilizar o comando p
# para imprimir as variáveis. Ou seja: p nome_da_variavel

# Nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos.
def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4
