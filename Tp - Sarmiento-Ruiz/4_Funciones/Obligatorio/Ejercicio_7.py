'''
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones
correspondientes a esas notas.
'''

def calificaciones(notas):
    calificacion = []
    for i in notas:
        if i <= 5:
            y = i
            calificacion.append(str(y) +' - Insuficiente')
        elif i <= 7:
            y = i
            calificacion.append(str(y) +' - Suficiente')
        elif i <= 9:
            y = i
            calificacion.append(str(y) +' - Bien')
        elif i == 10:
            y = i
            calificacion.append(str(y) +' - Sobresaliente')
        else:
            return
    return calificacion

notas = []
n = int(input("Ingrese la cantidad de notas: "))
for i in range(n):
    while True:
        nota = int(input('Ingrese una nota: '))
        if nota >=0 and nota <= 10:
            notas.append(nota)
            break
        else:
            print('Nota invalida')

for i in calificaciones(notas):
    print(i)


