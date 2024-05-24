'''
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones
correspondientes a esas notas. Por ejemplo 4 — Desaprobado
'''


def calificaciones(x):
    notas2 = []
    for i in x:
        if i >= 0 and i<6:
            y = i
            notas2.append(str(y) + ' - Desaprobado')
        elif i>= 6 and i<=10:
            y = i
            notas2.append(str(y) + ' - Aprobado')
        else:
            return
    return notas2

### Programa Principal ###
notas = []
while True:
    nota = int(input('Ingrese una nota u 11 para salir: '))
    if nota >=0 and nota <= 10:
        notas.append(nota)
    else:
        break

for i in calificaciones(notas):
    print(i)

