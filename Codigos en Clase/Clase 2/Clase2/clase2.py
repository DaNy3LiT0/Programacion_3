'''
#If con python

# pido un color y si es rojo
# aviso que es correcto

color = input ('Ingrese un color: ')
#if en javascript es una función

if color == 'rojo':
     print ('Color correcto')
     a = 3
     b = 4

print ('Programa finalizado.')

#else
color = input ('Ingrese un color: ')
if color == 'rojo':
     print ('Color correcto')
     a = 3
     b = 4
else:
     print('Color equivocado')

print ('Programa finalizado.')

# 0 1 2 3 4 5 6 7 8 9 10
# 0...3  No alcanza
# 4...6 Falta poco
# 7...9 Muy bien
# 10    Excelente

'''
nota = int(input ('Ingrese una nota'))

if nota >= 0 and nota <= 3:
    print('No alcanza')
else:
    if nota >= 4 and nota <= 6:
        print('Falta poco')
    else:
        if nota >=7 and nota <= 9:
            print('Muy bien')
        else:
            print('Excelente')

#Otra alternativa
# 0 1 2 3 4 5 6 7 8 9 10
# 0...3  No alcanza
# 4...6 Falta poco
# 7...9 Muy bien
# 10    Excelente

nota = int(input ('Ingrese una nota'))

if nota >= 0 and nota <= 3:
    print('No alcanza')
else:
    if nota <= 6:
        print('Falta poco')
    else:
        if nota <= 9:
            print('Muy bien')
        else:
            print('Excelente')




#Uso del elif
nota = int(input ('Ingrese una nota'))

if nota >= 0 and nota <= 3:
    print('No alcanza')
elif nota <= 6:
    print('Falta poco')
elif nota <= 9:
    print('Muy bien')
else:
    print('Excelente')



menu = 1
match menu:
    case 1:
        print('Opción 1')
    case 2:
        print('Opción 2')
    case 3:
        print('Opción 3')

    case other:
        print('Opcion n')





#WHILE


contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 1



contador = 1
while contador <= 10:
    print(contador)
    contador +=  1



#Puedo sumarlos

contador = 1
suma = 1
while contador <= 10:
    print(contador)
    contador +=  1
    suma = suma + contador
print ('La suma es: ', suma)


contador = 1
suma = 0
while contador <= 10:
    print(contador)
    suma += contador
    contador +=  1
print ('La suma es: ', suma)

#?
contador = 11
suma = 0
while contador <= 10:
    print(contador)
    suma += contador
    contador +=  1
print ('La suma es: ', suma)


# ESTRUCTURA FOR
#en javascript
#for (let i= 1, i < 10, i++ )
#range (inicial, final, paso)

for i in range (1, 10, 1): # [1,2,3,4,5,6,7,8,9]
    print(i)


for i in range (4, 11, 2): # [4,6,8,10]
    print(i)




#for (let i= 1, i < 10, 1++ )
#range (incial, final, paso)

for i in range (10, -1, -1): # [10,9,8,7,6,5,4,3,2,1]
    print(i)

#for (let i= 1, i < 10, 1++ )
#range (incial, final, paso)

#Puedo omitir el paso y python asume que se incremente de a 1

for i in range(1, 10): # [1,2,3,4,5,6,7,8,9]
    print(i)


#Puedo omitir el inicio y paso en python asumo que comienza e cero y se
#incrementa de a 1
for i in range(11): # [0, 1,2,3,4,5,6,7,8,9,10]
    print(i)


for i in range(11): # [0,1,2,3,4,5,6,7,8,9,10]
    i = 19
    print('hola', i)


suma=0
for i in range(11): # [0,1,2,3,4,5,6,7,8,9,10]
    i = 19
    suma += i
    print('hola', i, suma)


#break

for i in range(1, 10): # [1,2,3,4,5,6,7,8,9]
    print('hola',i)
    if i ==5:
        break

#podemos usar variables para definir los parametros del range

inicio = int(input('Inicio: '))
final = int(input('Final: '))

for i in range(inicio,final+1):
    print('hola',i)

#Existe el Do...while? no...


contador = 0
while contador <= 10:
    contador+=1
    if contador == 4:
        continue
    print(contador)


