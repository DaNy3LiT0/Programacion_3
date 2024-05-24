"""
Escribir un programa que pida al usuario una palabra y
muestre por pantalla el número de veces que contiene cada vocal
"""

def MostrarVocales(palabra):
    a, e, i, o, u = 0, 0, 0, 0, 0
    
    for y in range(len(palabra)):
        if palabra[y].lower() == 'a':
            a += 1
        elif palabra[y].lower()== 'e':
            e += 1
        elif palabra[y].lower() == 'i':
            i += 1
        elif palabra[y].lower() == 'o':
            o += 1
        elif palabra[y].lower() == 'u':
            u += 1
    return a, e, i, o, u

palabra = str(input("Ingrese una palabra >>> "))
a, e, i, o, u = MostrarVocales(palabra)
print("La palabra ingresada tiene repetidas las vocales en su contenido esta cantidad de veces...\n"
      f"la vocal 'a' = {a}\n"
      f"la vocal 'e' = {e}\n"
      f"la vocal 'i' = {i}\n"
      f"la vocal 'o' = {o}\n"
      f"la vocal 'u' = {u}")