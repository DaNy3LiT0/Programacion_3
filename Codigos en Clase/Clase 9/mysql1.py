
#Metodo Cread
import pymysql.connections



miConexion = pymysql.connect(host="localhost",user="root",passwd="",db="empresa")

miCursor = miConexion.cursor()


miCursor.execute("CREATE TABLE PRODUCTOS( NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, CATEGORIA_ARTICULO VARCHAR(50))")

datos = miCursor.fetchall()
for dato in datos:
    print(dato)

miConexion.commit()
miConexion.close()