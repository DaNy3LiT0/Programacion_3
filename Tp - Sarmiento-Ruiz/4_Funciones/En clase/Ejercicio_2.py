"""
Escribir una función a la que se le pase una cadena <nombre> y muestre por 
pantalla el saludo ¡hola <nombre>!

"""

def saludar(nombre):
    print(f"¡Hola {nombre.capitalize()}!")
    

### Programa Principal ###

nombre = str(input("Ingrese su nombre >>> "))
saludar (nombre)