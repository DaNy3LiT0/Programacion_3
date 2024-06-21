""" 
Localiza  el  error  en  el  siguiente  bloque  de  código.  Crea  una  excepción  para  evitar  que  el 
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución: 
   
resultado = 15 + "20"
"""

try:
    resultado = 15 + "20"
except TypeError:
    print("Error: No se puede sumar un entero con una cadena. Por favor, asegúrese de que ambos operandos sean del mismo tipo de datos.")
    

""" 
def convertir_a_numero(valor):
    try:
        return int(valor)
    except ValueError:
        try:
            return float(valor)
        except ValueError:
            return None

while True:
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")

    num1_numero = convertir_a_numero(num1)
    num2_numero = convertir_a_numero(num2)

    if num1_numero is None or num2_numero is None:
        print("Error: Uno o ambos números ingresados no son válidos. Por favor, ingrese solo números.")
    else:
        resultado = num1_numero + num2_numero
        print("El resultado es:", resultado)
        break
"""