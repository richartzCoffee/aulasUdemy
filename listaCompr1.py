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



