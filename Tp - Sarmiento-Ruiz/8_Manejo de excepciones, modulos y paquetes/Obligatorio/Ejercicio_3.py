""" 
Localiza  el  error  en  el  siguiente  bloque  de  código.  Crea  una  excepción  para  evitar  que  el 
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución: 
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }  
colores['blanco']
"""

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }  

try:
    color_es = 'blanco'
    color_en = colores[color_es]
    print(f"El color {color_es} en inglés es {color_en}")
except KeyError as e:
    print(f"Error: El color '{e.args[0]}' no existe en el diccionario. Por favor, seleccione un color válido.")
    
    
""" Ingreso manual...

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }  

color_es = input("Ingrese un color en español: ")

try:
    color_en = colores[color_es]
    print(f"El color {color_es} en inglés es {color_en}")
except KeyError as e:
    print(f"Error: El color '{e.args[0]}' no existe en el diccionario. Por favor, seleccione un color válido.")

"""