"""
Seek e Cursors

seek() -> É utilizada para mover o  cursor pelo arquivo.

"""
arquivo = open('texto.txt')

print(arquivo.read())

# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe
# um parâmetro que indica onde queremos colocar o cursor

# Movimentado o cursor pelo arquivo com a função seek()

arquivo.seek(0)

print(arquivo.read())
