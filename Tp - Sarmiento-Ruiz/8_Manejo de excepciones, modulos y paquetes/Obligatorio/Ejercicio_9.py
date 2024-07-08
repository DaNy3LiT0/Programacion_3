"""Diseñe un diccionario que tome como entrada un texto de al menos diez líneas y muestre un listado de las 10 palabras más frecuentes (use la función collections-counte"""

import collections
import re

def contar_palabras(texto):
    # Eliminar signos de puntuación y convertir a minúsculas
    texto_limpio = re.sub(r'[^\w\s]', '', texto).lower()
    
    # Dividir el texto en palabras
    palabras = texto_limpio.split()
    
    # Contar la frecuencia de cada palabra
    contador = collections.Counter(palabras)
    
    # Mostrar las 10 palabras más frecuentes
    return contador.most_common(10)

# Entrada de texto
texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

# Llamar a la función y mostrar el resultado
resultado = contar_palabras(texto)
print("Las 10 palabras más frecuentes son:")
for palabra, frecuencia in resultado:
    print(f"{palabra}: {frecuencia}")