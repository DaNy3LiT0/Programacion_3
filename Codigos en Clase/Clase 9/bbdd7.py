#CRUD READ
import sqlite3
miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

#UPDATE
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")



miCursor.execute("SELECT * FROM PRODUCTOS")
productos = miCursor.fetchall()

for producto in productos:
    print(producto)
    
    
miConexion.commit()
miConexion.close()
