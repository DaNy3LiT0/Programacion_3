import os
import sqlite3


def agregar_producto(nombre, descripcion, precio, cantidad, cursor, conn):
    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, precio, cantidad)
        VALUES (?,?,?,?);
    """, (nombre, descripcion, precio, cantidad))
    conn.commit()

def actualizar_cantidad(id_producto, cantidad, cursor, conn):
    cursor.execute("""
        UPDATE productos SET cantidad =? WHERE id =?;
    """, (cantidad, id_producto))
    conn.commit()

def ranking_mas_vendidos(cursor):
    cursor.execute("""
        SELECT * FROM productos ORDER BY vendidos DESC LIMIT 10;
    """)
    return cursor.fetchall()

def incrementar_ventas(id_producto, cursor, conn):
    cursor.execute("""
        UPDATE productos SET vendidos = vendidos + 1 WHERE id =?;
    """, (id_producto,))
    conn.commit()

def menu():
    print("Menú:")
    print("1. Agregar producto")
    print("2. Actualizar cantidad disponible")
    print("3. Incrementar ventas")
    print("4. Obtener ranking de productos más vendidos")
    print("5. Salir")

def main():
    # Obtener la ruta de la carpeta donde se encuentra el archivo .py
    script_dir = os.path.dirname(__file__)

# Crear conexión a la base de datos en la misma carpeta
    conn = sqlite3.connect(os.path.join(script_dir, 'inventario.db'))
    cursor = conn.cursor()

    # Crear tabla productos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL,
            vendidos INTEGER NOT NULL DEFAULT 0
        );
    """)

    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad disponible del producto: "))
            agregar_producto(nombre, descripcion, precio, cantidad, cursor, conn)
            print("Producto agregado correctamente!")

        elif opcion == "2":
            id_producto = int(input("Ingrese el ID del producto: "))
            cantidad = int(input("Ingrese la nueva cantidad disponible: "))
            actualizar_cantidad(id_producto, cantidad, cursor, conn)
            print("Cantidad actualizada correctamente!")

        elif opcion == "3":
            id_producto = int(input("Ingrese el ID del producto: "))
            incrementar_ventas(id_producto, cursor, conn)
            print("Venta registrada correctamente!")

        elif opcion == "4":
            ranking = ranking_mas_vendidos(cursor)
            print("Ranking de productos más vendidos:")
            for producto in ranking:
                print(f"{producto[1]} - Vendidos: {producto[5]}")

        elif opcion == "5":
            print("Adiós!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    main()