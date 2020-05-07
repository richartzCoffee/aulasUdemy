
'''

paracido com o args porem em vez de tuplas desenpacota dicionarios




'''

def cores(**kwargs):
    for p, i in kwargs.items():
        print(f"{i} {p}")
    print(kwargs)

cores(da=1,f=4,i=7)


def comprimeto(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] =='d':
        print("sim")
    elif 'geek' in kwargs:
        print("n")
    else:
        print("sei la")

comprimeto(geek='5')


#ordem correta

def ordem(obrigatorio,*args,talvez=True,**kwargs):
    print(f"{obrigatorio} {args} {talvez} {kwargs}")

ordem(4,5,4,4,4,5,5,4,6,daniel = 45)

da= {'daniel' : 45,'d':4}

ordem(4,5,4,4,4,5,5,4,6,**da)