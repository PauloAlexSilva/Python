"""
Sistemas de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.


# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho absoluto)
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())

# Podemos ver se um diretório é absoluto ou relativo

print(os.path.isabs('/home/ubuntu'))  # True - os.path.isabs('home') - False

# OBS: Para utilizadores Windows
# Forma de verificação do windows

print(os.path.isabs('C:\\Users\\home'))


# Podemos identificar o sistema operativo com o módulo os

print(os.name)  # posix - (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes do sistema operativo
print(os.uname())


print(os.getcwd())  # /home/ubuntu/PycharmProjects/Python/Sec_13_leitura_escrita_em_arquivos

res = os.path.join(os.getcwd(), 'nome_arquivo', 'nome_arquivo')

os.chdir(res)

print(os.getcwd())
# /home/ubuntu/PycharmProjects/Python/Sec_13_leitura_escrita_em_arquivos/nome_arquivo/nome_arquivo

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório e o segundo
# o diretório que será junto ao atual


# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir())  # Quantos diretórios tem este arquivo


"""

# Fazer o import
import os

# Podemos listar os arquivos e diretórios com mais detalhes com o scandir()

scanner = os.scandir()

arquivos = list(scanner)
# print(arquivos)

# print(dir(arquivos[0]))

print(arquivos[0].inode())  # ??
print(arquivos[0].is_dir())  # É um diretório? False
print(arquivos[0].is_file())  # É um arquivo? True
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até ao arquivo.
print(arquivos[0].stat())  # Estatisticas sobre o arquivo

# OBS: Quando utilizamos a função scandir() é necessário fechar a mesma assim como abrimos um
# arquivo.

scanner.close()