"""
Seek e Cursors

seek() -> É utilizada para mover o  cursor pelo arquivo.


arquivo = open('texto.txt')

print(arquivo.read())

# seek() -> A função seek() é utilizada para movimentar o cursor pelo arquivo. Ela recebe
# um parâmetro que indica onde queremos colocar o cursor.

# Movimentado o cursor pelo arquivo com a função seek() -> Procurar

arquivo.seek(0)

print(arquivo.read())

arquivo.seek(28)

print(arquivo.read())


# readline() -> Função que lê o arquivo linha a linha

ret = arquivo.readline()

print(type(ret))
print(ret)

print(ret.split(' '))


# readlines() -> função lê o arquivo linha a linha e coloca cada linha passa a ser
# um item da lista de strings

linhas = arquivo.readlines()

print(len(linhas))

#OBS: Quando abrimos um arquivo com a função open() é criada uma ligação entre o arquivo
no disco do computador e o programa. Essa ligação é chamada de streaming. Ao finalizar o
trabalho com o arquivo devemos encerrar essa ligação.
Para isso usamos a função close().

Passos para trabalhar com um arquivo:

1 - Abrir o arquivo;
2 - Trabalhar com o arquivo;
3 - Fechar o arquivo.

# 1 - Abrir o arquivo
arquivo = open('texto.txt')

# 2 - Trabalhar com o arquivo
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado
# True se o arquivo estiver aberto
# False se o aquivo estiver fechado

# 3 - Fechar o arquivo
arquivo.close()
print(arquivo.closed)

print(arquivo.read())
# OBS: Se tentarmos manipular o arquico após estar fecahdo teremos um ValueError.



"""
arquivo = open('texto.txt')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))
