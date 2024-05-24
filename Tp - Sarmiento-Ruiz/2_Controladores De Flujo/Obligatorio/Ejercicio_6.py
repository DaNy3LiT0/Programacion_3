'''
Integrantes del grupo: Ruiz Cinquegrani, Agustin Diego. y Sarmiento, Daniel.
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El
programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar
3000 pesos y si es mayor de 18 años, 10.000 pesos.
'''


edad = int(input('Ingrese la edad del cliente'))

if edad < 4:
    print('El precio de la entrada es: "Gratis"')
elif edad >= 4 and edad <= 18:
    print('El precio de la entrada es: "$3000"')
elif edad > 18:
    print('El precio de la entrada es: "$10000"')
else:
    print('FinPrograma')
