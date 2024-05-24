"""Escribir una clase en python llamada circulo que contenga un radio, con un método 
que devuelva el área y otro que devuelva el perímetro del circulo"""

import math

class Circulo:
    def __init__(self):
        self.radio = float(input("Por favor, ingresa el radio del círculo: "))

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio


c = Circulo()
print("Área: ", c.area())
print("Perímetro: ", c.perimetro())
