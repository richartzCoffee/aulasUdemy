"""
Modos de leituras

r -> ab qre para a leitura
w -> abre para a escrita
x -> abre para a esscrita somente se o arquivo não exixtir caso exista gera falha
a -> adiciona linhas no final do arquivo

"""
with open('texto.txt','r+') as file:
    print(file.read())

    file.write("daniel no iaaaaaaaanwwicio\ndo\narquivo\n\n\n")