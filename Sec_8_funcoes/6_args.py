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


# Exemplos

def soma(num1, num2, num3):
    return num1 + num2 + num3


print(soma(1, 2, 3))

# print(soma(1, 2))  # TypeError
# print(soma(1, 2, 3, 4))  # TypeError


# Etendendo o args

def soma(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total


def soma(*args):
    return sum(args)


print(soma())
print(soma(1))
print(soma(1, 2, 3))
print(soma(1, 2, 3, 4))

print(soma(23.4, 12, 5))


# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Paulo' in args and 'Silva' in args:
        return 'Bem vindo!'
    return 'Não sei quem é!'


print(verifica_info())
print(verifica_info(1, True, 'Silva', 'Paulo'))
print(verifica_info(1, 'Silva', 3.145))


"""


def soma(*args):  # args nome do atributo
    print(args)
    return sum(args)


# print(soma())
# print(soma(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

print(soma(*numeros))  # colocar '*' no nome do argumento

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento
# uma coleção de dados. Desta forma ele sabe que precisará de desempacotar os dados.
