"""Escribir un programa que almacene las asignaturas del 3 cuatrimestre del ITSE en una lista y la 
muestre por pantalla"""


asignaturas = []
nueva_asignatura = input("Ingrese una nueva asignatura (o ingrese ENTER para finalizar): ")

while nueva_asignatura.strip():  # Verifica si la cadena no está vacía
    asignatura_formateada = nueva_asignatura.title()
    asignaturas.append(asignatura_formateada)
    nueva_asignatura = input("Ingrese una nueva asignatura (o ingrese ENTER para finalizar): ")

print("Asignaturas del tercer cuatrimestre del ITSE:")
for asignatura in asignaturas:
    print(asignatura)

