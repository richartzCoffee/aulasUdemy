

numero = {'a': 1 ,'b':2}
print(numero)

[print(f"{a}  {b}") for a,b in numero.items()]

lisa = [1,2,3,4,5,6]

quadrado = {valor:valor**2 for valor in lisa}
print(quadrado)

res = {nun : ('par' if nun%2 ==0 else 'impar') for nun in lisa}
print(res)

