"""
Módulos BuiltIn (Módulos integrados, que já vêm instalados no Python)
________________________
|Python|Módulos builtin|
________________________


# Utilizando alias (apelidos) para módulos

import random as rdm

print(rdm.random())


# Utilizando alias (apelidos) para funções

from random import randint as rdi

print(rdi(5, 89))


# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())


# Importando todo o módulo

import random

print(random.random())


# Utilizando alias (apelidos) para funções duas funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())


"""

# Para fazer import de várias funções de um módulo: utiliza-se tuple

from random import (
    random,
    randint,
    shuffle,
    choice)

print(random())

print(randint(3, 7))

lista = ['Paulo', 'Silva', 'Mundo']
shuffle(lista)
print(lista)

print(choice('Silva'))
