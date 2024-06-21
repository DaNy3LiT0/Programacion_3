""" 
Localiza  el  error  en  el  siguiente  bloque  de  código.  Crea  una  excepción  para  evitar  que  el 
programa se blo1quee y además explica en un mensaje al usuario la causa y/o solución: 
          resultado = 10/0
"""

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero. Verifica que el divisor sea diferente de cero.")