"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à
Teoria dos Conjuntos da Matemática.

- Em Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:
    - Sets (conjuntos) não possuem valores duplicados;
    - Sets (conjuntos) não possuem valores ordenados;
    - Elementos não são acessados via índice, ou seja, conjuntos não são
    indexados.

Conjuntos são bons para se utilizar quando precisameos armazenar elementos
mas não nos importamos com a ordenação deles.
Quando não precisamos de nos preocupar com chaves, valores e itens duplicados

Os conjuntos (sets) são referênciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas(Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto

# Forma 1

    s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Temos valores repetidos
    print(s)
    print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o
# mesmo será ignorado sem gerar erro e não fará parte do conjunto

# Forma 2 - Mais comum

    s = {1, 2, 3, 4, 5, 5}
    print(s)
    print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

    if 3 in s:
        print('Tem o 3!')
    else:
        print('Não tem o 3!')


# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos.
    lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
    print(f'Lista: {lista} com {len(lista)} elementos.')

# Tuplas aceitam valroes duplicados, então temos 10 elementos.
    tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
    print(f'Tupla: {tupla} com {len(tupla)} elementos.')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
    dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
    print(f'Dicionario: {dicionario} com {len(dicionario)} elementos.')

# Conjuntos não acaitam valores duplicados, então temos 8 elementos
    conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
    print(f'Conjunto: {conjunto} com {len(conjunto)} elementos.')


# Usos Interessantes com Sets

# Imagine que fizemos um formulário de registo de visitantes de uma feira ou museu
# e os visitantes informam manualmente a cidade de onde vieram

# Nós adicionamos cada cidade numa lista Python, já que numa lista podemos adicionar novos
# elementos e ter repetição

    cidades = ['Viseu', 'Guarda', 'Covilhã', 'Covilhã', 'Fundão', 'Viseu', 'Covilhã']

    print(cidades)
    print(len(cidades))

# Agora é preciso saber quantas cidades distintas, ou seja, únicas temos

# Podemos usar o set para isso

    print(len(set(cidades)))


# Adicionando elementos num conjunto

    s = {1, 2, 3}

    s.add(4)
    s.add(4)  # A duplicidade não gera erro, Simplesmente é ignorado e não é adicionado
    print(s)


# Remover elementos num conjunto

    s = {1, 2, 3}
    print(s)

# Forma 1

    s.remove(3)  # Não é indice, informamos o valor a ser removido
    print(s)

# OBS: Caso o valor não seja encontrado será geradoo erro KeyError. Nenhum valor é devolvido.

# Forma 2

    s.discard(2)
    print(s)

# OBS: Se o valor não for encontrado não será gerado nenhum erro


# Copiando um conjunto para outro

    s = {1, 2, 3}
    print(s)

# Forma 1 - Deep Copy

    novo = s.copy()
    print(novo)

    novo.add(4)

    print(novo)
    print(s)

# Forma 2 -  Shallow Copy

    novo = s

    novo.add(4)

    print(novo)
    print(s)

# Podemos remover todos os itens de um conjunto

    s.clear()
    print(s)


# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um com estudantes do curso de Python e
# um com estudantes do curso Java

    estudantes_python = {'Paulo', 'Luis', 'Maria', 'Ana', 'Sofia', 'Carlos'}
    estudantes_java = {'Manel', 'Gustavo', 'Sofia', 'Julia', 'Maria'}

# veja que alguns alunos que estudam python também estudam java

# Precisamos gerar um conjuntos com nomes de estudantes unicos

# Forma 1 - Utilizando union

    unicos_1 = estudantes_python.union(estudantes_java)
    print(unicos_1)
    # {'Maria', 'Manel', 'Luis', 'Ana', 'Gustavo', 'Sofia', 'Julia', 'Paulo', 'Carlos'}

# Forma 2 - Utilizando o caractere pipe "|"

    unicos_2 = estudantes_python | estudantes_java
    print(unicos_2)
    # {'Maria', 'Manel', 'Luis', 'Ana', 'Gustavo', 'Sofia', 'Julia', 'Paulo', 'Carlos'}

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

    ambos_1 = estudantes_python.intersection(estudantes_java)
    print(ambos_1)
    # {'Maria', 'Sofia'}

# Forma 2 - Utilizando o "&"

    ambos_2 = estudantes_python & estudantes_java
    print(ambos_2)
    # {'Maria', 'Sofia'}

# Gerar umn conjunto de estudantes que não estão no outro curso

    so_python = estudantes_python.difference(estudantes_java)
    print(so_python)
    # {'Carlos', 'Luis', 'Paulo', 'Ana'}

    so_java = estudantes_java.difference(estudantes_python)
    print(so_java)
    # {'Julia', 'Gustavo', 'Manel'}


"""

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os vaores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
