"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende
    , todo o programa.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas,
    ou seja, seu escopo está limitado ao bloco onde foi declarado.

Para declarar variáveis em Python:
    nome_da_variável = valor_da_variável

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declaramos
uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
    int numero = 42;

Exemplo em Java:
    int numero = 42;

Exemplo em Python:
    numero = 42
"""

# Exemplo de variável global
numero = 42
print(numero)
print(type(numero))

# Reatribuição de uma variável
numero = 'Paulo'
print(numero)
print(type(numero))

numero = 42

# Exemplo de variável local -> novo (está declarada dentro do bloco if, logo é local)
if numero > 10:
    novo = numero + 10  # ou novo += 10
    print(novo)

