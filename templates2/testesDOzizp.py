'''
print([n for n in range(10) if not n%2])
f = {n: ("par" if not n%2 else "impar") for n in range(11) }
print(f)
print(list(n for n in range(20)))

lista1 = [0,1,2,3,4]
lista2 = [5,6,7,8,9]

print(set(zip(lista1,lista2)))

print(list(map(lambda x:x*2,lista1)))
lista3 = ["1","2","355"]
print(list(map(lambda n:int(n)*2,lista3)))

dc = {n:n**2 for n in range(1,11)}

print(dc)

print(list(filter(lambda n: not n%2,lista1)))

print(filter(lambda n:n%2,lista1))
'''

d = [{'a':1,'eita':90},{'a':4,'eita':0},{"a":10,"eita":5}]
print(d)
print(max(d,key=lambda d:d['eita'])['a'])