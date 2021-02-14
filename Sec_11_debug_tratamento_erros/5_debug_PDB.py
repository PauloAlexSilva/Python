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


"""

# Exemplo com o PDB - Python Debugger

# Para utilizar o Python Debugger precisamos* importar a biblioteca pdb e então utilizar a função
# set_trace()

import pdb

nome = 'Paulo'
sobrenome = 'Silva'
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'

