"""

print(os.getcwd())

print(os.chdir('..'))
print(os.getcwd())

print(os.path.isabs('C:/Users/danie/Desktop/Trabalhos em andamento/aulasUdemy/navegarcao.py'))

print(os.name)  nt windons
print(sys.platform)


print(os.getcwd())

res = os.path.join(os.getcwd(),'geek')
os.chdir(res)
print(os.getcwd())


"""


import os,sys
#podemos intntificar o sistema operacional

arquivo = list(os.scandir())

print(arquivo[0].inode())
print(arquivo[0].is_dir())
print(arquivo[0].is_file())

