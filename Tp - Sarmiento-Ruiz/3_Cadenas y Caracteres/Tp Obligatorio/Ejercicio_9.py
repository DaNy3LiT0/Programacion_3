"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al 
usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de 
fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello"""


precios_frutas = {
    "manzana roja": 1500,  # precio por kilo
    "banana ecuatoriana": 2500,
    "banana": 1500,
    "naranja": 1800,
    "pera": 2200,
    # Agrega más frutas y sus precios aquí
}

fruta = input("Ingrese el nombre de la fruta: ")
kilos = float(input("Ingrese el número de kilos: "))

if fruta in precios_frutas:
    precio = precios_frutas[fruta] * kilos
    print("El precio de {} kilos de {} es {}".format(kilos, fruta, precio))
else:
    print("Lo siento, la fruta {} no está en el diccionario.".format(fruta))
