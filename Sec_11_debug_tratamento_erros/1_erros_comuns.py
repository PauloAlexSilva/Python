"""
Erros mais comuns em Pyhton

# ATENÇÃO

É importante estar atento e apreender a ler as síadas de erros geradas pela execução do
nosso código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Puthon encontra um erro de sintaxe. Ou seja, foi escrito algo
               que o Python reconhece como parte da linguagem.

# Exemplos de SyntaxError

a)

    def funcao:                 # falta ()
        print('Paulo Silva')

b)

    None = 1 (None -> palavra reservada do Python)

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

# Exemplos de NameError

a)
    print(paulo) # paulo não foi definido

b)
    paulo() # esta função não foi definida

c)
    a = 18

    if a < 10:
        msg = 'É maior que 10'

print(msg) # Neste caso a variável 'msg' é declarada apenas dentro do if


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado

Exemplos TypeError

a)
    print(len(5)) # TypeError: object of type 'int' has no len()

b)
    print('Paulo' + []) # TypeError: can only concatenate str (not "list") to str


4 - IndexError -> Ocorre quando tentamos aceder um elemento num lista ou outro tipo de dado
                    indexado utilizando um indice inválido.

Exemplos IndexError

a)
    lista = ['Paulo'] # IndexError: list index out of range
    print(lista[1])

b)
    lista = ['Paulo']
    print(lista[0][10])


5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento
                    com o tipo correto mas valor inapropriado.

Exemplos ValueError

a)
    print(int('Paulo')) # ValueError: invalid literal for int() with base 10: 'Paulo'


6 - KeyError -> Ocorre quando tentamos aceder um dicionário com uma chave que não existe

Exemplos KeyError

a)
    dic = {}  # KeyError: 'Paulo'


7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

Exemplos AttributeError

a)
    tupla = (11, 2, 31, 4)
    print(tupla.sort()) #  AttributeError: 'tuple' object has no attribute 'sort'


8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError

a)
    def nova():
    print('Paulo')  # IndentationError: expected an indented block


"""





