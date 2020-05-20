"""
sorted com qualquer interavel

"""
numero = [1,2,3,56,41,5]

print(numero)

print(tuple(sorted(numero)))
print(sorted(numero,reverse=True))

usuarios =[
    {"usarname":"daniel","tw":["oi"]},
    {"usarname": "daaniaaaaaaael", "tw": [],"cor":"amarelo"},
{"usarname":"daniaael","tw":["oi"]}
]
print(sorted(usuarios,key=lambda usuario: len(usuario["tw"])))
