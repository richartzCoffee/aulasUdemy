''''''
lista = [1,2,3,4,5,6]
res = reversed(lista)
print(tuple(res))
res = reversed(lista)
print(set(res))
for letra in reversed("geek universed"):
    print(letra,end="",flush=False)
print("")
print("_".join(list(reversed("geek universe"))))