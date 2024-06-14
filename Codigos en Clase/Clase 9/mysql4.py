#Metodo READ
import pymysql.connections



miConexion = pymysql.connect(host="localhost",user="root",passwd="",db="empresa")

miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS")
datos = miCursor.fetchall()

for dato in datos:
    print(dato)

miConexion.commit()
miConexion.close()