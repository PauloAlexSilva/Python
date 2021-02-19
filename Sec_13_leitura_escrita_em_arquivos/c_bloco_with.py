"""
Bloco With

Passo para trabalhar com arquivos:

# 1 - Abrir arquivo;
# 2 - Manipulação do arquivo;
# 3 - Fechar arquivo.

O bloco With é utilizado para criar um contexto de trabalho onde os recursos utilizados
são fechados após o bloco with.


"""

# Bloco with -> É a forma Pythónica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.read())
    print(arquivo.closed)

# Após o With o arquivo está fechado
# arquivo.read()

print(arquivo.closed)
