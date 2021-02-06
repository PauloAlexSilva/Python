"""
Loop For

Loop -> repetition structure
For -> one of these structures

# C or Java

for(int i = 0; i < 10; i++){
    //code execution
}

# Python

for item in interavel:
    //code execution

We use loops to iterate over sequences or iterable values.
(Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis)

Iterable
    - String
        nome = 'Paulo'
    - List
        list = [1, 2, 3, 4, 5, 6]
    - Range
        numbers = range(1,10)

# Example of for 1 ( Iterating over a string)
for word in name:
    print(word)

# Example of for 2 (Iterating over a list)
for number in list_numbers:
    print(number)

# Example of for 3 ( Iterating over a range)

# range(initial_value, final_value)
# OBS:
#    The final value is not inclusive

for number_2 in range(1, 10):
    print(number_2)

Enumerate
enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 |      (0, 'P'), (1, 'a'), (2, 'u'), ...

for indice, letra in enumerate(name):
    print(name[indice])

for indice, letra in enumerate(name):
    print(letra)

for _, letra in enumerate(name): # If you don't need 'indice',
    print(letra)                 # You can discard this value and put "_"

for value in enumerate(name):
    print(value)
(0, 'P')
(1, 'a')
(2, 'u')
(3, 'l')
(4, 'o')
(5, ' ')
(6, 'S')
(7, 'i')
(8, 'l')
(9, 'v')
(10, 'a')

name = 'Paulo Silva'
list_numbers = [1, 3, 5, 7, 9]
numbers = range(1, 10)  # We have to turn it into a list

for value in enumerate(name):
    print(value[1])

plus = 0
amount = int(input('Whon many times should this loop run?\n'))

for n in range(1, amount + 1):
    num = int(input(f'Inform the value {n}/{amount}: '))
    plus = plus + num
print(f'The sum is {plus}')
"""

name = 'Paulo Silva'
for word in name:
    print(word, end='')  # Remove '\n' by default

# Original U+1F60D
# Modified U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
