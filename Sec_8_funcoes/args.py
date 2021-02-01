"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que poderá chamar de qualquer
coisa, desde que começe com asterisco.

Exemplo:
    *assim

Mas por conveção, utilizamos *args para defini-lo.

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada
em uma tupla. Não esquecer que as tuplas são imutá

"""


# Exemplos

def soma(num1, num2, num3):
    return num1 + num2 + num3


print(soma(1, 2, 3))
