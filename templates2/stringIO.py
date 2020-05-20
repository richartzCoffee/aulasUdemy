"""
String IO

ATENÇÂO: para ler ou escrevera arquivsa é preciso ter permição

string io -> utilizados para gerar aqrquivos gravados na memoria
"""

from io import StringIO

mensagem = 'normal daniPaz'

arquivo = StringIO(mensagem)

ar = arquivo.read().replace('normal','danieeeeellllllllllllllllllllll')
print(ar)


