'''
#------------------------------1------------------------------#
# la funcion no esta defenida en el codigo por eso no funciona
#No funciona
print("Estoy en mi programa") 
print sumar(3,4)
#------------------------------1------------------------------#

#------------------------------2------------------------------#
#aun no funciona
import mis_funciones


print("Estoy en mi programa") 
print sumar(3,4)



#------------------------------2------------------------------#

#------------------------------3------------------------------#
#En cambio
import mis_funciones


print("Estoy en mi programa") 
print (mis_funciones.sumar(3,4))



#------------------------------3------------------------------#

#------------------------------4------------------------------#

#Mis simple
from mis_funciones import sumar


print("Estoy en mi programa") 
print (sumar(3,4))




#------------------------------4------------------------------#

#------------------------------5------------------------------#

#quiero importar mas funciones
from mis_funciones import sumar, restar


print("Estoy en mi programa") 
print (sumar(3,4))
print (restar(3,4))


#------------------------------5------------------------------#


#------------------------------6------------------------------#

#Si quiero importar todas las funciones
from mis_funciones import *


print("Estoy en mi programa") 
print (sumar(3,4))
print (restar(3,4))


#------------------------------6------------------------------#

#------------------------------7------------------------------#
#quiero importar mas funciones
from mis_funciones import sumar
from mis_funciones import restar


print("Estoy en mi programa") 
print (sumar(3,4))
print (restar(3,4))


#------------------------------7------------------------------#
'''

#------------------------------8------------------------------#
#Puedo tener funciones que se llamen igual como las importadas o bien puedo cambiar su nombre
from mis_funciones import sumar as sum
from mis_funciones import restar

def sumar(a,b):
    return "CUAC"
    
print (sum(3,4))
print (restar(3,4))



#------------------------------8------------------------------#
