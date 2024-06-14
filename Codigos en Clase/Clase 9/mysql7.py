#Metodo DELETE
import pymysql.connections



miConexion = pymysql.connect(host="localhost",user="root",passwd="",db="empresa")

miCursor = miConexion.cursor()
miCursor2 = miConexion.cursor()

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")


datos = miCursor.fetchall()

miCursor2.execute("SELECT * FROM PRODUCTOS " )
datos = miCursor2.fetchall()

for dato in datos:
    print(dato)

miConexion.commit()
miConexion.close()