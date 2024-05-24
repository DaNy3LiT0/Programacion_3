'''
Integrantes del Grupo: Ruiz Cinquegrani Agustin y Sarmiento Daniel.
Escribir un programa que pida al usuario un número entero. Si su valor es 2, 4 o 6
mostrar su valor en letras.
'''

'''
numero = int(input('Ingrese un numero entero: '))

if numero == 2:
    print('Dos')
elif numero == 4:
    print('Cuatro')
elif numero == 6:
    print('Seis')
else:
    print('FinPrograma')
'''
numero = int(input('Ingrese un numero entero: '))
match numero:
    case 2:
        print('Dos')
    case 4:
        print('Cuatro')
    case 6:
        print('Seis')
    case other:
        print('Opcion n')