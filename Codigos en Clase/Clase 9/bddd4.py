import sqlite3



miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()


miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR01','pelota', 600, 'juguetería') ")

miCursor.execute("SELECT * FROM PRODUCTOS")
datos = miCursor.fetchall()

miConexion.commit()
miConexion.close()

for elemento in datos:
    print(elemento)