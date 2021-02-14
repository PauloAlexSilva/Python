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


"""


# Exemplo mais complexo

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
