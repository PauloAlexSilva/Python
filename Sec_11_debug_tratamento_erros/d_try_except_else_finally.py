"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA A ENTRADA DEVE SER TRATADA!

OBS: A função do utilizador é DESTRUIR o sistema

# Else -> É executado somente se não ocorrer o erro.

try:
    num = int(input('Digite um número: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'O número introduzido foi: {num}')


# Finally

try:
    num = int(input('Digite um número: '))
except ValueError:
    print('Valor inválido!')
else:
    print(f'O número introduzido foi: ')
finally:
    print('Executando o finally')

# OBS: O bloco finally é sempre executado, indepedentemente se houve ou não execução

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.


# Exemplo mais complexo - Errado

def dividr(a, b):
    return a / b


num1 = int(input('Informe o primeiro numero: '))

try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa de ser numérico!')

try:
    print(dividr(num1, num2))
except NameError:
    print('Valor incorreto!')

# Exemplo complexo - Correto
# OBS: O programador é responsável pelas entradas das suas funções. Então é necessário tratar

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto!'
    except ZeroDivisionError:
        return 'Não é possível dividir por 0!'


num1 = input('Introduza o primeiro número: ')
num2 = input('Introduza o segundo número: ')

print(dividir(num1, num2))


# Exemplo complexo - Genérico

# OBS: O programador é responsável pelas entradas das suas funções. Então é necessário tratar

# Tratamento de erros de forma genérica
def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um erro!'


num1 = input('Introduza o primeiro número: ')
num2 = input('Introduza o segundo número: ')

print(dividir(num1, num2))
"""


# Exemplo complexo - Semi-Genérico

# OBS: O programador é responsável pelas entradas das suas funções. Então é necessário tratar

# Tratamento de erros de forma genérica
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}!'


num1 = input('Introduza o primeiro número: ')
num2 = input('Introduza o segundo número: ')

print(dividir(num1, num2))
