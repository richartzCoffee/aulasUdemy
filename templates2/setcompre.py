
lista = (1,1,2,2,3,3,5)
sett = {1,1,1,2,2,3,3,5}
print(lista)
print(sett)

numero = {x**2 for x in lista}
print(numero)

name = "abcdefghijk"

name_l = {l for l in name}
print(name_l)