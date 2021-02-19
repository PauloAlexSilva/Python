"""
Escrever em Arquivos


# OBS: Ao abrir um arquivo para leitura não podemos fazer escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos ler esse arquivo, apenas
podes escrever.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrever dados num arquivo, após abrir o arquivo utilizamos a função write().
ESta função recebe uma string como parâmetro. Caso contrário teremos um TypeError.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado.
Caso ele já exista o anterior será apagado e um novo será criado. Dessa forma todos
o conteúdo do arquivo anterior é perdido.


# Exemplo de escrita - modo 'w' - write (escrever)

# Forma Pythónica

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Podemos colocar o número de linhas que quisermos.\n')
    arquivo.write('Esta é a última linha.')


# Forma tradicional de escrita em arquivos (Não é a forma Pythónica)

arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais texto.')

arquivo.close()


with open('paulo.txt', 'w') as arquivo:
    arquivo.write('Paulo ' * 1000)


"""

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe o nome de uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
