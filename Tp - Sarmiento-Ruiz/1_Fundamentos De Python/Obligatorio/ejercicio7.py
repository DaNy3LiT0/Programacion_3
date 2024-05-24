'''
Integrantes del Grupo: Ruiz Cinquegrani Agustin y Sarmiento Daniel.
Escribir un programa que pida al usuario dos números enteros y muestre por
consola lo siguiente: <n> dividido <m> da un cociente <c> y un resto <r> donde
<n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente
y el resto de la división entera respectivamente.
'''

n = int(input('Ingrese un numero entero: '))
m = int(input('Ingrese otro numero entero: '))

c = n // m
r = n % m

print(f"{n} divido {m} da un cociente {c} y un resto {r} \n"
      f"donde {n} y {m} son los numeros introducidos por el usuario y,\n"
      f"{c} y {r} son el cociente y el resto de la division entera respectivamente")
