
import statistics

dados = [1.2,2.2,3.5,4.8,5.91,6.8]

media = statistics.mean(dados)
print(media)



res = filter(lambda x:x<media,dados)
print(list(res))

paises = ["","argentina","","brasil"]

res = filter(None,paises)

print(list(res))

usuarios =[
    {"usarname":"daniel","tw":["oi"]},
    {"usarname": "daaniel", "tw": []},
{"usarname":"daniaael","tw":["oi"]}
]

res = list(filter(lambda u: not len(u["tw"]), usuarios))
print(len(res))

nomes = ["daniel","dani","test"]

lista = list(map(lambda nome:f"sua inst {nome}",filter(lambda nome:len(nome)<5,nomes)))

print(lista)