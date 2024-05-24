"""
Escribir una función que reciba otra función y una lista, y devuelva otra lista con el 
resultado de aplicar la función dada a cada uno de los elementos de la lista
"""

def crear_lista(n):
    lista = []
    for i in range(n):
        num = int(input("Ingrese el elemento de la lista >>> "))
        lista.append(num)
    input("Presione ENTER para continuar >>> ")
    return lista

### Programa Principal ###
n = int(input("Ingrese la cantidad de elementos que tendra la lista >>> "))

lista_numeros = crear_lista(n)


print(lista_numeros)



