"""
Escribir una clase en python que calcule la potencia(x, n)
x = es la base
n = es el exponente
"""

class Potencia:
    def __init__(self):
        self.x = int(input("Ingrese el número base: "))
        self.n = int(input("Ingrese el exponente: "))

    def calcular_potencia(self):
        return self.x ** self.n

    def __str__(self):
        return f"Potencia de {self.x} elevado a {self.n}: {self.calcular_potencia()}"

# Programa Principal
potencia = Potencia()
print(potencia)  

