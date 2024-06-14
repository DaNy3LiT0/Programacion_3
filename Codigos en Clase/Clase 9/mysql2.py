#Metodo INSERT un registro
import pymysql.connections



miConexion = pymysql.connect(host="localhost",user="root",passwd="",db="empresa")

miCursor = miConexion.cursor()
miCursor2 = miConexion.cursor()
producto = ('muñeca', 500, 'jugueteria')
miCursor.execute("INSERT INTO PRODUCTOS VAlUES (%s,%s,%s)", producto)

miCursor2.execute("SELECT * FROM PRODUCTOS")
datos = miCursor2.fetchall()

for dato in datos:
    print(dato)

miConexion.commit()
miConexion.close()