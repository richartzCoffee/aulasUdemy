"""


"""

lista = [1,2,3,6,5,5,6,9,63,4,5,6,689,8,9,]
lista3 = [0,9,8,7,89,55]
lista4= [0,2,3]

zzip = zip(lista3,lista,lista4)
print(list(zzip))
zzip = zip(lista3,lista,lista4)
print(set(zip(zzip,zip(zip(zip(lista3,lista),lista),lista3))))

dici = {'a':4,'b':5,'c':9}
print(set(zip(dici.values(),lista)))

dd = [(1,2),(3,4),(5,6),(7,8),(9,10)]
print(set(zip(*dd)))

aluno = ["daniel","luca","everton"]
pr1 = [10,10,10]
pr2 = [9,8,10]


print(list(zip(aluno,map(lambda nota:max(nota),zip(pr1,pr2)))))
