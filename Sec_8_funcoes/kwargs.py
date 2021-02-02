"""
**kwargs

Poderiamos chamar este parâmetro de **x, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em um tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.


# Exemplo

def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}!')


cores(paulo='azul', ana='amarelo', fernanda='vermelho', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios

cores()
cores(carlos='navy')


# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimentos Pythônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho a certeza que é você!'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))


# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios
- *args
- Parâmetros default (não obrigatórios)
- **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos!')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Carlos', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)



"""


# A importância de manter a ordem dos parâmetros da declarção

# Função com a ordem correta de parâmetros

def mostra_info(a, b, *args, intrutor='Paulo', **kwargs):
    return [a, b, args, intrutor, kwargs]


"""
a = 1
b = 2
args = (3,)
instrutor = 'Paulo'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}

1º Forma

[1, 2, (3,), 'Paulo', {'sobrenome': 'University', 'cargo': 'Instrutor'}]

2º Forma
[1, 2, (), 3, {'sobrenome': 'University', 'cargo': 'Instrutor'}]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Função com a ordem incorreta de parâmetros

def mostra_info2(a, b, instrutor='Paulo', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info2(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar com **kwargs

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Paulo', 'sobrenome': 'Silva'}

print(mostra_nome(**nomes))


"""


def soma_mutiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)

soma_mutiplos_numeros(*lista)
soma_mutiplos_numeros(*tupla)
soma_mutiplos_numeros(*conjunto)
soma_mutiplos_numeros(**dicionario)  # duplo asteristico

# OBS: Os nomes da chave de um dicionário devem ser os mesmos dos parâmetros da função
# dicionario2 = dict(d=1, e=2, f=3)
# soma_mutiplos_numeros(**dicionario2)  # TypeError

dicionario = dict(a=1, b=2, c=3, nome='Paulo')
soma_mutiplos_numeros(**dicionario, lang='Python')
