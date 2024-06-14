import sqlite3
miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE PRODUCTOS(CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))"
)

productos = [
    ('AR01','pelota', 600, 'juguetería'),
    ('AR02','pantalon', 1500, 'confección'),
    ('AR03','destornillador', 1000, 'ferretería'),
    ('AR04','jarrón', 1200, 'cerámica'),
]

miCursor.executemany("INSERT INTO PRODUCTOS VAlUES (?,?,?,?)",productos)

for producto in productos:
    print(producto)