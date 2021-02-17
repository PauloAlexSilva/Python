"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo
chamado __init__.py

Nas versões do Python 3.x, não é mais obrigatória a utilização deste arquivo, mas
normalmente ainda é utilizado para manter compatibilidade.


from teste import teste_1, teste_2



print(teste_1.pi)
print(teste_1.funcao_1(4, 6))

print(teste_2.curso)
print(teste_2.funcao_2())


from teste.teste_secundario import teste_3, teste_4

print(teste_3.funcao_3())

print(teste_4.funcao_4())

"""

from teste.teste_1 import funcao_1
from teste.teste_secundario.teste_4 import funcao_4

print(funcao_1(2, 2))

print(funcao_4())
