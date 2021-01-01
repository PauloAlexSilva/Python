"""
Utilitários Python para auxiliar na programação.

Dir -> Apresenta todos os atributos/propriedades e funções/métodos disponíveis
        para determinado tipo de dado ou variável.

    dir(tipo de dado/variável)

    dir("HELLO")
        ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__
        ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_sub
        class__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce
        __', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subc
        lasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'fo
        rmat', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'i
        slower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
         'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rparti
        tion', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate'
        , 'upper', 'zfill']

    "HELLO".lower()
    'hello'

    "hello".upper()
    'HELLO'

Help -> Apresenta a documentação como utilizar os atributos/propriedades e
        funções/métodos disponíveis para determinado tipo de dado ou variável.

    -> \help(tipo de dado/variável.propriedadde)

        help("OLA".lower)
            Help on built-in function lower:

            lower() method of builtins.str instance
                Return a copy of the string converted to lowercase.

"""