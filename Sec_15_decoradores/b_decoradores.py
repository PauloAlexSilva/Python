"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntax Sugar / Açucar Sintático)

/---------------------------------/
/        Function Decorator       /
/---------------------------------/

-----------------------------------------
/  /---------------------------------/  /
/  /       Função decorada           /  /
/  /---------------------------------/  /
/----------------------------------------

"""


# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um gosto conhece-lo!')
        funcao()
        print('Tenha um bom dia!')

    return sendo


def saudacao():
    print('Seja bem-vindo!')


# Teste 1

teste = seja_educado(saudacao)

teste()
