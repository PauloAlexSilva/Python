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


# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um gosto conhece-lo!')
        funcao()
        print('Tenha um bom dia!')

    return sendo


def saudacao():
    print('Seja bem-vindo!')


# saudacao()

# Teste 1

# teste = seja_educado(saudacao)

# teste()


# Teste 2

def raiva():
    print('ODEIO-TE!')


raiva_educada = seja_educado(raiva)

raiva_educada()


# Decorators com Syntax Sugar

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um gosto...')
        funcao()
        print('Tenha um excelente dia!')

    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Paulo!')


# Teste

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()

"""

# OBS: Não confundir Decorator com Decorator Function
