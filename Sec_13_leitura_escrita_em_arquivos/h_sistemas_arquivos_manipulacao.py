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


# Criar Diretórios - únicos (um a um)

# Path Relativo

os.mkdir('Templates')

# OBS: A função mkdir cria um diretório se este não exisitr. Caso exista, teremos FileExistsError

# Path Absoluto

os.mkdir('/home/ubuntu/template')

# OBS: Sen não tivermos permissão para criar o directório teremos um PermissionError


# Criando multi-diretórios

os.makedirs('pasta/teste')

# OBS: Se os diretórios já existirem ocorre um FileExistsError


os.makedirs('pasta2/teste', exist_ok=True) # Se exisitr é para ignorar


# Alterar nome de arquivos e diretórios

# Diretórios

os.rename('pasta', 'pasta_nova')

# Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos alterar o nome não estiver vazio teremos um OSError

# Arquivos

os.rename('mais.txt', 'menos.txt')



# ATENÇÃO: Muito cuidado com os comando de delete. Ao apagar um arquivo ou diretório não
# vão para a lixeira, são eleminados definitavamente.

# Remover Arquivos

os.remove('menos.txt')

# OBS: Se estiver no windows e o arquivo que se quer eliminar estiver a ser usado, será gerado um
# erro.

# Caso o arquivo não existe teremos o FileNotFoundError

# OBS: Se for informado um diretório em vez de um arquivo, teremos um IsADirectoryError


# Remover Diretórios

os.rmdir('Templates')

# OBS: Se o diretório tiver conteúdo será gerado um erro OSError.

# OBS: Se o diretório não existir teremos um FileNotFoundError



# Podemos remover árvores de dirtórios vazios
os.removedirs('teste1/teste2/teste3')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para


# Importando a biblioteca send2trash (Envia arquivos e diretórios para o lixo)

from send2trash import send2trash

os.remove('novo.txt')  # não vai para a lixeira

send2trash('arquivo_teste_1.txt')  # Este vai para a lixeira

# OBS: Se os arquivo não existir teremos OSError



# Trabalhando com arquivos e diretórios temporários

import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'TEmporário {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Testeq\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo dentro dele criando um arquivo para
# escrever para escrevermos um texto. No final, usamos um input() só para mantermos os arquivos
# temporários 'vivos' dentro dos blocos with

# OBS: Possivelmente o código acima não irá funcionar em windows.

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso utilizamos o b''

"""

import os

