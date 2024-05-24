'''
Integrantes del grupo: Ruiz Cinquegrani, Agustin Diego. y Sarmiento, Daniel.
Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
'''


numero1 = int(input('Ingrese un numero para el dividendo: '))
numero2 = int(input('Ingrese un numero para el divisor: '))


if numero2 != 0:
    print(numero1/numero2)
else:
    print('error, ingrese un numero mayor que 0')
