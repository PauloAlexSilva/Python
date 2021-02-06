"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance


"""
# Import
from collections import deque

# Criando deques

deq = deque('paulo')

print(deq)

# Adicionar elementos no deque

deq.append('y')  # Adiciona no fim

print(deq)

deq.appendleft('k')  # Adiciona no lado inicio da lista

print(deq)

# Remover elementos

print(deq.pop())  # Remove e retorna o último elemento

print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento

print(deq)
