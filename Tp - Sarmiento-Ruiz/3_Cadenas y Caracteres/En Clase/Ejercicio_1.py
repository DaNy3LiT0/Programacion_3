"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
"""

FechaNaciemiento = ""
while len(FechaNaciemiento) != 10:
    FechaNaciemiento = input('Ingrese su fecha de nacimiento en el formato dd/mm/aaaa: ')
    
    if len(FechaNaciemiento) < 10:
        print("La fecha ingresada no tiene el formato solicitado")
        print("")
    elif len(FechaNaciemiento) > 10:
        print("La fecha ingresada no tiene el formato solicitado")
        print("")
    else:
        print(f'Dia: {FechaNaciemiento[0:2]}')
        print(f'Mes: {FechaNaciemiento[3:5]}')
        print(f'Año: {FechaNaciemiento[6:10]}')