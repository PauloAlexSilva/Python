"""
Sistemas de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.


"""

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho absoluto)
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())
