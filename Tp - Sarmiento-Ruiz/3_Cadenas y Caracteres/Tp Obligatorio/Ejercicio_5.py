"""Escribir un programa que almacene las asignaturas de un curso en una lista, pregunte al usuario 
la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En 
<asignatura> has sacado <nota> donde <asignatura> es cada una de las 
asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el 
usuario"""


asignaturas_notas = {}

while True:
    asignatura = input("Ingrese una asignatura (o presione Enter para finalizar): ").upper()
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

print("Asignaturas y notas:")
for asignatura, nota in asignaturas_notas.items():
    print(f"{asignatura}: {nota:.2f}")
