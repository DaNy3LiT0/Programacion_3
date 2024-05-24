"""Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y 
muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 
dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos 
enteros y 2 decimales"""

def formatear_unidades(num):
    return "{:03d}".format(num)

def formatear_precio(precio_unid):
    entero = int(precio_unid)
    decimal = precio_unid - entero
    return "{:06d}.{:02d}".format(entero, int(decimal * 100))

def formatear_costo(precio_unid, unidades):
    entero = int(precio_unid * unidades)
    decimal = precio_unid * unidades - entero
    return "${:08d}.{:02d}".format(entero, int(decimal * 100))

##### Programa Principal #####

producto = input("Ingrese un producto: ").upper()
precio_unid = float(input("Ingrese su precio unitario: "))
unidades = int(input("Ingrese la cantidad comprada: "))

unidades_formateadas = formatear_unidades(unidades)
precio_formateado = formatear_precio(precio_unid)
costo_final = formatear_costo(precio_unid, unidades)

print(f"{producto} {precio_formateado} {unidades_formateadas} {costo_final}")
