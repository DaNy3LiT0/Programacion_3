'''
Integrantes del Grupo: Ruiz Cinquegrani Agustin y Sarmiento Daniel.
Escribir un programa que pida al usuario un número entero. Si es mayor de 10,
mostrar si es par o impar.
'''

numero = int(input('Ingrese un numero entero: '))

if numero > 10:
    if numero%2 == 0:
        print('El numero es par')
    else:
        print('El numero es impar')
else:
    print('el numero es menor que 10')


