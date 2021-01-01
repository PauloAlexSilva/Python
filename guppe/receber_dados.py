"""
Receber dados do utilizador

input() -> Todo dado recebido via input é do tipo String

Em Python, String é tudo o que estiver entre:
    - Aspas simples;
    - Aspas duplas;
    - Aspas simples triplas;
    - Aspas duplas triplas.

Exemplos:
    - Aspas simples -> 'Hello World'
    - Aspas duplas -> "Hello World"
    - Aspas simples triplas -> '''Hello World'''
"""
# - Aspas duplas triplas -> """Hello World"""
"""
"""

# Entrada de dados
# print("Qual é o seu nome? ")
# nome = input()  # Input -> Entrada

# Nova forma do input
nome = input('Qual é o seu nome?\n')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemeplo de print 'mais altual' 3.7
print(f'Seja bem-vindo(a) {nome}\n')

# print("Qual a sua idade? ")
# idade = input()

# Nova forma de input
idade = int(input('Que idade tem?\n'))

# Processamento


# Saida de dados
# print('A %s tem %s anos.' % (nome, idade))

# Exemeplo de print 'mais altual' 3,7
print(f'O {nome} tem {idade} anos!\n')

"""
# int(idade) => cast
"""
print(f'O {nome} nasceu em {2021 - idade}')  # Faz calculo da idade no print
