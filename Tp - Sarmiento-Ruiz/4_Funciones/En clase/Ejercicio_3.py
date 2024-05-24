"""
Escribir una función que reciba un número entero positivo y devuelva su factorial
"""

def factorial(numero):
    resultado = 1
    for i in range(1,numero+1):
        resultado *= i
    
    return resultado
   

### Programa Principal ###

numero = 5
factorial(numero)
print(f"El Factorial de {numero} es: {factorial(numero)}")
    