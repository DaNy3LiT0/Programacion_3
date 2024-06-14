#Metodo UPDATE
import pymysql.connections



miConexion = pymysql.connect(host="localhost",user="root",passwd="",db="empresa")

miCursor = miConexion.cursor()
miCursor2 = miConexion.cursor()
miCursor.execute("UPDATE PRODUCTOS SET precio = 1000 WHERE nombre_articulo ='pantalon'" )
datos = miCursor.fetchall()



miCursor.execute("SELECT * FROM PRODUCTOS " )
datos = miCursor.fetchall()

for dato in datos:
    print(dato)

miConexion.commit()
miConexion.close()