"""
Funções com Parametro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Num programa qualquer geralmente temos:
    - Entrada -> Processamento -> Saída

Se for uma função, sabemos que:
    - Não possuem entrada;
    - Não possuem saída;
    - Possuem entrada mas não possuem saída;
    - Não possuem entrada mas possuem saída;
    - Possuem entrada e saída.


# Refatorando uma função

def quadrado(numero):
    # return numero * numero
    return numero ** 2  # elevado ao quadrado


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(quadrado())  # TypeError


# Refaturando a função

def cantar_parabens(aniversariante):
    print('Parabéns a voçê')
    print('Nesta data querida')
    print('Muitos anos de vida')
    print(f'Prabéns {aniversariante}')


cantar_parabens('Paulo')


# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# numa função quantos parâmetros forem necessários. Eles são separados por vírgula

# Exemplo


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se informarmos um número errado de parâmetros ou argumentos, teremos TypeError

# print(soma(2, 3, 4))  # TypeError - Passando argumentos a mais
# print(soma(4))  # TypeError - Passando argumentos a menos


# Nomeando parâmentros

def nome_compelto(nome, sobrenome):
    return f'Seu nome compelto é {nome} {sobrenome}'


print(nome_compelto('Paulo', 'Silva'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros improta!

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_compelto(sobrenome, nome))

# Argumentos nomeados (KeyWord Arguments)

# Caso utilizemos nomes dos parâmentros nos argumentos para informá-los,
# podemos utilizar qualquer ordem.

print(nome_compelto(nome='Angelina', sobrenome='Jolie'))
print(nome_compelto(nome=nome, sobrenome=sobrenome))
print(nome_compelto(sobrenome='Marques', nome='Marcia'))



"""


# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))
    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))

