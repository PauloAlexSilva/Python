"""
Bloco Try/Except

Utilizamos o bloco try/except para tratar tratar erros que podem ocorrer no nosso código.
Prevenindo assim que o programa para de funcionar e o utilizador receba mensagens de erro
inesperadas

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problemas


# Exemplo 1 - Tratando um erro genérico

try:
    paulo()
except:
    print('Deu algum erro!')

# Tente executar a função paulo, caso seja encontrado erros, imprima a mensagem de erro


# Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum erro!')

# Tente executar a função paulo, caso seja encontrado erros, imprima a mensagem de erro

OBS: Tratar erros de forma genérica não é a melhor forma de tratamento de erros.
O ideal é tratar SEMPRE de forma específica.


# Exemplo 3 - Tratamento específico de erros

try:
    paulo()
except NameError:
    print('Está a utilizar uma função inexistente')


# Exemplo 4 - Tratamento específico de erros

try:
    len(1)
except TypeError:
    print('Está a utilizar uma função inexistente')


# Exemplo 5 - Tratamento específico de erro com detalhes do erro

try:
    len(1)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}!')


# Podemos fazer vários tratamento de erros de uma vez

try:
    paulo()
except NameError as err:
    print(f'Deu NameError: {err}!')
except TypeError as errb:
    print(f'Deu TypeError: {errb}!')
except:
    print('Deu um erro diferente!')



"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Paulo'}

print(pega_valor(dic, 1))
