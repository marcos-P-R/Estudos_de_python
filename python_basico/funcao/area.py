import math
def quadrado(altura):
    return pow(altura, 2)

def retangulo(altura, base):
    return altura * base

def triangulo(altura, base):
    return (altura * base) / 2

def circulo(raio):
    return math.pi * pow(raio, 2)

def trapesio(base_menor, base_maior, altura):
    return ((base_maior + base_menor) * altura) / 2