"""Usando el módulo sqlite3 o pymysql crea una base de datos que permita registrar y categorizar  los  gastos  personales.  Consultas  para  almacenar  los  detalles  de  los gastos,  como  la  fecha,  la  descripción,  la  categoría  y  el  monto  y  consultas  para informar sobre gastos totales por categoría, mes, año, etc."""

import sqlite3
import os
import datetime 

class GastosDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS categorías (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS gastos (id INTEGER PRIMARY KEY, fecha DATE NOT NULL, descripción TEXT NOT NULL, categoría_id INTEGER NOT NULL, monto REAL NOT NULL, FOREIGN KEY (categoría_id) REFERENCES categorías (id))''')
        self.conn.commit()

    def insert_categoría(self, nombre):
        try:
            self.cursor.execute("INSERT INTO categorías (nombre) VALUES (?)", (nombre,))
            self.conn.commit()
            print("Categoría insertada correctamente!")
        except sqlite3.IntegrityError:
            print("Ya existe una categoría con ese nombre.")

    def insert_gasto(self, fecha, descripción, categoría_id, monto):
        try:
            self.cursor.execute("INSERT INTO gastos (fecha, descripción, categoría_id, monto) VALUES (?,?,?,?)", (fecha, descripción, categoría_id, monto))
            self.conn.commit()
            print("Gasto insertado correctamente!")
        except sqlite3.IntegrityError:
            print("No se pudo insertar el gasto.")

    def get_categorías(self):
        self.cursor.execute("SELECT * FROM categorías")
        return self.cursor.fetchall()

    def get_gastos_por_categoría(self):
        self.cursor.execute("SELECT c.nombre, SUM(g.monto) AS total FROM gastos g JOIN categorías c ON g.categoría_id = c.id GROUP BY c.nombre")
        return self.cursor.fetchall()

    def get_gastos_por_mes(self):
        self.cursor.execute("SELECT strftime('%Y-%m', fecha) AS mes, SUM(monto) AS total FROM gastos GROUP BY mes")
        return self.cursor.fetchall()

    def get_gastos_por_anio(self):
        self.cursor.execute("SELECT strftime('%Y', fecha) AS año, SUM(monto) AS total FROM gastos GROUP BY año")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

def main():
    db_file = os.path.join(os.path.dirname(__file__), "gastos.db")
    db = GastosDB(db_file)
    db.create_tables()

    while True:
        print_menu()
        opción = input("Seleccione una opción: ")

        if opción == "1":
            insert_gasto(db)
        elif opción == "2":
            print_gastos_por_categoría(db)
        elif opción == "3":
            print_gastos_por_mes(db)
        elif opción == "4":
            print_gastos_por_anio(db)
        elif opción == "5":
            print("Saliendo...")
            db.close()
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def print_menu():
    print("Menú:")
    print("1. Insertar gasto")
    print("2. Consultar gastos por categoría")
    print("3. Consultar gastos por mes")
    print("4. Consultar gastos por año")
    print("5. Salir")

def insert_gasto(db):
    año = datetime.date.today().year
    while True:
        día = int(input("Ingrese el día del gasto (1-31): "))
        mes = int(input("Ingrese el mes del gasto (1-12): "))

        if día < 1 or día > 31:
            print("Día inválido. Debe ser entre 1 y 31.")
            continue

        if mes < 1 or mes > 12:
            print("Mes inválido. Debe ser entre 1 y 12.")
            continue

        # Verificar si el día es válido para el mes correspondiente
        if mes in [4, 6, 9, 11] and día > 30:
            print("Día inválido para el mes seleccionado.")
            continue
        elif mes == 2:
            if día > 28:
                print("Día inválido para febrero.")
                continue
            elif día == 29 and not es_bisiesto(año):
                print("Día inválido para febrero en un año no bisiesto.")
                continue

        break

    if día < 10:
        día_str = f"0{día}"
    else:
        día_str = str(día)

    if mes < 10:
        mes_str = f"0{mes}"
    else:
        mes_str = str(mes)

    fecha = f"{año}-{mes_str}-{día_str}"

    descripción = input("Ingrese la descripción del gasto: ")

    categorías = db.get_categorías()
    print("Seleccione una categoría:")
    for i, categoría in enumerate(categorías):
        print(f"{i+1}. {categoría[1]}")
    print(f"{len(categorías)+1}. Agregar nueva categoría")

    opción = int(input("Seleccione una opción: "))

    if opción <= len(categorías):
        categoría_id = categorías[opción-1][0]
    else:
        nombre = input("Ingrese el nombre de la nueva categoría: ")
        db.insert_categoría(nombre)
        categoría_id = db.cursor.lastrowid

    monto = float(input("Ingrese el monto del gasto: "))
    db.insert_gasto(fecha, descripción, categoría_id, monto)

def es_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def print_gastos_por_categoría(db):
    resultados = db.get_gastos_por_categoría()
    print("Gastos por categoría:")
    print("---------------")
    for row in resultados:
        print(f"{row[0].title():<20} {row[1]:>10.2f}")
    print("---------------")

def print_gastos_por_mes(db):
    resultados = db.get_gastos_por_mes()
    print("Gastos por mes:")
    print("-----------")
    for row in resultados:
        print(f"{row[0].title():<10} {row[1]:>10.2f}")
    print("-----------")

def print_gastos_por_anio(db):
    resultados = db.get_gastos_por_anio()
    print("Gastos por año:")
    print("-----------")
    for row in resultados:
        print(f"{row[0].title():<10} {row[1]:>10.2f}")
    print("-----------")
if __name__ == "__main__":
    main()