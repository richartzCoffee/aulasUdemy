'''

modulo collecions - named tuple

tuplas com chaves

'''

from collections import namedtuple

#foma 1

cachorro = namedtuple('cachorro','idade raça nome')

#forma 2

cachorro2 = namedtuple('cachorro',['idade','raça','nome'])

ray = cachorro(idade=1,raça='dd',nome='ray')



#
#forma 1
print(ray[0])
print(ray[1])

#forma 2
print(ray.raça)
print(ray.idade)
print(ray.nome)





