'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería de un
determinado día, los almacene en una lista y los muestre por pantalla ordenados de
menor a mayor.
'''


numeros = input("Ingrese los numeros ganadores de la loteria, separados por comas: ")

numeros_ganadores = [int(numero) for numero in numeros.split(',')]
numeros_ganadores.sort()

for numero in numeros_ganadores:
    print(numero, end=', ')

