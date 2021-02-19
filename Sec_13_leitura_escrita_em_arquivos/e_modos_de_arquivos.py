"""
Modos de Abertura de Arquivo

r -> Abre para a leitura - Padrão;
w -> Abre para escrita - Sobrescreve caso o arquivo já exista;
x -> Abre para escrita somente se o arquivo não exisitr. Caso o arquivo exista, gera FileExistsError.
a -> Abre para escrita adicionando o conteúdo ao final do arquivo.
# OBS: Abrindo no modo 'a' -> append, se o arquivo não exisitir será criado. Caso exista, o novo
conteúdo será adicionado sempre ao final do arquivo. Com o modo a não controlamos o cursor.
+ -> Abre para o modo de atualização: Leitura e Escrita.

https://docs.python.org/3/library/functions.html#open


# Exemplo - 'x'
try:
    with open('bom_dia.txt', 'x') as arquivo:
        arquivo.write('Teste Bom Dia.\n')
except FileExistsError:
    print('Arquivo já existe!')


# Exemplo - 'a'

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe o nome de uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break


"""

with open('outro.txt', 'a+') as arquivo:
    arquivo.write('Teste!\n')
    arquivo.write('Nova Linha.\n')
