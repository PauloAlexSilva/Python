"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICAS e também de podermos colocar QUALQUER tipo de dado.

Liguagens C/Java: Arrays

    - Possuem tamanho e tipo de dado fixo:
        Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
        sera SEMPRE do tipo inteiro e poderá ter sempre no máximo 5 valores.

Python:

    - Dinânimco:
        Não possuem tamanho fixo. Ou seja, podemos criar a lista e simplesmente ir adicionando
        elementos.
    - Qualquer tipo de dado:
        Não possuem tipo de dado fixo. Ou seja, podemos colocar qualquer tipo de dado.

    - As listas em Pyhton são representadas por parenteses rectos []


    list_1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]  # Inteiros
    list_2 = ['P', 'a', 'u', 'l', 'o', ' ', 'S', 'i', 'l', 'v', 'a']  # Strings
    list_3 = []  # Lista vazia
    list_4 = list(range(11))  # Vai gerar números de 10 elementos de 0 a 10
    list_5 = list('Paulo Silva')  # Irá gerar a lista de Strings criada à mão acima.


# Podemos facilmente checar se determinado valor está contido na lista
    num = 9
    if num in list_4:
        print(f'Encontrei o numero {num}!')
    else:
        print(f'Não encontrei o número {num}!')


# Podemos facilmente ordenar uma lista
    list_1.sort()
    print(list_1)


# Podemos facilmente contar o número de ocorrências de um valor numa lista
    print(list_1.count(1))
    print(list_5.count('e'))


# Adicionar elementos em listas

Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar 1 elemento de cada vez

    print(list_1)
    list_1.append(42)  # list_1.append(41, 32, 212, 321) Erro
    print(list_1)

    list_1.append([2, 3, 4, 5])  # Adicionar uma lista como elemento único (sublista)
    print(list_1)

    if [2, 3, 4, 5] in list_1:
        print('Encontrei a lista!')
    else:
        print('Não encontrei a lista!')

    list_1.extend([14, 78, 96])  # Coloca cada elemento da lista como valor adicional à lista
# O extend não aceita valor único
    print(list_1)


# Podemos inserir um novo elemento na lista informando a posição do índice

# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista
    list_1.insert(2, 'Novo valor')
    print(list_1)


# Podemos facilmente juntar duas listas

    #list_6 = list_1 + list_2
    #print(list_6)
    list_1.extend(list_2)
    print(list_1)


# Podemos facilmente inverter uma lista

# Forma 1
    list_1.reverse()
    list_2.reverse()
    print(list_1)
    print(list_2)

# Forma 2
    print(list_1[::-1])
    print(list_2[::-1])


# Copiar uma lista

    list_6 = list_2.copy()
    print(list_6)


# Podemos contar quantos elementos existem dentro da lista
    print(len(list_1))
    print(len(list_2))
    print(len(list_3))
    print(len(list_4))
    print(len(list_5))


# Remover elementos de uma lista

# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o último elemento mas também o retorna
    print(list_5)
    list_5.pop()
    print(list_5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita desde índice são deslocados para a esquerda.
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError.
    list_5.pop(2)
    print(list_5)


# Podemos remover todos os elementos (zerar a lista)

    print(list_5)
    list_5.clear()
    print(list_5)


# Podemos facilmente mutiplicar os elementos de uma lista
    list_6 = [1, 2, 3]
    print(list_6)
    list_6 = list_6 * 3
    print(list_6)


# Podemos facilmente converter uma string para uma lista

# Exemplo 1

    curso = 'Programação em Python: Essencial'
    print(curso)
    curso = curso.split()
    print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas

# Exemplo 2
    curso = 'Programação,em,Python:,Essencial'
    print(curso)
    curso = curso.split(',') # É informado ao split que a ',' onde a string tem que ser separada
    print(curso)


# Convertendo uma lista em uma String

    list_6 = ['Programação', 'em', 'Python', 'Essencial']
    print(list_6)

# OBS: O join irá pegar na lista 6, coloca espaço entre cada elemento e transforma em uma string
    curso = ' '.join(list_6)
    print(curso)

# OBS: O join irá pegar na lista 6, coloca '$' entre cada elemento e transforma em uma string
    curso = '$'.join(list_6)
    print(curso)


# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

    list_6 = [1, 2.34, True, 'Paulo', 'd', [1, 2, 3], 1234567890]
    print(list_6)
    print(type(list_6))


# Iteração sobre listas

# Exemplo 1 - Usando for

    soma = 0
    for elemento in list_4:
        print(elemento)
        soma = soma + elemento
    print(soma)

# Exemplo 2 - usando

    carrinho = []
    produto = ''

    while produto != 'sair':
        print("Adicione um produto na lista ou digite 'sair' para sair: ")
        produto = input()
        if produto != 'sair':
            carrinho.append(produto)

    for produto in carrinho:
        print(produto)


# Utilizando variáveis em Listas

    numeros = [1, 2, 3, 4, 5]
    print(numeros)

    num_1 = 1
    num_2 = 2
    num_3 = 2
    num_4 = 4
    num_5 = 5

    numeros = [num_1, num_2, num_3, num_4, num_5]
    print(numeros)


# Fazemos acesso ao elementos de forma indexada

    #           0         1         2        3
    cores = ['verde', 'amarelo', 'azul', 'branco']

    print(cores[0])
    print(cores[1])
    print(cores[2])
    print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
# Para se entender melhor o índice  negativo, é melhor pensar como a lista fosse um círculo
# onde o final de um elemento está ligado ao início da lista

    print('\nPrint de forma inversa!')
    print(cores[-1])
    print(cores[-2])
    print(cores[-3])
    print(cores[-4])
    # print(cores[-5]) dá erro pois não existe índice -5

    for cor in cores:
        print(cor)

    indice = 0
    while indice < len(cores):
        print(cores[indice])
        indice += 1


# Gerar indice em um for

    for indice, cor in enumerate(cores):
        print(indice, cor)


# Listas aceitam valores repetidos

    list_1 = []
    list_1.append(42)
    list_1.append(42)
    list_1.append(33)
    list_1.append(33)
    list_1.append(42)
    print(list_1)


# Outros métodos não tão importantes mas também úteis

# Encontrar o indíce de um elemento na lista

    numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indíce da lista está o valor 6
    print(numeros.index(6))

# Em qual indíce da lista está o valor 9
    print(numeros.index(9))

# print(numeros.index(19)) # Gera ValueError
# OBS: Caso não tenha o elemento na lista, será apresentado erro -> ValueError

# OBS: No caso de ter mais que um elemento devolve o primeiro que encontrar
    print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a procurar
    print(numeros.index(5, 1))  # procurar a partir do índice 1
    print(numeros.index(5, 2))  # procurar a partir do índice 2
    print(numeros.index(5, 3))  # procurar a partir do índice 3

# print(numeros.index(5, 4))  # procurar a partir do índice 4
# OBS: Caso não tenha o elemento na lista, será apresentado erro -> ValueError

# Podemos fazer buscar dentro de um range, início/fim
    print(numeros.index(8, 3, 6))  # procura o índice de valor 8, entre os índices de 3 a 6


# Revisão de slicing

# lista[início:fim:passo]
# range[início:fim:passo]

# Trabalhando com slice de lista com o parâmento 'início'

    lista = [1, 2, 3, 4]

    print(lista[1::])  # ou lista[1:] Iniciando no índice 1 e pegando todos os elementos restantes
    print(lista[-1:])  # Também posso passar valores negativos (ver como um circulo)

# Trabalhando com slice de lista com o parâmento 'fim'

    print(lista[:2])  # Começa em 0 e vai até 2-1
    print(lista[:4])  # Começa em 0 e vai até 4-1
    print(lista[1:3])  # Começa em 1 e vai até 3-1

# Trabalhando com slice de lista com o parâmetro 'passo'

    print(lista[1::2])  # Começa em 1 e vai até ao final de 2 em 2
    print(lista[::2])  # Começa em 0 e vai até ao final de 2 em 2


# Invertendo valores numa lista

    nome = ['Paulo', 'Silva']

    nome[0], nome[1] = nome[1], nome[0]
    print(nome)

    nome = ['Paulo', 'Silva']
    nome.reverse()
    print(nome)


# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho*
# * Se os valores forem todos inteiros ou reais

    lista = [1, 2, 3, 4, 5, 6]
    print(sum(lista))  # soma
    print(max(lista))  # máximo valor
    print(min(lista))  # mínimo valor
    print(len(lista))  # tamanho da lista


# Transformar uma lista em tupla

    lista = [1, 2, 3, 4, 5, 6]
    print(lista)
    print(type(lista))

    tupla = tuple(lista)
    print(tupla)
    print(type(tupla))


# Desempacotamento de listas

    lista = [1, 2, 3]
    num1, num2, num3 = lista

    print(num1)
    print(num2)
    print(num3)

    # Se tivermos um número diferente de elementos na lista ou variáveis
    # para receber os dados, teremos ValueError


# Copia de uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

    lista = [1, 2, 3]
    print(lista)

    lista_2 = lista.copy()  # cópia
    print(lista_2)

    lista_2.append(4)

    print(lista)
    print(lista_2)

    # Ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista,
    # mas elas ficaram totalmente independentes, ou seja, modificando uma lista,
    # não afeta a outra. Isso em Python é chamado de Deep Copy (Cópia profunda)


# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # cópia

print(nova)
nova.append(4)

print(lista)
print(nova)

# Ao fazer a cópia via atribuição, copiamos os dados da lista para a nova lista,
# mas apósrealizar a modificação de uma das listas, essa modificação se reflete
# em ambas as listas. Isso em Python é chamado de Shallow Copy.

"""


