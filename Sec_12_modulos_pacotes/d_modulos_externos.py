"""
Instalando e Utilizando Módulos Externos

Utilizamos o gestor de pacotes Python Pip - Python Installer Package

Podemos ver todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

Instalar um módulo:

pip install nome_do_modulo


#Instalando o pacote colorama

pip install colorama

# Utilizando o pacote instalado

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Paulo Silva')
print(Fore.RED + 'Paulo Silva')
print(Fore.BLUE + 'Paulo Silva')



"""
from colorama import init, Fore
import pydf
pdf = pydf.generate_pdf('<h1>Programação em Python do básico ao avançado</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

