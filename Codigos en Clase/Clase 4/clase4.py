'''
#--------------------------------1---------------------------------#
def sumar(a,b):
    suma = a + b
    print(f"{a} + {b} ={suma}")


#programa principal
#Invocando a la función
sumar(4,6)  

#Pasar datos de la funcion por valor: el 4 se copia en a y se copia en b
#Pasar datos de la funcion por valor (paso de parámetros por valor): el 4 se copia en a y se copia en b
#Las variables que se encuentran dentro de la funcion son locales a la función

#--------------------------------1---------------------------------#


#--------------------------------2---------------------------------#

#Puedo hacer: declarar una variable y pasarlo como parámetro. El valor de num1
#se copia como parámetro en a

def sumar(a,b):
    suma = a + b
    print(f"{a} + {b} ={suma}")


#programa principal
num1 = 4 
#Invocando a la función
sumar(num1,6)
#print(suma)  #No podemos acceder a una variable local de la  función.

#--------------------------------2---------------------------------#




#--------------------------------3---------------------------------#

#las variables que creo dentro de la funcion son variables locales
#y no podemos acceder por fuera de la función
def sumar(a,b):
    suma = a + b
    print(f"{a} + {b} ={suma}")


#programa principal
num1 = 4 
#Invocando a la función
sumar(num1,6)
print(suma)  #No podemos acceder a una variable local de la  función.

#--------------------------------3---------------------------------#


#--------------------------------4---------------------------------#

# La variable global la puedo ver dentro de la función y afuera de la funcion
def sumar(a,b):
    suma = a + b
    print("num1 dentro de la funcion: ",num1)
    
    print(f"{a} + {b} ={suma}")

#programa principal
num1 = 4    #variable global
sumar(num1,6)


#--------------------------------4---------------------------------#

#--------------------------------5---------------------------------#
# Python crea dos variables una local y otra global para Num1 luego de ejecutada la funcion Num1 se destruye
def sumar(a,b):
    suma = a + b
    num1 = 0
    print("num1 dentro de la funcion: ",num1)
    
    print(f"{a} + {b} ={suma}")

#programa principal
num1 = 4
sumar(num1,6)

print("num1 en el programa principal: ",num1)

#--------------------------------5---------------------------------#

#--------------------------------6---------------------------------#

#Como demostrarlo?


def sumar(a,b):
    suma = a + b
    num1 = 0
    print("Posición de memoria de num1 en la función: ",id(num1))
    print("num1 dentro de la funcion: ",num1)
    
    print(f"{a} + {b} ={suma}")

#programa principal
num1 = 4
sumar(num1,6)
print("Posición de memoria de Num1 en el programa principal: ",id(num1))

#--------------------------------6---------------------------------#


#--------------------------------7---------------------------------#
# Puedo requerir modificar el cavlor de una variable golbal dentro de la funcion...
#para hacer que num1 sea la misma variable dentro de la funcion puedo definirla como  global dentro de la función pero entraria en contradiccipon del tema del encapsulamiento.

def sumar(a,b):
    global num1
    suma = a + b
    num1 = 0
    print("Posición de memoria de num1 en la función: ",id(num1))
    print("num1 dentro de la funcion: ",num1)
    
    print(f"{a} + {b} ={suma}")

#programa principal
num1 = 4
sumar(num1,6)
print("Posición de memoria de Num1 en el programa principal: ",id(num1))
print(num1)




#Cuando pasamos los parametros por global estamos pasando los valores por referencia o sea le estamos indicando a una funcion que los valores con los que tiene que operar
#estan en una posición de memoria que definio el programa principal 
#Los tipos de datos simples siempre se pasan por valor
#Las colecciones siempre se pasan por referencia (se pasa un puntero al lugar donde esta la lista ir a archivo lista_1.py
ir a clase_1.py
#--------------------------------7---------------------------------#



#--------------------------------8---------------------------------#
#Return un resultado- no muestra
def sumar(a,b):
    suma = a + b
    return suma

#programa principal
sumar(2,6)  

#--------------------------------8---------------------------------#


#--------------------------------9---------------------------------#

#para mostrarlo

def sumar(a,b):
    suma = a + b
    return suma

#programa principal
resultado= sumar(2,6)  
print("El resultado es: ", resultado)


#--------------------------------9---------------------------------#


#--------------------------------10---------------------------------#

#Que pasaría si paso como argumento un solo valor, teniendo dos parámetros

# Si paso solo un valor u omito uno

def sumar(a,b):
    suma = a + b
    return suma

#programa principal
resultado= sumar(2)  
print("El resultado es: ", resultado)


#--------------------------------10---------------------------------#


#--------------------------------11---------------------------------#

#Puedo resolverlos usando parametros por defecto

def sumar(a,b=0):
    suma = a + b
    return suma

#programa principal
resultado= sumar(2)  
print("El resultado es: ", resultado)



#--------------------------------11---------------------------------#



#--------------------------------12---------------------------------#

#o puedo pasar los dos argumentos

def sumar(a,b=0):
    suma = a + b
    return suma

#programa principal
resultado= sumar(2,10)  
print("El resultado es: ", resultado)


#--------------------------------12---------------------------------#




#--------------------------------13---------------------------------#
# Puede pasar que los argumentos no se pasen ordenados o bien falten

def saludar(nom,apel, saludo):
    print(f"{saludo} {nom} {apel}") 
    
#Programa principal

saludar("Maria de los Angeles", "Pérez", "Hola")
saludar("Ana", "Herrera", "Adios")

#--------------------------------13---------------------------------#



#--------------------------------14---------------------------------#

def saludar(nom,apel, saludo="Bienvenidx"):
    print(f"{saludo} {nom} {apel}") 
    
#Programa principal

saludar("maria de los angeles", "Pérez", "Hola")
saludar("Ana", "Herrera", "Adios")
saludar("Pedro", "Juarez")

#--------------------------------14---------------------------------#


#Puedo cambiar el orden de los argumentos
#SyntaxError: positional argument follows keyword argument
def saludar(nom,apel, saludo="Bienvenidx"):
    print(f"{saludo} {nom} {apel}") 
    
#Programa principal

saludar("Pedro", "juarez", "Hola")
saludar("Ana", "Herrera", "Adios")
saludar(ape = "Herrera", nom = "Ana", "Adios")

#--------------------------------15---------------------------------#


#SyntaxError: positional argument follows keyword argument
#Solucion
#Python solicita que los valores que se pasan como argumentos posicionales esten antes que los valores pasados como argumentos por clave
def saludar(saludo, nom , apel):
    print(f"{saludo} {nom} {apel}") 
    
#Programa principal

saludar("Adios","Maria de los Angeles", "Pérez" )
saludar("Adios",apel = "Herrera", nom = "Ana")


#--------------------------------15---------------------------------#

# Funciones con argumentos posicionales arbitrarios
def sumar(*b):
    result=0
    for i in b:
        result=result+i
    return result

print (sumar(1,2,3,4,5))
print (sumar(10,20))



#Argumentos de palabra clave arbitrarias

def colores(**a):
    for i in a.items():
        print (i)
colores(numbers=5,colors="blue",fruits="apple")
'''
Salida:
('numbers', 5)
('colors', 'blue')
('fruits', 'apple')
'''



#--------------------------------16---------------------------------#
#Funciones que devuelven mas de un valor de varias formas:

def probar():
    a = 1
    b= 2
    c= 3
    return a

print (probar())
#--------------------------------16---------------------------------#

#--------------------------------17---------------------------------#
#retornar tres valores con una lista
def probar():
    a = 1
    b = 2
    c = 3
    lista = [a,b,c]
    return lista

print (probar())


#--------------------------------17---------------------------------#

#--------------------------------18---------------------------------#
#retornar un valor de la lista
def probar():
    a = 1
    b = 2
    c = 3
    lista = [a,b,c]
    return lista

x = probar()
print (x[1])

#--------------------------------18---------------------------------#



#--------------------------------19---------------------------------#

#Python ofrece una forma mas sencilla para hacerlo: devuelve una tupla

def probar():
    a = 1
    b = 2
    c = 3
    
    return a, b,c 


print (probar())   # Terminal: (1, 2, 3)



#--------------------------------19---------------------------------#

#--------------------------------20---------------------------------#

#Puedo desempaquetar la tupla

 
def probar():
    a = 1
    b = 2
    c = 3
    
    return a, b,c 


x,y,z = probar()
print(y)

#--------------------------------20---------------------------------#





#retornamos a las diapositivas


#--------------------------------21---------------------------------#

# Hay funciones que llaman a otra
#No es considerado una buena practica


 
def probar():
    a = 1
    b = 2
    c = 3
    def otra():
        print("Hola")
        f= 10
    
    otra()
    


probar()

#--------------------------------21---------------------------------#


#--------------------------------22---------------------------------#

#Lo anterior no es una buena práctica


def otra():
    print("Hola")


def probar():
    a = 1
    b = 2
    c = 3
    otra()
probar()



#--------------------------------22---------------------------------#


# ir a tabla.py

#--------------------------------24---------------------------------#

#FUNCIONES LAMBDA O ANONIMAS
def cuadrado(x):
    return x**2



cuadrado=lambda x: x**2
print(cuadrado(5))

#--------------------------------24---------------------------------#


#--------------------------------25---------------------------------#

# FUNCIONES MAP .Utiliza una funcion lambda y una lista y operada la función con cada elemento de la lista.
#Devuelve un objeto que no es iterable hay que convertirlo en una lista para poder operar


lista =[1,2,3,4,5,0]

lambda x: x**2
map(lambda x: x**2, lista)


#Conversion  a lista porque al map devuelve un objeto

list(map(lambda x: x**2,lista))



#--------------------------------25---------------------------------#

#--------------------------------26---------------------------------#

#si quiero imprimir:

lista =[1,2,3,4,5,0]

lista = list(map(lambda x: x**2,lista))

print(list(map(lambda x: x**2,lista)))

#--------------------------------26---------------------------------#



# ir a funciones_lambda_map_py


#Cual es par o impar



lista =[1,2,3,4,5,0]

print(list(map(lambda x: "Par" if x % 2 == 0 else "Impar",lista)))
'''