"""
Geradores

- Geradores (Genarators) são Iterators (Iteradores):

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
    - Generators podem ser criados com funções geradoras;
    - Funções geradoras utilizam a palavra reservada "yield";
    - Generators podem ser criados com Expressões Geradoras.

Diferenças entre Funções e Generator Funtions (Funções Geradoras)

______________________________________________________________________________
| Funções                             |     Genatator Functions              |
------------------------------------------------------------------------------
| Utilizam return                     | Utilizam yield                       |
______________________________________________________________________________
| retorna uma vez                     | podem utilizar yield multiplas vezes |
------------------------------------------------------------------------------
| quando executada, retorna um valor  | quando executada retorna um generator|
------------------------------------------------------------------------------


# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


# OBS: Uma Generator Function não é um Generator. Ela gera um generator.

gen = conta_ate(5)
# print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


"""


# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


# OBS: Uma Generator Function não é um Generator. Ela gera um generator.

gen = conta_ate(10)

for num in gen:
    print(num)
