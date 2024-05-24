"""Escribir una clase en python que revierta una cadena de palabras
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi" 
"""

""" 
class Reversa:
    def __init__(self, cadena):
        self.cadena = cadena

    def invertir_palabras(self):
        palabras = self.cadena.split()
        palabras_invertidas = palabras[::-1]
        self.cadena = " ".join(palabras_invertidas)

    def __str__(self):
        return self.cadena

# Programa Principal
reversa = Reversa("Mi Diario Python")
reversa.invertir_palabras()
print(reversa)   
"""


### Lo mismo pero pidiendo que ingrese una frase ###
class Reversa:
    def __init__(self):
       self.cadena = input("Ingrese una frase: ")

    def invertir_palabras(self):
        palabras = self.cadena.split()
        palabras_invertidas = palabras[::-1]
        self.cadena = " ".join(palabras_invertidas)

    def __str__(self):
       return self.cadena

reversa = Reversa()
reversa.invertir_palabras() 
print(reversa) 
