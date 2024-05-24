'''
Escribir una función que convierta un número decimal en binario y otra que
convierta un número binario en decimal.
'''


def decimal_binario(num):
    binario = bin(num).replace('0b','')
    return binario

def binario_decimal(binario):
    bin = str(binario)
    decimal = 0
    for digito in bin:
        decimal = decimal * 2 + int(digito)
    return decimal

numero = int(input('Ingrese 1 para ingresar un numero decimal o 2 para ingresar un numero binario: '))
if numero == 1:
    num = int(input('Ingrese un numero decimal: '))
    print('El numero decimal', num, 'en binario es:', decimal_binario(num))
elif numero == 2:
    binario = input('Ingrese un numero binario: ')
    print('El numero binario', binario, 'en decimal es:', binario_decimal(binario))
else:
    print('Opcion invalida')

