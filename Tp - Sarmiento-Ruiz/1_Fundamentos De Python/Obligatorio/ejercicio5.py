'''
Integrantes del Grupo: Ruiz Cinquegrani Agustin y Sarmiento Daniel.
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
coste por hora. Después debe mostrar por consola la paga que le corresponde.
'''

horas_trabajadas = int(input('ingrese la cantidad de horas trabjadas: '))

coste_horas = int(input('ingrese el coste de las horas: '))

resultado = horas_trabajadas * coste_horas

print(f'El monto a pagar es ${resultado}')