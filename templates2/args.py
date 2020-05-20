

'''
o args serve para passar parametros ´pdensod chamr qualuqrr coisa se colocar o asterisco na frente.


*args

assim vc pode passar varios parametros não descritos para uma tupla


'''

def teste(*args):
    print(args)


teste(1,2,3,4,4,4,4)

te= [1,2,3,4,5,1,4]

teste(*te)
