'''

Modulo collection : ordered Dict

dicionario não garatne a order

'''

from collections import OrderedDict

dicionario = OrderedDict({'a':1,'b':2,'c':3,'d' :'4'})
print(dicionario)



#dic comum
dic1 = {'a':1,'b':2,'c':3,'d' :'4'}
dic2 = {'b':1,'a':2,'d':3,'c' :'4'}

print(dic1 == dic2) #ordem não importa

#orde dict

dic1 = OrderedDict({'a':1,'b':2,'c':3,'d' :'4'})
dic2 = OrderedDict({'b':1,'a':2,'d':3,'c' :'4'})

print(dic1 == dic2) #ordem importa