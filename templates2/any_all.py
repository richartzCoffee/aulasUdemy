"""
Any _ all

all() -> retorna true se todos os interaveis são verdadeiros ou se o interavel esta vazio

"""
nomes = ['Daniel','Darla','Dianna']

nun = [0,1,2,3,4,5,6,7,88,8]

print(all(['0',1121212,1,4]))

print([nome[0].upper() == 'D' for nome in nomes])

print(all([nome[0].upper() == 'D' for nome in nomes]))

print([letra  for letra in 'dddd' if letra in 'aeiou'])

print(all([letra  for letra in 'aieou' if letra in 'aeiou']))

print(any(nomes))
print(any(nun))
nun = ["",0,"1"]
print(any(nun))


