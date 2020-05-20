"""
LEitura de aruivos

função integrada open

OBs se o arquivo n existir ele retorn um FileNotErro
"""

arquivo = open('texto.txt',encoding='UTF-8').read()

print(type(arquivo))
print(arquivo)
