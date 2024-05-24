"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un 
curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos 
de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es 
cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar 
también el número total de créditos del curso"""

materia_creditos = {}

while True:
    materia = input("Ingresa el nombre de la asignatura (o ENTER para terminar): ")
    if materia.lower() == "":
        break
    creditos = int(input(f"Ingresa los creditos para {materia}: "))
    materia_creditos[materia] = creditos


for materia, creditos in materia_creditos.items():
    print(f"La {materia} tiene {creditos} créditos.")

# Calcular el número total de créditos
total_creditos = sum(materia_creditos.values())
print(f"El número total de créditos del curso es: {total_creditos}")
