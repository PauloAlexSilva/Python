"""
Módulo Random

O que são módulos?

- Em Python são outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.


# OBS: Existem duas formas de utilizar um módulo ou função deste.

# Forma 1 - Importando todo o módulo (Não recomendado)

import random

# random() -> Gera um número real pseudo-aleatório entre 0 e 1

# OBS: Ao realizar o import de todo o módulo, todas as funções atributos, classes e propriedades
# que estiverem dentro do móculo ficaram disponíveis (Ficarão em memória).
# Se soubermos as funções que precisamos utilizar deste módulo esta não é a melhor forma.
# Isso será visto na forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome
# da função, separados por ponto.

# OBS: Não confundir a função random() com o pacote random. Pode parecer confuso, mas a função random()
# é apenas uma função dentro do módulo random.


# Forma 2 - Importando um função específica do módulo (Forma recomendada)

from random import random

# No import acima estamos fazendo o seguinte: do módulo random, import a função random

for i in range(10):
    print(random())


# uniform() -> Gera um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # o 7 não é incluído


# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos

# Gerador de apostas

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')  # começa em 1 e vai até 60


# choice() -> Mostra um valor aleatório entre um iterável

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice('Paulo Silva'))


"""

# shuffle() -> Tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas.pop())

print(cartas)
