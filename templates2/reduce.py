"""
OBS: A partir do python a funão redecu() não é masi uma função integrada
agora temos que importar d o modulo functools

em palavras do Guido
"Mano, usa a porra do loop for, é mais pratico seu tanso"
é isso ai

para entender o reduce

dados = [a1,a2,a3,a4]

def func(xy,y)
    return x*xy

"""
from functools import reduce

def soma(x,y):
    return x+y

test = [1,2,3,4,5,6]

r = reduce(soma,test)
print(r)