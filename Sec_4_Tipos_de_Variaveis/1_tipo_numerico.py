"""
Tipo Numérico

# Atribuir um valor a uma variável
>>> num = 42

# Print dessa variável
>>> num
42
>>> print(num)
42

# Calculos
>>> 5 + 4
9
>>> 7 - 2
5
>>> 3 * 5
15
>>> 5 / 2
2.5

# Cast de um int
>>> int(5 / 2)
2

# Mod pythónico
>>> 5 // 2
2
s
# Módulo
>>> 4 % 2
0
>>> 5 % 2
1
>>> 7 % 2
1

# Elevação
>>> 3 ** 3
27

# Maior número inteiro em Java
>>> 2**63
9223372036854775808

# Em python depende da memória do computador
>>> 2**1000
107150860718626732094842504906000181056140481170553360744375038837035105112493612249319837881569585812759467291755
314682518714528569231404359845775746985748039345677748242309854210746050623711418779541821530464749835819412673987
67559165543946077062914571196477686542167660429831652624386837205668069376

# Separação da unidade de forma a facilitar a visualização
>>> 1000
1000
>>> 10000000
10000000
>>> 1_000_000
1000000
>>>

# Cálculos
>>> num + 1
43
>>> print(num + 1)
43
>>> num += 1
>>> num
43
>>> num = num + 1
>>> num
44
>>> num -= 1
>>> num
43
>>> num *= 2
>>> num
86
>>> num /= 2
>>> num
43.0
>>> num *= 2
>>> num
86
>>> num /= 2
>>> num
43.0
>>> num //= 2
>>> num
21.0

# Ver tipo da variável
>>> type(num)
<class 'float'>
>>> num = 42
>>> type(num)
<class 'int'>
>>> type(num)
<class 'float'>
>>> num = 42
>>> type(num)
<class 'int'>

# Ver possibilidades a realizar com o num
>>> dir(num)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__
doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewa
rgs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__
lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd
__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod
__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__r
xor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor_
_', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_b
ytes']

>>> num.__add__(8)
50

"""

num = 1_000_000
print(num)
