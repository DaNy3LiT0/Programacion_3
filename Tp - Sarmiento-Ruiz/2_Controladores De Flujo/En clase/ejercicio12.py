'''
Integrantes del Grupo: Ruiz Cinquegrani Agustin y Sarmiento Daniel.
Leer números enteros, y contar la cantidad de pares e impares que se han ingresado
hasta que se ingrese un número negativo.
'''
numpar = 0
numimpar = 0

while True:
    numero = int(input('Ingrese un numero: '))
    if numero >= 0:
        if numero%2 == 0:
            numpar += 1
        else:
            numimpar += 1
    else:
        print(f'La cantidad de numeros pares ingresados es: {numpar} y la '
            f'cantidad de numeros impares ingresados son: {numimpar}.')
        break

