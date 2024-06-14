import sqlite3

miConexion = sqlite3.connect("Primera")

miCursor = miConexion.cursor()

#Solo se ejecuta una sola vez esta instrucción
miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")


#miCursor.execute("INSERT INTO PRODUCTOS VAlUES('PELOTA',1500,'DEPORTES')")


miCursor.execute("SELECT * FROM PRODUCTOS")
datos = miCursor.fetchall()

miConexion.commit()
miConexion.close()


for dato in datos:
    print(dato)



