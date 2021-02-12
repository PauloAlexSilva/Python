"""
Levantando os próprios erros com Raise

raise -> Lança exceções

OBS: O raise não é uma função, é uma palavra reservada, assim como def ou qualquer outra
em Pyhton

Para simplificar, pense no raise como sendo útil para que possamos criar as nossas
prórpias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de Erro')


# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}.')


colore(2, 4)


def colore(texto, cor):
    cores = ('verde', 'amaraleo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser umda entre: {cores}.')
        print('Após o raise.') # Este print não é executado após o rase
    print(f'O texto {texto} será impresso na cor {cor}.')


colore('Paulo', 'vermelho')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.

"""


# Exemplo real

def colore(texto, cor):
    cores = ('verde', 'amaraleo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser umda entre: {cores}.')
        print('Após o raise.') # Este print não é executado após o rase
    print(f'O texto {texto} será impresso na cor {cor}.')


colore('Paulo', 'vermelho')
