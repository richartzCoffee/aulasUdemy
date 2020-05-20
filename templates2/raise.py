"""
Não é uma função

raise -> llança execoues

obs não é uma função é uam palavra reservada

o raise assim como o return finaliza a função


"""

def color(Tex,color):
    cores = ["azul","verde"]
    if type(Tex) is not str:
        raise TypeError("Texto precisa ser um string")
    if type(color) is not str:
        raise TypeError("cor tem que ser uma string")
    if color not in cores:
        raise ValueError(f"a cor precisa estar dentro dos parametro {cores}")

    print(Tex)
    print(color)

color("azul","azul")
