'''

Gerar novos dados com variaveis em uma lista


[dado for dado in interavel]


numeros = [0,1,2,3,4,5,6]

res = [numero *10 for numero in numeros]

print(res)

def test(valor):
    return valor*2

res = [test(numero) for numero in numeros]

print(res)

'''

numeros = [1,2,3,4,5,6,7,8,9]

res = [numero * 10 for numero in numeros]

print(res)

res = [numero/2 for numero in numeros]

print(res)

da = 'daniel'
print(da.title())

impar = [numero for numero in numeros if numero%2]

print(impar)