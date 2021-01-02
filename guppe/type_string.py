"""
Tipo String

Em Puthon um dado é considerado do tipo String sempre que:
    - Estiver entre àspas simples:
        - 'uma string';
        - '2340';
        - 'a';
        - 'True';
        - '42.3'.

    - Estiver entre àspas duplas:
        - "uma string";
        - "2340";
        - "a";
        - "True";
        - "42.3".

    - Estiver entre àspas simples triplas:
        - '''uma string''';
        - '''2340''';
        - '''a''';
        - '''True''';
        - '''42.3'''.
 """
#    - Estiver entre àspas duplas triplas:
#        - """uma string""";
#        - """2340""";
#        - """a""";
#        - """True""";
#        - """42.3""".

nome = 'Hello World'
print(nome)
print(type(nome))
"""
# Resultado
Hello World
<class 'str'>
"""

nome = "Hello World"
print(nome)
print(type(nome))
"""
# Resultado
Hello World
<class 'str'>
"""

nome = '''Hello World'''
print(nome)
print(type(nome))
"""
# Resultado
Hello World
<class 'str'>
"""

nome = """Hello World"""
print(nome)
print(type(nome))
"""
# Resultado
Hello World
<class 'str'>
"""

nome2 = "Paulo \nSilva"
print(nome2)
print(type(nome2))

# Ao usar enter faz de \n
nome3 = """Paulo 
Silva"""
print(nome3)
print(type(nome3))

# Coverte tudo para maiúscula
print(nome.upper())

# Converte tudo em minúscula
print(nome.lower())

# Transforma numa lista de Strings
print(nome.split())

# O Python converte cada letra de uma string num elemento de uma lista de strings
# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10
# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# Slice de string
print(nome[0:5])  # Imprimir apenas a primeira palavra (imprime do espaço 0 ao 4)
print((nome[6:11]))

"""
Usando o split a frase "Hello World" é separada pelo espaço e transformada 
numa lista com duas Strings. Para imprimir a string que está na posição 0 
basta fazer o seguinte.

[   0,       1]
['Hello', 'World'] 
"""
print(nome.split()[0])
print(nome.split()[1])

# Inverter impressão de uma String
"""
[::-1] -> Comece do primeiro elemento, vá até ao último elemento e inverta
"""
print(nome[::-1])

# Trocar letras na String
print(nome.replace('l', 'o'))  # Neste caso troca onde está o "l" por "o"

# Exemplo de troca de texto e fica igual
texto = 'socorram me subino onibus em marrocos'  # Palíndromo
print(texto)

print(texto[::-1])
