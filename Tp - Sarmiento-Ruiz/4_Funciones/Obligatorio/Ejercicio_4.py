'''
Escribir una función que reciba una frase y devuelva un diccionario con las palabras
que contiene y su longitud.
'''

def palabras_y_longitud(frase):
    palabras = frase.split()
    resultado = {}
    for palabra in palabras:
        resultado[palabra] = len(palabra)
    return resultado


texto = input('Ingrese una frase: ')
print(palabras_y_longitud(texto))