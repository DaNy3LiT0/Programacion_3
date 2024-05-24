'''
Integrantes del grupo: Ruiz Cinquegrani, Agustin Diego. y Sarmiento, Daniel.
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
ingresos iguales o superiores a 300000 pesos mensuales. Escribir un programa que
pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario
tiene que tributar o no.
'''


nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
ingresos = int(input('Ingrese su nacionalidad: '))

if ingresos >= 300000 and edad > 16:
    print(f'El usuario {nombre} tiene que tributar.')
else:
    print(f'El usuario {nombre} no tiene que tributar.')

