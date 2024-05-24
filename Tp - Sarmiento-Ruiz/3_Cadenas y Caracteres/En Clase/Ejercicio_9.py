"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo 
guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> 
tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>
"""

datos_usuario = {}

datos_usuario['nombre'] = input("Ingrese su nombre >>> ")
datos_usuario['edad'] = input("Ingrese su edad >>> ")
datos_usuario['direccion'] = input("Ingrese su direccion >>> ")
datos_usuario['telefono'] = input("Ingrese su numero telefonico >>> ")
print()
print(f"El usuario {datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {datos_usuario['direccion']}"
      f" y su número de teléfono es {datos_usuario['telefono']}")