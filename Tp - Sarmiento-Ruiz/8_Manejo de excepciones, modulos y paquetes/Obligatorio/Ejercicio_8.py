""" Diseñe  un sistema de  lotería  en donde se solicita al  usuario que construya  un  diccionario donde la clave es el número comprado por la persona y el valor es el nombre de la misma.  
La lotería entrega 5 premios: 
o 1 premio: Un viaje a Turquía con todo pago 
o 2 premio: auto 
o 3 premio: una motocicleta 
o 4 premio: una notebook 
o 5 premio: una bicicleta    
Genere 5 números aleatorios para definir los ganadores teniendo en cuenta que el  número comprado tiene tres dígitos. Por ejemplo: 003, 050, 850. 
Finalmente muéstrelos nombres de los ganadores y los premios ganados """

import random

def crear_diccionario():
    diccionario = {}
    while True:
        nombre = input("Ingrese su nombre: ")
        numero_comprado = input("Ingrese el número comprado (tres dígitos): ")
        if len(numero_comprado) == 3 and numero_comprado.isdigit():
            diccionario[numero_comprado] = nombre
            print("Número agregado correctamente.")
        else:
            print("El número debe tener tres dígitos. Inténtalo nuevamente.")
        respuesta = input("¿Desea agregar otro número? (s/n): ")
        if respuesta.lower() != 's':
            break
    return diccionario

def generar_ganadores(diccionario):
    premios = ["Un viaje a Turquía con todo pago", "Un auto", "Una motocicleta", "Una notebook", "Una bicicleta"]
    ganadores = random.sample(list(diccionario.keys()), 5)
    for i, ganador in enumerate(ganadores):
        print(f"El ganador del premio {i+1} es {diccionario[ganador]} con el número {ganador}. Premio: {premios[i]}")

def main():
    diccionario = crear_diccionario()
    generar_ganadores(diccionario)

if __name__ == "__main__":
    main()