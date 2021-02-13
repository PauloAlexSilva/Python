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


"""

# Finally

try:
    num = int(input('Digite um número: '))
except ValueError:
    print('Valor inválido!')
print('Depois do bloco try/except')
