"""
Loop While

Forma geral

While expressão_booleana:
    //Execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo

num = 5
num < 5

-> Exemplo 1
    num = 1

    while num < 10:
        print(num)
        num += 1

    # OBS: Num loop while, é importante cuidar do critério de paragem para evitar lool infinitos.

# Exemplo 2

    resposta = ''

    while resposta != 'sim':
        resposta = input('Já acabou Paulo? ')

# Em C ou Java

    while(expressão){
        //execução
    }

    do{
        //execução
    }while(expressão);

No Python não existe o do{}While()
"""
