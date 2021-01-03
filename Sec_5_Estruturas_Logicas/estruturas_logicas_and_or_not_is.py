"""
Logical Structures (Estruturas Lógicas): and(e), or(ou), not(não), is(é)

# Unary operators (Operadores unários):
    - not

# Binary operators (Operadores binários):
    - and, or, is

# Operating rules
    - To 'and', both values need to be 'True'
    - To 'or', one needs to be 'True'
    - To 'not', the boolean value is inverted, if True changes to False, if Flase changes to True
    - To 'is', the value is compared to a second value

# >>> nome = 'Paulo'
# >>> dir(nome)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format
__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init
__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne_
_', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode
', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isas
cii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', '
istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix'
, 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split
', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# >>> nome.isupper()
False
# >>> nome.istitle()
True
# >>> 1 == 1
True
# >>> 1 is 1
True
# >>> nome is 'Paulo'
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True
# >>> nome is 'aulo'
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
"""
active = True
logged = True

if active and logged:
    print('Welcome user!')
else:
    print('You need to verify your account! Check your email!')

# Se não estiver ativo
if not active:
    print('Do you need activete your account! Check you email!')
else:
    print('Welcome user!')

if active is True:
    print('Welcome user!')
else:
    print('Do you need activete your account! Check you email!')

if active:
    print('Welcome user!')
else:
    print('Do you need activete your account! Check you email!')

print(not True)
print(not False)

# Is active True?
print(active is True)
