"""Los teléfonos de una empresa tienen el siguiente formato prefijo-9-codigo de área-
extensión-número donde el prefijo es el código del país +n 34, y la extensión tiene dos 
dígitos (15) y el código de area (385). Escribir un programa que pregunte por un número de 
teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo sin el 9 y sin 
extensión
"""

##### Programa Principal #####

numero_completo = str(input("Por favor ingrese su numero telefonico, utilizadando el siguiente formato sin ()\n"
            "+(cod pais)-9-(cod area)-15-(numero) "))
if len(numero_completo) == 20:
        separo = numero_completo.split("-")
        cod_area = separo[2]
        numero = separo[4]
        resultado = cod_area + "-" + numero
        
print("El número de teléfono sin el prefijo, sin el 9 y sin la extensión es: ",resultado)
    
    