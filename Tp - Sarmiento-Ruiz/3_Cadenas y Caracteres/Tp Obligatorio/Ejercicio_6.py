"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por 
pantalla las asignaturas que el usuario tiene que repetir"""



asignaturas_notas = {}

while True:
    asignatura = input("Ingrese una asignatura (o presione Enter para finalizar): ").capitalize()
    if not asignatura:
        break
    
    nota_str = input(f"Ingrese la nota para {asignatura}: ")
    if nota_str.replace(".", "", 1).isdigit():
        nota = float(nota_str)
        if 1 <= nota <= 10:
            asignaturas_notas[asignatura] = nota
        else:
            print("La nota debe estar entre 1 y 10. Inténtalo nuevamente.")
    else:
        print("Ingresa una nota válida (número decimal).")


asignaturas_desaprobadas = {}
for asignatura, nota in asignaturas_notas.items():
    if nota <= 3:
        asignaturas_desaprobadas[asignatura] = {"nota": nota, "leyenda": "RINDE EN MARZO"}
    elif 3 < nota < 6:
        asignaturas_desaprobadas[asignatura] = {"nota": nota, "leyenda": "RINDE EN DICIEMBRE"}
        
# Aqui se crea un Diccionario dentro de otro diccionario 
# asignaturas_desaprobadas = {asignatura,datos}
# datos = {nota,leyenda}

print("\nAsignaturas desaprobadas:")
for asignatura, datos in asignaturas_desaprobadas.items():
    print(f"{asignatura.upper()} - Nota: {datos['nota']:.2f} - {datos['leyenda']}")