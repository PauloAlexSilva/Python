"""
Teste de Memória com Generators


# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13, ..



# Função usando Listas - 450MB

def fib_lista(maximo):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste
for n in fib_lista(100000):
    print(n)


"""


# Função usando geradores - 3,7MB
def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste
for n in fib_gen(100000):
    print(n)
