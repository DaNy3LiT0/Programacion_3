'''
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal,
que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media.
El programa pedirá el número de días que se van a introducir.
'''

def temp_media(temp_max, temp_min):
    temp = (temp_max+temp_min)/2
    return temp

dias = int(input('Ingrese el numero de dias que se van a introducir: '))
for i in range(dias):
    temp_max = float(input(f'Ingrese la temperatura maxima del dia {i+1}: '))
    temp_min = float(input(f'Ingrese la temperatura minima del dia {i+1}: '))
    media = temp_media(temp_max, temp_min)
    print(f'La temperatura media del dia {i+1} es: {media}°C')
