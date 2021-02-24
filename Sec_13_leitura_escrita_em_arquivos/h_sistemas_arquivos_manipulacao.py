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



"""

import os

# Criar arquivos

open('arquivo.txt', 'w').close()
