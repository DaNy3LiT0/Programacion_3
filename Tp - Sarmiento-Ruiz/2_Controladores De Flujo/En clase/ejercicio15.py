'''
Integrantes del Grupo: Ruiz Cinquegrani Agustin y Sarmiento Daniel.
Escribir en pantalla los múltiplos de 3 entre 1 y 100. Sumarlos, y mostrar
la suma al final.
'''

resultado = 0

for i in range (1,101):
    if i%3 == 0:
        resultado += i
        print(i)

print(resultado)

