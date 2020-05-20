"""

print(os.path.exists('texto.txt'))

os.mkdir('templats/daniel') um de cada vez
os.makedirs('daniel/d/t/a') cria varios

if not os.path.exists('templats'):
    #os.mknod('daniel.txt')
    os.mkdir('templats')
    print("poi")


os.makedirs('daniel/d',exist_ok=True)

os.rename('templats','templates2')

os.rename('daniel/d/t/a','daniel/d/t/f')

os.remove('texto.txt')

print(list(os.scandir()))

for arquivo in os.scandir("daniel/d/t"):
    print(f'{arquivo.name}')
    if arquivo.is_file():
      os.remove(arquivo.path)

os.removedirs('daniel/d/t ')

import bilbioteca sandTrash



with tempfile.TemporaryDirectory() as tmp:

    with open(f'{tmp}/aqquivo.txt','w') as tempo:
        tempo.write('teste')
    input()


em arquivos temporarios so escrevemos bits



arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'danieldada')
print(arquivo.read())


arquivo.closed



"""


import os
import tempfile


