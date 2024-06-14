import sqlite3

miConexion = sqlite3.connect("Primera")

miCursor = miConexion.cursor()

#miCursor.execute("INSERT INTO PRODUCTOS VAlUES('PELOTA',1500,'DEPORTES')")

variosProductos=[
    ("Camiseta", 4000, "Deportes"),
    ("jarrón", 4000, "Cerámica"),
    ("Camion", 4000, "Juguetería")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)
miCursor.execute("SElECT * FROM PRODUCTOS")
variosProductos =miCursor.fetchall()

#print(variosProductos)

for producto in variosProductos:
    #print(producto)
    print(f"Nombre producto: {producto[0]} seccion: {producto[2]}")


miConexion.commit()
miConexion.close()