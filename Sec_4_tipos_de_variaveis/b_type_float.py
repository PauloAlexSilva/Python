"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O seperador de casas decimais na programação é o ponto e não a virgula.

"""

# Errado no ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo no ponto de vista do Float

valor = 1.44
print(valor)
print(type(valor))
"""
# Resultado

(1, 44)
<class 'tuple'>
1.44
<class 'float'>
"""

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(valor2)
print(type(valor1))
print(type(valor2))

"""
# Resultado
1
44
<class 'int'>
<class 'int'>
"""

# Podemos converter um floar para um int
"""
OBS:. Ao converter valores float para inteiros, perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

"""
# Resultado
1
<class 'int'>
"""

# Podemos trabalhar com números complexos
"""
Todo o numero complexo é acompanhado de um "j"
>>> type(5j)
<class 'complex'>
"""
variavel = 5j
print(variavel)

# Podemos convert um int para float
num = 1_000_000
print(num)
print(type(num))
print(float(num))
print(type(float(num)))

"""
1000000
<class 'int'>
1000000.0
<class 'float'>
"""

"""
# Na conversão de int para float perde-se precisão

Ex:
>>> salario = 2.56
>>> salario2 = 3.67
>>> total = salario + salario2
>>> total
6.23
>>> total2 = int(salario) + int(salario2)
>>> total2
5
>>> total - total2
1.2300000000000004

# Ver o que se pode fazer com float

>>> dir(salario)
['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__
eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__g
etnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__
mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_e
x__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '_
_set_format__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__',
 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
"""
