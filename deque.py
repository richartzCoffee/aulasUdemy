'''

modulo collections - Deque

podemos dizer  que o deque é uma lista de alta performace

'''

from collections import deque

#criando deques

deq = deque('geek')

print(deq)

deq.append('dd')

print(deq)

deq.appendleft('4') #adicona no começo da lista

print(deq)

deq.popleft()

print(deq)