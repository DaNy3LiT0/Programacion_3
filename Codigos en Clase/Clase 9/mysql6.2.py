import pymysql.connections

miConexion = pymysql.connect(host="localhost",user="root",passwd="",db="empresa")

miCursor = miConexion.cursor()
miCursor2 = miConexion.cursor()
producto = ('muñeca', 500, 'jugueteria')

productos = [
    ('pelota', 600, 'juguetería'),
    ('pantalon', 1500, 'confección'),
    ('destornillador', 1000, 'ferretería'),
    ('jarrón', 1200, 'cerámica'),
    ('pantalones', 3500, 'confección'),
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,%s,%s,%s)", productos)

miCursor2.execute("SELECT * FROM PRODUCTOS")
datos = miCursor2.fetchall()

for dato in datos:
    print(dato)

miConexion.commit()
miConexion.close()