"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro é opcional

print('Hello World!')

print()


# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado()) # TypeError


def exponencial(numero, potencia=2):  # Passar um valor por parâmtro ele se torna opcional
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão elevado ao quadrado
print(exponencial(3, 5))  # Elevado à potência informada pelo utilizador

# Se o utilizador passar apenas um argumento, este será atribuido ao parâmetro "numero",
# e será calculado o quadrado deste número;
# Se o utilizador passar dois argumentos, o primeiro será atribuído ao parâmetro "numero" e
# o segundo ao parâmetro "potencia". Então será calculada esta potência.


# OBS : Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre
# estar no final da declaração

# ERRO!
def teste(num=2, potencia):
    return num ** potencia


print(teste(6))


# Outros exemplos

def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())  # TypeError


# Exemplo mais complexo

def mostra_informacao(nome='Paulo', instrutor=False):
    if nome == 'Paulo' and instrutor:
        return 'Bem vindo instrutor Paulo'
    elif nome == 'Paulo':
        return 'Eu pensei que era o intrutor!'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Carlos'))
print(mostra_informacao(nome='Carlos'))


# Porque utilizar parâmetros com valor default?

- Permite que sejamos mais flexiveis nas funções;
- Evita erros com parâmetros incorretos;
- Permite trabalhar com exemplos mais legíveis de código.


# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções, etc.


# Exemplos

def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))


# Escopo - Evitar probelmas e confusões

# Variáveis Globais
# Váriáveis Locais

instrutor = 'Paulo'  # Variável global


def hello():
    instrutor = 'Python'  # Variável local
    return f'Hello {instrutor}!'


print(hello())
print(instrutor)

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local
# terá preferência


def hello():
    prof = 'Paulo'  # variável local
    return f'Hello {prof}'


print(hello())
print(prof)  # NameError


# ATENÇÃO com variáveis globais (Se podermos evitar, evite)

total = 0


def incrementa():
    total = total + 1  # UnboundLocalError ( A variável local
    return total       # está sendo utilizada para processamento sem ter sido inicializada)


print(incrementa())


# ATENÇÃO com variáveis globais (Se podermos evitar, evite)

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global

    total = total + 1  # UnboundLocalError ( A variável local
    return total  # está sendo utilizada para processamento sem ter sido inicializada)


print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())


"""


# Podemos ter funções que são declaradas dentro de funções e também tem uma forma especial de
# escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # não é uma variável local
        contador = contador + 1
        return contador

    return dentro()


print(fora())
print(fora())
print(fora())

print(dentro())  # NameError
