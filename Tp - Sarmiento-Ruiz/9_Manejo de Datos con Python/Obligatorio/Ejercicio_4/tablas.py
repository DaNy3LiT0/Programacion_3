"""Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido."""

"""Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido."""

import os

def guardar_tabla_de_multiplicar():
    número = int(input("Introduce un número entero entre 1 y 10: "))
    while número < 1 or número > 10:
        print("Error: el número debe estar entre 1 y 10")
        número = int(input("Introduce un número entero entre 1 y 10: "))

    ruta_archivo_actual = os.path.dirname(__file__)
    nombre_archivo = f"tabla-{número}.txt"
    ruta_completa = os.path.join(ruta_archivo_actual, nombre_archivo)

    with open(ruta_completa, "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{número} x {i} = {número * i}\n")

    print(f"Tabla de multiplicar del {número} guardada en {ruta_completa}")

guardar_tabla_de_multiplicar()