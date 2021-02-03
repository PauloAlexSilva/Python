"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais ( Arrays/Vetores);
    - Multidimensionais (Matrizes)

Em Python nós temos as Listas

(Nas outras linguagens isto não é possivel)

numeros = [1, 'b', 3.13, True, 5] -> Podem ter vários tipos de dados


# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)
print(type(listas))

# Como fazermos para acessar os dados

# linha, coluna
print(listas[0][1])  # Acesso ao número 2
print(listas[2][1])  # Acesso ao número 8

print(listas[2][-2])  # Acesso ao número 8, funciona como um circulo


# Iteração com loops com uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]


"""

# Outros exemplos

# Gerar um tabuleiro/matrix 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo do galo

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valor iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])

