### Sarmiento Daniel y Ruiz Cinquigrani Agustin ###

"""
Escribir un programa que pida al usuario un número entero positivo y muestre por 
pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

num = int(input("Ingrese un Numero >>> "))

impar = [str(i) for i in range (1, num+1) if i % 2 != 0]

print (", ".join(impar))
        
