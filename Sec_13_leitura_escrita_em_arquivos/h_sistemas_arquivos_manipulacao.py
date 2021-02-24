"""
Sistema de Arquivos - Manipulação


# Descobrir se um arquivo ou diretório existe
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))  # True

# Diretório

# Paths relativos
print(os.path.exists('inicio'))  # False
print(os.path.exists('Python/../inicio'))  # False

# Path absolutos
print(os.path.exists('/home/ubuntu/Python'))  # False


# Forma 1
open('arquivo_teste_1.txt', 'w').close()

# Forma 2
open('arquivo_teste_2.txt', 'a').close()

# Forma 3

with open('arquivo_teste_3.txt', 'w') as arquivo:
    pass  # Não faz nada

"""

import os

# Criar arquivos


