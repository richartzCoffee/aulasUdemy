from sys import getsizeof

nomes = ['Danie','Dai','Angelita']

print(any(nome[0] == "D" for nome in nomes))

list_compre = getsizeof([x * 10 for x in range(1000)])
print(list_compre)

list_compre = getsizeof({x * 10 for x in range(1000)})
print(list_compre)

list_compre = getsizeof({x:x * 10 for x in range(1000)})
print(list_compre)

t = (x * 10 for x in range(10))

list_compre = getsizeof(t)

print(list_compre)

print(list(t)[0])







