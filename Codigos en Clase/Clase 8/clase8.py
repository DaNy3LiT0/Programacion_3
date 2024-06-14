#---------------------------------1---------------------#
#a = 3
#b =a+3
#print(a  #El programa se rompe

#Los errores son muy explicativos. 
# 1 - Se muestra el nombre de archivo donde se produjo el error
#2 - Nos dice la linea donde esta el error
#3 - Nos dice el tipo de error
#---------------------------------1---------------------#
#---------------------------------2---------------------#
#Los errores pueden ser de otro tipo. Pongo el nombre de una función inexistente. Error de nombre (NameError)
#a = 3
#b =a+3
#pront(a)  #El programa se rompe

#---------------------------------2---------------------#

#---------------------------------3---------------------#

# Me da un error. Porque la división entre 0 no esta definido. Division entre 0 (ZeroDivisionError)
#a = 3
#b =a-3
#print(a/b)  #El programa se rompe
#---------------------------------3---------------------#
#---------------------------------4---------------------#
# Un error de tipos.TypeError
#a = 3
#b = "hola"

#print(a + b)

#---------------------------------4---------------------#

#---------------------------------5---------------------#
#Input siempre devuelve una cadena . TypeError
#n = input("Ingrese un número: ")
#mitad = n / 2
#print(f"{n}/2 = {mitad}")

#Solucion. Sin embargo puedo ingresar un error al permitir usar algo diferente a un numero

#n = float(input("Ingrese un número: "))
#mitad = n / 2
#print(f"{n}/2 = {mitad}")

#---------------------------------5---------------------#

#---------------------------------6---------------------#
#la forma de evitar que el programa se rompa si ingresamos una palabra es agregar un bloque try
#
#try:
#    n = float(input("Ingrese un número: "))
#    mitad = n / 2
#    print(f"{n}/2 = {mitad}")
#except:
#    #Codigo a incluir si existen un error
#    print()
#    print("Se produjo un error")    
#    print("intente nuevamente")    

#print("resto del programa...") #El programa sigue ejecutandose
#Necesitamos que el usuario si se equivocó vuelva a intentarlo hasta que ingrese un numero
#---------------------------------6---------------------#

#---------------------------------7---------------------#

#print("Entrando en el bucle")
#while True:
#    try:
#        n = float(input("Ingrese un número: "))
#        mitad = n / 2
#        print(f"{n}/2 = {mitad}")
#        break
#    except:
#        #Codigo a incluir si existen un error
#        print()
#        print("Se produjo un error")    
#        print("intente nuevamente")    

#print("resto del programa...") #El programa sigue ejecutandose

#---------------------------------7---------------------#

#---------------------------------8---------------------#
#Se puede romper por 0 o no era un numero
# Else si sale bien

#print("Entrando en el bucle")
#while True:
#    try:
#        n = float(input("Ingrese un número: "))
#        mitad = 100 / n
#        print(mitad)
#    except:
#        print()
#        print("Se produjo un error")    
#        print("intente nuevamente")    
#    else:
#        print("Todo ok!!")
#        break

#print("resto del programa...") #El programa sigue ejecutandose

#---------------------------------8---------------------#


# finally se ejecuta siempre incluso si hay un break.
# Se utiliza si se necesita limpiar lsa variables, inicializar algun ejemplo, 

# print("Entrando en el bucle")
# while True:
#     try:
#         n = float(input("Ingrese un número: "))
#         mitad = 100 / n
#         print(mitad)
#     except:
#         print()
#         print("Se produjo un error")    
#         print("intente nuevamente")    
#     else:
#         print("Todo ok!!")
#         break
#     finally:
#         print("(Bucle completado)")

# print("resto del programa...") #El programa sigue ejecutandose

#---------------------------------9---------------------#

#Except atrapa todos los errores hasta hora podemos poner except dependiendo del error

#print("Entrando en el bucle")
#while True:
#    try:
#        n = float(input("Ingrese un número: "))
#        mitad = 100 / n
#        print(mitad)
#    except ZeroDivisionError:
#        print()
#        print("El número ingresado no puede ser cero")    
#        print("intente nuevamente")    
#    else:
#        print("Todo ok!!")
#        break
#    finally:
#        print("(Bucle completado)")

#print("resto del programa...") #El programa sigue ejecutandose

#---------------------------------9---------------------#


#--------------------------------10---------------------#
#En el caso anterior solo atrapa los 0. Si ingreso "Hola" no podria atraparlo

#print("Entrando en el bucle")
#while True:
#    try:
#        n = float(input("Ingrese un número: "))
#        mitad = 100 / n
#        print(mitad)
#    except ZeroDivisionError:
#        print()
#        print("El número ingresado no puede ser cero")    
#        print("intente nuevamente")    
#    except ValueError:
#        print()
#        print("Debe ingresar un número")    
#        print("intente nuevamente")    
#    else:
#        print("Todo ok!!")
#        break
#    finally:
#        print("(Bucle completado)")
#
#print("resto del programa...") #El programa sigue ejecutandose



#--------------------------------10---------------------#


#--------------------------------11---------------------#

#Si quiero atrapar combinacion de teclas o una sola tecla como ENTER

#print("Entrando en el bucle")
#while True:
#    try:
#        n = float(input("Ingrese un número: "))
#        mitad = 100 / n
#        print(mitad)
#    except ZeroDivisionError:
#        print()
#        print("El número ingresado no puede ser cero")    
#        print("intente nuevamente")    
#    except ValueError:
#        print()
#        print("Debe ingresar un número")    
#        print("intente nuevamente")    
#    except KeyboardInterrupt:
#        print()
#        print("Ingreso un caracter extraño")    
#        print("intente nuevamente")    
#    else:
#        print("Todo ok!!")
#        break
#    finally:
#        print("(Bucle completado)")

#print("resto del programa...") #El programa sigue ejecutandose



#--------------------------------11---------------------#

#--------------------------------12---------------------#
#Si quiero considerar otros errores no considerados ponemos solo except




#print("Entrando en el bucle")
#while True:
#    try:
#        n = float(input("Ingrese un número: "))
#        mitad = 100 / n
#        print(mitad)
#    except ZeroDivisionError:
#        print()
#        print("El número ingresado no puede ser cero")    
#        print("intente nuevamente")    
#    except ValueError:
#        print()
#        print("Debe ingresar un número")    
#        print("intente nuevamente")    
#    except KeyboardInterrupt:
#        print()
#        print("Ingreso un caracter extraño")    
#        print("intente nuevamente")    
#    except:
#       print("Se produjo un error")
#    else:
#        print("Todo ok!!")
#        break
#    finally:
#        print("(Bucle completado)")

#print("resto del programa...") #El programa sigue ejecutandose




#--------------------------------12---------------------#


#--------------------------------13---------------------#
#Puedo poner un except asignandole una variable




#print("Entrando en el bucle")
#while True:
#    try:
#        n = float(input("Ingrese un número: "))
#        mitad = 100 / n
#        print(mitad)
#    except Exception as e:
#        print("Ha ocurrido un error =>", type(e).__name__)
#    else:
#        print("Todo ok!!")
#        break
#    finally:
#        print("(Bucle completado)")

#print("resto del programa...") #El programa sigue ejecutandose


#--------------------------------13---------------------#
