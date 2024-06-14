#CRUD DELETE
import sqlite3
miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

#DELETE
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")



miCursor.execute("SELECT * FROM PRODUCTOS")
productos = miCursor.fetchall()

for producto in productos:
    print(producto)

miConexion.commit()
miConexion.close()
