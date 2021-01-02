"""
Tipo Boolean

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True
False

OBS: Sempre com a inicial em maiúscula
"""

ativo = False

print(ativo)

"""
Operações Básicas
"""
# Negação (not)
"""
Fazendo a negação, se o valor booleano for verdadeiro o resutlado será falso.
Se o valor for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print(not ativo)

# Ou (or)
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve
ser verdadeiro.

>>> True or True
True
>>> True or False
True
>>>False or True
True
>>> False or False
False
"""
logado = False
print(ativo or logado)

# E (and)
"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos o valores devem ser verdadeiros.

>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
"""

# Alguns testes Booleanos
"""
>>> 5 > 6
False
>>> 5 < 6
True
>>> 6 == 6
True
>>> 4 <= 5
True
>>> num1 = 7
>>> num2 = 8
>>> num1 >= num2
False
>>> num1 == num2
False
>>> num1 < num2 or num1 > 3
True
>>> num1
7
>>> num2
8
>>> num1 < num2 and num1 > 3
True
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> ativo = True
>>> type(ativo)
<class 'bool'>
>>> dir(ativo)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__
doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewa
rgs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__
lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd
__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod
__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__r
xor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor_
_', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_b
ytes']
"""
