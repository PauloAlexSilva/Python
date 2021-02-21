"""
StringIO

ATENÇÃO: Para ler ou escrever dados nos arquivos do Sistema Operacional o software precisa ter
permissão:
    - Permissão de Leitura -> Para ler o arquivo;
    - Permissão de Escrita -> Para escrever.

StringIO -> Utilizado para ler e criar arquivos em memória.

"""
# Primeiro fazemos o import

from io import StringIO

mensagem = 'Esta é uma String normal.'

# Podemos criar um arquivo em memória já com uma String enserida ou mesmo vazia para enserir texto
# depois.

arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo podemos utilizar tudo o que já sabemos

print(arquivo.read())

arquivo.write(' Outro texto!')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
