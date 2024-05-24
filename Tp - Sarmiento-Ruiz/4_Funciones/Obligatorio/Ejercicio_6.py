'''
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el
diccionario generado con la función anterior y devuelva una tupla con la palabra
más repetida y su frecuencia
'''


def contar_palabras(cadena):
    palabra1 = cadena.replace(',','')
    palabra2 = palabra1.replace('.','')
    palabras3 = palabra2.split()
    frecuencias = {}
    for palabra in palabras3:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def palabra_mas_repetida(diccionario):
    palabra_max = max(diccionario, key=diccionario.get)
    return (palabra_max, diccionario[palabra_max])

cadena = input('Ingrese un texto: ')
frecuencias = contar_palabras(cadena)
print(frecuencias)
print(palabra_mas_repetida(frecuencias))

