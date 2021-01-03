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
"""

name = 'Paulo Silva'
list_numbers = [1, 3, 5, 7, 9]
numbers = range(1, 10)  # We have to turn it into a list

"""
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
"""

"""
Enumerate
enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
"""
for i, v in enumerate(name):
    print(name[i])
