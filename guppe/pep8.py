"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythónica.

[1] - Utilize Camel Case para os nomes de classes;
    EX: class Calculadora:

        class CalculadoraCientifica:

[2] - Utilize nomes em minusculo, separados por underline funções ou variáveis;
    Ex: def soma():
        pass


    def soma_dois():
        pass

[3] - Utilize 4 espaços para identação!(muito importante);
    if 'a' in 'banana':
    ____print('tem') "(não é recomendado usar o tab, pois em alguns pc's
    pode ser diferente de 4 espaços) 4 espaços se não resulta em erro
    de identeação"

[4] - Linhas em branco;
        - Para definir uma classe é preciso 2 linhas em branco;
        - Separar funções e definições de classe com duas linhas em branco;
        - Métodos dentro de uma classe devem ser separados com uma única
        linha em branco.

[5] - Imports:
        - devem ser sempre feitos em linhas separadas;
        -
"""


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


def soma():
    pass


def soma_dois():
    pass

if 'a' in 'banana':
    print('tem')