### Sarmiento Daniel y Ruiz Cinquigrani Agustin ###

"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

capital = float(input("Ingrese el Capital a Invertir >>> "))
interes = float(input("Ingrese el TNA actual en el mercado >>> "))
anios = int(input("Ingrese el tiempo de inversion expresada en Años >>> "))

for i in range(1, anios + 1):
    capital *= 1 + interes / 100
    print(f"El capital obtenido en el año {i} es: {capital}")

