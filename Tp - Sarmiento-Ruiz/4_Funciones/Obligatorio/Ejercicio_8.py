'''
Utilizar la función incorporada map() para crear una función que retorne una lista
con la longitud de cada palabra (separas por espacios) de una frase. La función
recibe una cadena de texto y retornara una lista.
'''


def long_palabras(frase):
    palabras = frase.split()
    longitudes = list(map(len, palabras))
    return longitudes

# Ejemplo de uso
frase = input('Ingrese una frase: ')
print(long_palabras(frase))

