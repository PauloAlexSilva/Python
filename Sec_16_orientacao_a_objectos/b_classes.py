"""
POO - Classes

Em POO, Classes são modelos dos objetos do mundo real sendo representados computacionalmente.

Sistema para automatizar o controlo das lampadas


Classes podem conter:
    - Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lampada, possivelmente
    iriamos querer saber se a lampada é 110 ou 220 volts, de que cor é, etc

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto
    pode realizar no seu sistema. No caso da lâmpada, por exemplo, um coportamento comum que muito
    provavelmente iríamos querer representar no nosso sistema  é o de ligar e desligar a mesma.


Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está
implementado.


OBS: Quando criamos uma classe em Python utilizamos por convenção o nome da classe começando com
letra maiúscula. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo,
todas juntas.

Dica: EM computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares
para nomes de classes, atributos, métodos, arquivos, diretórios etc.


"""


class Lampada:
    pass


class ContaCorrente:
    pass


lamp = Lampada

print(type(Lampada))
