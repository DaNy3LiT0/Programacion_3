"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un 
palíndromo
"""

def palindromo(palabra):
    if palabra == palabra[::-1]:
        print (f"La palabra ingresesada '{palabra.upper()}' es un palindromo")
    else:
        print (f"La palabra ingresesada '{palabra.upper()}' NO es un palindromo")
    
    
palabra = str(input("Ingrese una palabra >>> "))
palindromo(palabra)