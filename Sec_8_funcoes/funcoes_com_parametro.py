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



"""


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
