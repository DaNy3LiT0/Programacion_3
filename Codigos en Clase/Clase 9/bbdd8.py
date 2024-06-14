#CRUD UPDATE
import sqlite3
miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

#UPDATE
miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 90 WHERE NOMBRE_ARTICULO='pelota'")



miCursor.execute("SELECT * FROM PRODUCTOS")
productos = miCursor.fetchall()

for producto in productos:
    print(producto)

miConexion.commit()
miConexion.close()
