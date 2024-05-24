"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 
'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo 
o un mensaje de aviso si la divisa no está en el diccionario
"""

divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisas_minusculas = {clave.lower(): valor for clave, valor in divisas.items()}

divisa_usuario = input("Ingrese una divisa >>>").capitalize()

if divisa_usuario in divisas:
    print(f"El símbolo de {divisa_usuario} es {divisas.get(divisa_usuario)}")
else:
    print(f"La divisa {divisa_usuario} no está en el diccionario.")
        