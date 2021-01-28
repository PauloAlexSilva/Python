"""
Difinindo Funções

- Funções são pequenos pedaços de código que realizam tarefas especificas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muitos úteis para executar procedimentos similiares por repetidas vezes;

OBS: Se fizer uma função que realiza várias tarefas dentro dela é bom fazer uma
verificação para que a função seja simplificada.

Já utilizamos várias funções desde do inicio do curso
Ex:
    - print()
    -len()
    -max()
    -count()


"""
# Exemplo de utilização de funções:

# cores = ['verde', 'amarelo', 'branco']

# Utilizando a função integrada (Built-in) do Python pint()

# print(cores)

# curso = 'Programação em Python'

# print(curso)

# cores.append('roxo')

# print(cores)

# curso.append('Mais') # AttributeError
# print(curso)

# cores.clear()
# print(cores)

# print(help(print))

# DRY - Dont Repeat Yourself

# Como definir funções?
"""
Em Python, a forma geral de definir uma função é:

def nome_da_funao( parametros_de_entrada):
    bloco_da_funcao

Onde:
    nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, 
    separado por underline (Snake Case)
    
    parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, 
    podendo ser opncionais ou não;
    
    bloco_da_funcao -> Também chamado de corpo da funçáo ou implementação, é onde o 
    processamento da função acontece. 
    Neste bloco, pode ter ou não retorno da função.
    
    OBS: Para definir uma função utilizamos a palavra reservada 'def' informando assim ao 
    Python que estamos a difinir uma função. Também abrimos o bloco de código com o já 
    conhecido dois pontos ':' que é utilizado em Python para definir blocos
    
    
    
"""


# Definindo a primeira função

# Definição
def diz_ola():
    print('Hello!')


"""
OBS: 
    1 - Dentro das funções podemos utilizar outras funções;
    2 - A função só executa uma tarefa, ou seja a única coisa que faz é dizer Hello
    3 - Esta função não recebe nenhum parâmetro de entrada;
    4 - Esta função não retorna nada.
"""

# Utilizando funções

# Chamada de execução
diz_ola()


# Exemplo 2

def cantar_parabens():
    print('Parabéns a você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida!')


cantar_parabens()

"""for n in range(5):
    print(n)
    cantar_parabens()"""

# Em Python, podemos criar variáveis do tipo de uma função e executar esta função através
# da variável

canta = cantar_parabens
canta()
