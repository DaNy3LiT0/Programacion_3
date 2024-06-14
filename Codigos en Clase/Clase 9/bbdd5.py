#ID AUTOINCREMENTABLE
import sqlite3
miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

miCursor.execute(
    '''
    CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20))
    '''
    )
productos = [
    ('pelota', 600, 'juguetería'),
    ('pantalon', 1500, 'confección'),
    ('destornillador', 1000, 'ferretería'),
    ('jarrón', 1200, 'cerámica'),
]

miCursor.executemany("INSERT INTO PRODUCTOS VAlUES (NULL,?,?,?)",productos)

for producto in productos:
    print(producto)