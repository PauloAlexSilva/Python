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


# Criar arquivos

# os.mknod('arquivo.teste_4.txt')

os.mknod('teste.mknod.txt')

# OBS: Se estiver a usar um Mac OS pode gerar um erro de PermissionError
# OBS: Criando um arquivo via mknod() se o arquivo já exisitr teremos o erro FileExistsError


# Criar Diretórios

# Path Relativo

os.mkdir('Templates')

# OBS: A função mkdir cria um diretório se este não exisitr. Caso exista, teremos FileExistsError

# Path Absoluto

os.mkdir('/home/ubuntu/template')

# OBS: Sen não tivermos permissão para criar o directório teremos um PermissionError



"""

import os







