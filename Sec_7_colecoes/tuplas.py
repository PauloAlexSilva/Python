"""
TUPLAS (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao criar uma tupla ela não muda.
    Toda a operação em uma tupla gera uma nova tupla.

    print(type(()))
    # <class 'tuple'>

# CUIDADO 1: As tuplas são representadas por (), mas:

    tupla_1 = (1, 2, 3, 4, 5, 6)
    print(type(tupla_1))
    print(tupla_1)

    tupla_2 = 1, 2, 3, 4, 5, 6
    print(tupla_2)

    print(type(tupla_2))

    <class 'tuple'>
    (1, 2, 3, 4, 5, 6)
    (1, 2, 3, 4, 5, 6)
    <class 'tuple'>

# CUIDADO 2: Tuplas com 1 elemento

    tupla_3 = (4)  # Isso não é uma tupla
    print(tupla_3)
    print(type(tupla_3))

    tupla_4 = (4,)  # Isso é uma tupla
    print(tupla_4)
    print(type(tupla_4))

    tupla_5 = 4,
    print(tupla_5)
    print(type(tupla_5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pelas vírgula ',' e não pelo
# uso pelo uso dos parênteses '()'

(4) - Não é tupla
(4,) - É tupla
4, - É tupla


# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)

    tupla = tuple(range(11))
    print(tupla)
    print(type(tupla))


# Desempacotamento de tupla

    tupla = ('Paulo Silva', 'Programação em Python')
    nome, curso = tupla

    print(nome)
    print(curso)

# OBS: Gera erro (ValueError) se colocarmos um número diferente para desempacotar


# Métodos para adição, remoção de elementos nas tuplas não existem, dado o
# facto das tuplas serem imutáveis


# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho

# * Se os valores forem todos inteiros ou reais

    tupla = (1, 2, 3, 4, 5, 6)

    print(sum(tupla))
    print(max(tupla))
    print(min(tupla))
    print(len(tupla))


# Concatenação de Tuplas

    tupla_1 = (1, 2, 3)
    print(tupla_1)

    tupla_2 = (4, 5, 6)
    print(tupla_2)

    print(tupla_1 + tupla_2)  # Tuplas são imutáveis

    print(tupla_1)
    print(tupla_2)

    tupla_3 = tupla_1 + tupla_2
    print(tupla_3)

    tupla_1 = tupla_1 + tupla_2  # Tuplas são imutáveis, mas podemos subrescrever seus valores
    print(tupla_1)


# Verificar se determinado elemento está contido na tupla

    tupla_1 = (1, 2, 3)
    print(3 in tupla_1)

    True


# Iterando sobre uma Tupla

    tupla_1 = (1, 2, 3)

    for n in tupla_1:
        print(n)

    for indice, valor in enumerate(tupla_1):
        print(indice, valor)


# Contando elementos dentro de uma tupla

    tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

    print(tupla.count('a'))

    nome = tuple('Paulo Silva')
    print(nome)

    print(nome.count('a'))



# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Slicing

# tupla(inicio,fim,passo)

print(meses[1:10:2])

# O acesso a elementos de uma tupla também é semelhante a de uma lista

    print(meses[5])

# Iterar com While

    i = 0
    while i < len(meses):
        print(meses[i])
        i += 1


# Verificamos em qual indice de um elemento está na tupla

    print(meses.index('Junho'))

# OBS: Caso o elemento não exista será gerado ValueError


# Porque utilizar tuplas?

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam o código mais seguro*

# * Isso porque trabalhar com elementos imutáveis traz segurança para o código


# Copiando uma tupla para outra

    tupla = (1, 2, 3)
    print(tupla)

    nova = tupla # Na tupla não temos o problema de Shallow Copy

    print(nova)
    print(tupla)

    outra = (4, 5, 6)

    nova = nova + outra

    print(nova)
    print(tupla)
"""
