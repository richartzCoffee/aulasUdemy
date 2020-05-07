'''
print(dicionario)

caso vc coloque uma chabve que não exite

Default Dict -> Ao criar um dicionario, infomamos pela funçõa lambada um valor que
caso informar um valor que não esta escrito retorna esse valor.

lambdas são funções sem nome, que podem ou não reveber parametros de entrada.


'''

from collections import defaultdict

dicionario = defaultdict(lambda :0)

dicionario['teste'] = 'funciona assim'

print(dicionario)

print(dicionario['sim']) #chave que não exite

