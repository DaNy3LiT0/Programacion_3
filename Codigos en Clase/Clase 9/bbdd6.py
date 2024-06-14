#UNIQUE
import sqlite3
miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

miCursor.execute(
    '''
    CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20))
    '''
    )
productos = [
    ('pelota', 600, 'juguetería'),
    ('pantalon', 1500, 'confección'),
    ('destornillador', 1000, 'ferretería'),
    ('jarrón', 1200, 'cerámica'),
    ('pantalones', 3500, 'confección'),
]

miCursor.executemany("INSERT INTO PRODUCTOS VAlUES (NULL,?,?,?)",productos)

registros = miCursor.execute("SELECT * FROM PRODUCTOS")

for registro in registros:
    print(registro)
    
    
miConexion.commit()
miConexion.close()
