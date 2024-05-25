'''
Escribir una función reciba un diccionario con las asignaturas y las notas de un 
alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las 
calificaciones correspondientes a las notas aprobadas
'''

def aprobadas(total_asignaturas):
    asignaturas_aprobadas ={}
    for materia, nota in total_asignaturas.items():
        if nota >= 6:
            asignaturas_aprobadas[materia.upper()] = nota
    return asignaturas_aprobadas



### Programa Principal ###

total_asignaturas = {}

while True:
    materia = input("Ingresa el nombre de la asignatura (o ENTER para terminar): ")
    if materia.lower() == "":
        break
    nota = int(input(f"Ingresa la nota obtenida en {materia}: "))
    total_asignaturas[materia] = nota

asignaturas_aprobadas = aprobadas(total_asignaturas)
for materia, nota in asignaturas_aprobadas.items():
    print(f"En la {materia} tiene una nota de {creditos}")