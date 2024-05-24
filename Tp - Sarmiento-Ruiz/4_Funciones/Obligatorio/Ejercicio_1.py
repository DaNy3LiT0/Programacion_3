'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y
el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA,
deberá aplicar un 21%.
'''


def cal_iva(n1, n2):
    if n2 != "":
        resultado = n1+((n1*n2)//100)
        return resultado
    else:
        n2 = 21
        resultado = n1+((n1*n2)//100)
        return resultado

total = int(input('Ingrese el total de la factura: '))
iva = input('Ingrese el iva a aplicar: ')


print(f'El total mas iva es ${cal_iva(total,iva)}')
