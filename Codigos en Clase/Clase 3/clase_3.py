'''
c="programación 3" # cadena de longith variable  


#c=""   #cadena de longitud 0

# Hay muchos funciones para trabajar con cadenas

print (len(c))

#puedo mostrar un caracter en particular (el indice siempre comienza en 0):
c="programación 4" # cadena de longith variable  
print(c[2]) 
print(c[10])
print(c[11])


#quiero saber el ultimo

print(c[len(c)-1])
#Una alternativa seria:
print( c[-1])




#o el penultimo
print(c[-2])
#o el antepenultimo
print(c[-3])



#Cuidar que el indice sea un no existe. SI nos pasamos de rango python muestra hasta el final
#de rango

#print(c[44]) #indice fuera de rango
#print(c[-44]) #indice fuera de rango



#Podemos seleccionar una subcadena adentro de otra
#Rebanadas: devuelve uno menos


c="programación III" # cadena de longith variable  

#Por ejemplo  "III"
print (c[13:16])



#Por ejemplo si me paso de rango no me da error, me muestra hasta el final
print (c[13:20])


#Si quiero mostrar hasta el ultimo caracter. Solo pongo el indice inicial
print (c[13:])


c="programación 3" # cadena de longith variable  

# Si quiero mostrar desde el principio
print (c[:14])


# Si quiero ver la cadena completa:
print (c[:])


# Otro parametro importante me dice cada cuantos caracteres se van a mostrar

print (c[0:14:1])  #cada uno
print (c[0:14:2])  #cada dos
print (c[0:14:3])  #cada dos



# Si ponemos -1 se cuenta en orden decreciente hasta uno antes de llegar al 0

c="programación 3" # cadena de longith variable  

print (c[14:0:-1])  

print (c[14::-1])  


# me muestra la cadena entera pero al reves
print (c[::-1])  


#Por ejemplo quiero saber i una cadena es capitua de otra:

c= '234432'
d= c[::-1]

if c==d:
    print('Es capicúa')
else:
    print('No es capicúa')
    


#Para palindromos tambien se aplica

c= 'neuquen'
d= c[::-1]


if c==d:
    print('Es un palíndromo capicúa')
else:
    print('No es un palíndromo')
    

#tambien podemos averiguar cual letra tiene el codigo ASCII mas alto
c= '1 neuquen'
print(max(c))
#tambien podemos averiguar cual letra tiene el codigo ASCII mas pequeño
print(min(c))


#Podemos comparar las cadenas ver cual esta antes que otra en un diccionario

c= 'Palabra'    
d= 'Hola'
if c < d:
    print('c esta antes que d')
else:
    print('d esta antes que c')



#Podemos comparar las cadenas por ejemplo para ver si el ingreso de una 
#contraseña es correcta

c= 'Palabra'    
d= 'fsdfsd45464646' #(Ingreso de un usuario)


if c==d:
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')




#Regresamos a las diapo

#Regresamos a partir del for

#Una cadena lo puedo recorrer con un for

for letra in range(len(c)):
    print(c[letra])



    
#Si estamos recorriendo listas o cadenas python tiene un procedimiento mejor
c= 'neuquen'

for letra in c:
    print(letra)

for letra in c:
    print(letra, end='')



#Regresar a las diapositivas

#Uso de join

c ='hola'
c = '-----'.join(c)
print(c)




#Uso de split
c= 'Me recuerda a los profesores de la escuela técnica'
lista = c.split(' ')
print(lista)

#formato csv de excel
c= 'Me recuerda a los profesores de la escuela técnica'
lista = c.split(',')
print(lista)


#  Uso de cadena.find()
c = 'programacion programacion programacion'

pos= c.find('programacion')
pos2= c.rfind('programacion', 10,50 )

print(pos)
print(pos2)





# Uso de f-string
nombre ='Maria de los angeles'
legajo ='45646'
edad = 55
telefono = "3854172879"


print('nombre: '+ nombre + ' legajo: ' + legajo + ' mi edad es: ' + str(edad) + 'mi telefono es:' + telefono  )
print(f"nombre: {nombre} , legajo: {legajo} , edad: {edad}, telefono: {telefono}")

#Mirar documento string5 
#Uso del metodo str.format()

comision= "tarde"
materia ="programación III"
print("Esta es la comision" + comision + " de la materia  " + materia)
print("Esta es la comision {} de la materia {}".format(comision, materia))
print("Esta es la comision {0} de la materia {1}".format(comision, materia))
print("el resultado de la suma de {} y {} es igual a {}".format(8,9, 8+9))


#LISTAS####################
#Primer elemento 0
d=["Lun","Mar","Mie", "Jue"]

print(d[1])
print(d[2])
print(d[-2])
#Rebanadas
print(d[1:3])
print(d)
print(d[::-1])

#Existe un método para invertirla
d=["Lun","Mar","Mie", "Jue"]
print(d)
d.reverse()
print(d)

#las listas son mutables puedo cambiar su contenido

#Puedo cambiar su contenido

d=["Lun","Mar","Mie", "Jue"]
print(d)
d[2]= 3
print(d)


#Puedo agregar al final un elemento

d=["Lun","Mar","Mie", "Jue"]
d.append("Vie")
print(d)



#Puedo eliminar el ultimo elemento
d=["Lun","Mar","Mie", "Jue"]
d.pop()
print(d)


#Puedo eliminar el elemento que indica el indice

d=["Lun","Mar","Mie", "Jue"]
d.pop(1)
print(d)


#Puedo puedo ordenar la lista alfabeticamente

d=["Lun","Mar","Mie", "Jue"]
d.sort()
print(d)


e=[5,8,6,2,9,5,6,8]
e.sort()
print(e)


#Puedo imprimir el elemento mas grande de la lista

e=[5,8,6,2,9,5,6,8]
print(max(e))


#Puedo imprimir el elemento mas chico de la lista
e=[5,8,6,2,9,5,6,8]
print(min(e))


#Puedo recorrer una lista con for
e=[5,8,6,2,9,5,6,8]
for elemento in e:
    print(elemento)




#En vez de hacer esto:

e=[5,8,6]

a =e[0]
b =e[1]
c =e[2]
print(a,b,c) 

#El desempaquetado
e=[5,8,6]
a, b,c = e
print(a,b,c) 

#Si pongo mas variables que la cantidad de elementos de la lista me da error
#que pasa si pongo menos variables menos o mas variables demasiados elementos para desempaquetar
# puedo asignar mas de un elemento a una variable
e=[5,8,6,9,10]
a,*b = e    #5 [8, 6, 9, 10]
print(a,b) 



#Una lista puede ser una combinacion de elementos de diferentes tipos



#lista de lista
# cada lista representa  las notas de un alumno
d=  [[4,6,3],
    [8,9,10],
    [7,8,6]]

#Podemos mostrar cada nota

for elemento in d:
    for nota in elemento:
        print(f"la nota es {nota}")

#Podemos calcular el promedio

d=[[4,8,3],[8,9,10],[4,8,6]]

for alumno in d:
    promedio = sum(alumno) / 3
    print(f"El promedio es {promedio}")



#la función list

a = "Estamos aprendiendo python"

lista = list(a)
print(lista)



#Conversion de un range a lista

lista = list(range(2,11,2))
print(lista)


#Conjuntos
a = "Estamos aprendiendo python"

#Conversion de la cadena en conjunto
conjunto=  set(a)
print(conjunto)



numeros = "1111111112222222333333"
conjunto = set(numeros)
print(conjunto)


conjunto ={'Palotes,juan de los', (1930,11,2), 45612313}
a = set(conjunto)
for elem in a:
    print(elem)
#[print (elem) for elem in  a]


#Puedo eliminar todos los elementos del conjunto
conjunto ={'Palotes,juan de los', (1930,11,2), 45612313}
a = set(conjunto)

a.clear()
print(a)




#Diccionarios
alumnos = {'Juan': 8, 'Pedro': 9, 'Maria': 10, 'Luis': 7}
print(alumnos)

print(alumnos['Maria'])
print(alumnos.get('Maria')) 



# Si intento agregar un nuevo elemento con la misma clave modifica su valor

alumnos = {'Juan': 8, 'Pedro': 9, 'Maria': 10, 'Luis': 7}

alumnos['Pedro'] = 120
print(alumnos)


# Si intento agregar un nuevo elemento con una clave que no esta en el diccionario
# lo agrega
alumnos = {'Juan': 8, 'Pedro': 9, 'Maria': 10, 'Luis': 7}

alumnos['Ana'] = 10
print(alumnos)



alumnos = {'Juan': 8, 'Pedro': 9, 'Maria': 10, 'Luis': 7}

print(alumnos.keys())
for i in alumnos.keys():
    print(i)




alumnos = {'juan': 8, 'pedro': 10, 'maria': 9}
print(alumnos.items())

# items() devuelve una tupla con las claves y los valores:
for clave, valor in alumnos.items():
    print("Alumno:", clave, "Nota:", valor)

'''


