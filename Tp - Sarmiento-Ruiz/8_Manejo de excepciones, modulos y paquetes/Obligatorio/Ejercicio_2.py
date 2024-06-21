"""
Localiza  el  error  en  el  siguiente  bloque  de  código.  Crea  una  excepción  para  evitar  que  el 
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución: 
lista = [1, 2, 3, 4, 5] 
lista[10]
"""

lista = [1, 2, 3, 4, 5]

try:
    print(lista[10])
except IndexError as ie:
    print("Error: El índice está fuera de rango. Por favor, ingrese un índice válido entre 0 y", len(lista) - 1)
    
    """     
lista = [1, 2, 3, 4, 5]

indice_ingresado = int(input("Ingrese un índice: "))

try:
    if indice_ingresado >= len(lista):
        raise IndexError("El índice está fuera de rango")
    print(lista[indice_ingresado])
except IndexError as ie:
    print("Error:", ie)
    """
    
# en los ejemplos anteriores suponemos que el usuario conoce que las los indeces en python comienzan en 0, pero en el caso de que no lo sepa es importante proporcionar un mensaje de error que sea claro y fácil de entender

""" 
lista = [1, 2, 3, 4, 5]

indice_ingresado = int(input("Ingrese un índice: "))

try:
    if indice_ingresado < 1 or indice_ingresado > len(lista):
        raise IndexError("El índice debe estar entre 1 y {}".format(len(lista)))
    print(lista[indice_ingresado - 1])  # Restamos 1 para compensar el índice que empieza en 1
except IndexError as ie:
    print("Error:", ie)
"""