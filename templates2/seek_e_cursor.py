"""
Seek e Cursor

seek -> movimentar o cursor do texto
print(file.read())
file.seek(0)

if not file.closed:
    f = file.read()
    file.seek(0)

    for i in f.split("\n"):
        print(file.readline(),end='')
    file.seek(0)

    print(file.readlines())

file.close()

"""

file = open('texto.txt')

print(file.read())

file.close()

