""" 
Crea un script llamado generador.py que cumpla las siguientes necesidades: 
a. Debe incluir una función llamada leer_numero(). Esta función tomará 3 valores: ini, fin y mensaje. El objetivo es leer por pantalla un número >= que ini y <= que fin. 
Además, a la hora de hacer la lectura se mostrará en el input el mensaje enviado a la  función.  Finalmente  se  devolverá  el  valor.  Esta  función  tiene  que  devolver  un número, y tiene que repetirse hasta que el usuario no lo escriba bien (lo que incluye cualquier valor que no sea un número del ini al fin). 
b. Una vez la tengas creada, deberás crear una nueva función llamada generador, no recibirá ningún parámetro. Dentro leerás dos números con la función leer_numero(): 
    i. El primer número será llamado números, deberá ser entre 1 y 20, ambos incluidos, y se mostrará el mensaje ¿Cuantos números quieres generar? [1-20]: 
    ii. El segundo número será llamado modo y requerirá un número entre 1 y 3, ambos incluidos. El mensaje que mostrará será: ¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:. 
c. Una vez sepas los números a generar y cómo redondearlos, tendrás que realizar lo siguiente: 
i. Generarás una lista de números aleatorios decimales entre 0 y 100 con tantos números como el usuario haya indicado.
ii. A cada uno de esos números deberás redondearlos en función de lo que el usuario ha especificado en el modo
iii. Para  cada  número  muestra  durante  el  redondeo,  el  número  normal  y después del redondeo. 
d. Finalmente devolverás la lista de números redondeados.
"""

import random

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if ini <= numero <= fin:
                return numero
            else:
                print(f"El número debe estar entre {ini} y {fin}. Inténtalo nuevamente.")
        except ValueError:
            print("Por favor, ingresa un valor numérico válido.")

def generador():
    numeros = int(leer_numero(1, 20, "¿Cuántos números quieres generar? [1-20]: "))
    modo = int(leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: "))

    lista_numeros = [random.uniform(0, 100) for _ in range(numeros)]

    def redondear(numero):
        if modo == 1:
            return round(numero)
        elif modo == 2:
            return int(numero)
        else:
            return round(numero, 2)

    for num in lista_numeros:
        num_redondeado = redondear(num)
        print(f"Número original: {num:.2f} | Número redondeado: {num_redondeado:.2f}")

    return lista_numeros

if __name__ == "__main__":
    numeros_redondeados = generador()
    print("Lista de números redondeados:", numeros_redondeados)
