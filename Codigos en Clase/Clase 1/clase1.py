#Esto es un comentario Comentario
##################################
#Print se encarga de enviar datos a la terminal
#explicar lo que sale en la terminal
#Clear limpia la consola

print("Hola mundo!")
###############################
#Puedo poner mas de un argumento separado por comas
print("Hola mundo!", "a",3,3, 3+4*2)
#Los print se imprimen despues de un salto de página(acciómpor defecto)
print("Hola mundo")
print("Adios.")
#############################
#Si quiero espacios entre prints
print("Hola mundo")
print()
print()
print()
print("Adios.")
########################################
#Si quiero imprimir prints seguidos:
print("Hola mundo", end=" - ")
print("Adios.")

###############################################
#Comentarios


'''
print("Hola mundo", end=" - ")
print("Adios.")

'''

#Otro para docstring
"""sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
"""
#Ir a diapositivas: variables y convenciones de nombres

############################################################
#Tratamiento de constantes
PI= 3.141592653559
print(PI)
PI = 4
print(PI)
#Ir a diapositivas

############################################################
#Tipos de variables

nota1 = 9
nota2 =10 # 10.0 flotante
nota3 =4
promedio =(nota1 + nota2 + nota3)/3  #flotante
print("El promedio es :", promedio)

############################################################
#La divisio define el tipo de la variable como flotante

nota1 = 9
nota2 =10 # 10.0 flotante
nota3 =2
promedio =(nota1 + nota2 + nota3)/3  #flotante
print("El promedio es :", promedio)


############################################################
#La divisio sea exacta se usa //

nota1 = 9
nota2 =10 # 10.0 flotante
nota3 =2
promedio =(nota1 + nota2 + nota3)//3  #flotante
print("El promedio es :", promedio)

############################################################

#Hay otros operadores como modulo %

############################################################

#python es un lenguaje fuertemente tipado. No se puede hacer los siguiente
#porque salta un error

#nota1 = 9
#nota2 =10 
#nota3 =2
#promedio =(nota1 + nota2 + nota3)/3
#print("El promedio es :" + promedio)


############################################################

#Como solucionar? con la conversión de tipos

nota1 = 9
nota2 =10 
nota3 =2
promedio =(nota1 + nota2 + nota3)/3
print("El promedio es :" + str(promedio))

############################################################

#Puedo convertir un numero a un texto

#nota1 = "9"
#nota2 =10 
#nota3 =2
#promedio =(nota1 + nota2 + nota3)/3
#print("El promedio es :" + str(promedio))

# int
nota1 = int("9") #No int("9s"),int("s")
nota2 =10 
nota3 =2
promedio =(nota1 + nota2 + nota3)/3
print("El promedio es :" + str(promedio))

# foat
nota1 = float("9") # float("9.0")
nota2 =10 
nota3 =2
promedio =(nota1 + nota2 + nota3)/3
print("El promedio es :" + str(promedio))


#Puedo cortar las instrucciones \
nota1 = "dadadssssssssssssssssssssssssssssssssssss \
    ssssssssssssssssssssssssada"

#Debo tener un mecanismo para ingresar datos input()
#Esta instrucción toma un dato por teclado y lo almacena en algun lado

#a = input()
#print(a)


#Debo tener un mecanismo para ingresar indicar que se debe ingresar

#a = input("Ingrese la nota 1: ") #Siempre devuelve cadenas
#print(a)

#######################################
#Si intento hacer estaoperación me daráun error porque 
#al ingresar la variable latoma como cadena
#nota1 = input("Ingrese la nota 1: ")
#nota2 =input("Ingrese la nota 2: ")
#nota3 =input("Ingrese la nota 3: ")
#promedio =(nota1 + nota2 + nota3)/3
#print("El promedio es :" + promedio)

#######################################
#Debemos hacer la conversión

#nota1 = input("Ingrese la nota 1: ")
#nota2 =input("Ingrese la nota 2: ")
#nota3 =input("Ingrese la nota 3: ")
#promedio =(int(nota1) + int(nota2) + int(nota3))/3
#print("El promedio es :" + str(promedio))

#######################################
#Se utilizamas esto

#nota1 = int(input("Ingrese la nota 1: "))
#nota2 =int(input("Ingrese la nota 2: "))
#nota3 =int(input("Ingrese la nota 3: "))
#promedio =(nota1 + nota2 + nota3)/3
#print("El promedio es :" + str(promedio))

#######################################
#Si queremos saber de quetipo esun variable en tiempo deejecución
#Usamos type

#nota1 = int(input("Ingrese la nota 1: "))
#print(type(nota1))

#nota2 = "dadasdasdadsadasd"
#print(type(nota2))


#Uso correcto de true
#print(type(true)) #Da error
#print(type(True)) #Da error


######################Regresamos a operadores

################Expresiones boolenas

#a = 60
#b = a > 90
#print(b)

####Operadores de pertenencia
a = "Clase de python"
print("p" in a)
print("ase" in a)
print("u" not in a)
print("Clase" not in a)




