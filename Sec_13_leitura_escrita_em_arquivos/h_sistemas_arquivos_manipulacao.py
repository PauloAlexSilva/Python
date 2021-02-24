"""
Sistema de Arquivos - Manipulação

"""

import os

# Descobrir se um arquivo ou diretório existe
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))  # True

# Diretório

# Paths relativos
print(os.path.exists('inicio'))  # False
print(os.path.exists('Python/inicio'))  # False

# Path absolutos
print(os.path.exists('/home/ubuntu/Python'))  # False

