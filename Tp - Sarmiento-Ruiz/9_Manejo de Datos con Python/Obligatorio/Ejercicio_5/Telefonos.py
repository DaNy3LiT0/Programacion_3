"""Escribir  un  programa  para  gestionar  un  listado  telefónico  con  los  nombres  y  los teléfonos de los clientes de una empresa. El programa debe incorporar funciones para crear el listado si no existe, para consultar el teléfono de un cliente, añadir el 
teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listado debe estar guardado  en  el  fichero  de  texto  listado  donde  el  nombre  del  cliente  y  su  teléfono deben aparecer separados por comas y cada cliente en una línea distinta."""

import os

def crear_listado():
    ruta_listado = os.path.join(os.path.dirname(__file__), "listado.txt")
    if not os.path.exists(ruta_listado):
        with open(ruta_listado, "w") as f:
            pass

def consultar_teléfono():
    ruta_listado = os.path.join(os.path.dirname(__file__), "listado.txt")
    if not os.path.exists(ruta_listado):
        print("El archivo de listado no existe")
        return
    with open(ruta_listado, "r") as f:
        clientes = [linea.strip().split(",") for linea in f]
        print("Clientes y teléfonos:")
        for cliente, teléfono in clientes:
            print(f"{cliente}: {teléfono}")

def agregar_cliente(nombre, teléfono):
    ruta_listado = os.path.join(os.path.dirname(__file__), "listado.txt")
    with open(ruta_listado, "a") as f:
        f.write(f"{nombre},{teléfono}\n")

def eliminar_cliente():
    ruta_listado = os.path.join(os.path.dirname(__file__), "listado.txt")
    with open(ruta_listado, "r") as f:
        clientes = [linea.strip().split(",") for linea in f]
    print("Clientes activos:")
    for i, (cliente, teléfono) in enumerate(clientes, start=1):
        print(f"{i}. {cliente}: {teléfono}")
    opción_eliminar = input("Seleccione el número del cliente que desea eliminar: ")
    try:
        opción_eliminar = int(opción_eliminar)
        if opción_eliminar < 1 or opción_eliminar > len(clientes):
            print("Opción inválida")
            return
        cliente_eliminar = clientes[opción_eliminar - 1][0]
        with open(ruta_listado, "w") as f:
            for cliente, teléfono in clientes:
                if cliente!= cliente_eliminar:
                    f.write(f"{cliente},{teléfono}\n")
        print(f"Cliente {cliente_eliminar} eliminado con éxito")
    except ValueError:
        print("Opción inválida")

def main():
    crear_listado()

    while True:
        print("1. Consultar teléfono")
        print("2. Agregar cliente")
        print("3. Eliminar cliente")
        print("4. Salir")
        opción = input("Seleccione una opción: ")

        if opción == "1":
            consultar_teléfono()
        elif opción == "2":
            nombre = input("Ingrese el nombre del cliente: ")
            teléfono = input("Ingrese el teléfono del cliente: ")
            agregar_cliente(nombre, teléfono)
            print(f"Cliente {nombre} agregado con éxito")
        elif opción == "3":
            eliminar_cliente()
        elif opción == "4":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()