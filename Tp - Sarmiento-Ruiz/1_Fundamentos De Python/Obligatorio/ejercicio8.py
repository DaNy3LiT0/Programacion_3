'''
Integrantes del Grupo: Ruiz Cinquegrani Agustin y Sarmiento Daniel.
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión.
'''

def inversion(dinero, tasa, anios):

    interes = int(dinero*((tasa/100)*anios))
    resultado = dinero + interes
    print(f'El interes generado es ${interes} mas el dinero invertido ${dinero} da como capital ${resultado}.')

dinero = int(input('Ingrese la cantidada de dinero a invertir: $'))
tasa = float(input('Ingrese el interes anual: '))
anios = int(input('Ingrese la cantidad de años: '))

inversion(dinero, tasa, anios)
