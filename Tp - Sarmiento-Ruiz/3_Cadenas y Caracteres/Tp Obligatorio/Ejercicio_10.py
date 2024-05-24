"""Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las
palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> 
separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. 
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si 
una palabra no está en el diccionario debe dejarla sin traducir"""


traducciones = {}

while True:
    entrada_usuario = input("Introduce una palabra en español y su traducción en inglés separadas por dos puntos (o presiona Enter para finalizar): ")
    if entrada_usuario == "":
        break
    palabra, traduccion = entrada_usuario.split(":")
    traducciones[palabra.strip()] = traduccion.strip()

frase_espanol = input("Introduce una frase en español: ")

palabras_espanol = frase_espanol.split()

traduccion_frase = []

for palabra in palabras_espanol:
    if palabra in traducciones:
        traduccion_frase.append(traducciones[palabra])
    else:
        traduccion_frase.append(palabra)

print("Traducción:", " ".join(traduccion_frase))