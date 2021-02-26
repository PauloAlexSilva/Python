"""
Criando uma versão de Loop

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Paulo':
    print(letra)

iter([1, 2, 3, 4, 5])
iter('Paulo')

"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Paulo Silva')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)