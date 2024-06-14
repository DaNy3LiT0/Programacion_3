#Metodo ID
import pymysql.connections



miConexion = pymysql.connect(host="localhost",user="root",passwd="",db="empresa")

miCursor = miConexion.cursor()
miCursor2 = miConexion.cursor()



miCursor.execute("CREATE TABLE PRODUCTOS(ID INTEGER PRIMARY KEY AUTO_INCREMENT,NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, CATEGORIA_ARTICULO VARCHAR(50))")

datos = miCursor.fetchall()

#miCursor2.execute("SELECT * FROM PRODUCTOS " )
#datos = miCursor2.fetchall()

#for dato in datos:
#    print(dato)

miConexion.commit()
miConexion.close()