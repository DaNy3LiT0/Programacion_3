'''
class Transporte:
    ruedas=4


avion= Transporte()
tren=Transporte()

print(avion.ruedas)
print(tren.ruedas)
#-----------------1--------------
class Transporte:
    ruedas= 4 #Atributo de clase
    
#Debemos crear un metodo que se encargue de proporcionar esas propiedades de cada objeto     
    #Metodo constructor
    #parametro obligatorio, el primero: self (es el nombre del objeto que estoy construyendo)
    def constructor(self, medio, empresa, v_max,color="sin color"):
        #Atributos de instancia, varian de un objeto a otro
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color
        self.combustible = combustible


#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

avion = Transporte()
tren = Transporte()
#-----------------1--------------

#-----------------2--------------
class Transporte:
    ruedas= 4 #Atributo de clase


print("\033[H\033[J")          # Limpiamos la pantalla

#Podemos mostrar la cantidad de ruedas de los objetos
#Usamos la notación punto    

avion = Transporte()
tren = Transporte()

print(avion.ruedas)
print(tren.ruedas)

#-----------------2--------------


#-----------------3--------------

class Transporte:
    ruedas= 4 #Atributo de clase
    
#Debemos crear un metodo que se encargue de proporcionar esas propiedades de cada objeto     
    #Metodo constructor
    #parametro obligatorio, el primero: self (es el nombre del objeto que estoy construyendo)
    def constructor(self, medio, empresa, v_max,color="sin color"):
        #Atributos de instancia, varian de un objeto a otro
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color


#Debemos definir atributos que sean propios para cada instancia del objeto
#Debemos crear un Metodo iniciador o constructor para definir atributos propios de ese objeto

print("\033[H\033[J")          # Limpiamos la pantalla

avion = Transporte()
avion.constructor("aire", "A. Arg.", 1400, "azul y blanco")
tren = Transporte()
tren.constructor("tierra", "F. Sarmiento", 60, "celeste")

#-----------------3--------------

#-----------------4--------------


#No mostre nada aun
class Transporte:
    ruedas= 4 
    
    def constructor(self, medio, empresa, v_max,color="sin color"):
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color


#Debemos definir atributos que sean propios para cada instancia del objeto
#Debemos crear un Metodo iniciador o constructor para definir atributos propios de ese objeto

#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

avion = Transporte()
avion.constructor("aire", "A. Arg.", 1400, "azul y blanco")
tren = Transporte()
tren.constructor("tierra", "F. Sarmiento", 60, "celeste")

#Accedemos a los atributos de instancia de los objetos con notación punto
#Los atributos de instancias permiten definir valores diferentes para cada objeto

print("Avion: ",avion.medio)
print("Tren: ",tren.medio)

#Accedemos a los atributos de clase de los objetos con notación punto

print("Cantidad de ruedas del avion: ",avion.ruedas)
print("Cantidad de ruedas del tren: ",tren.ruedas)

# Puedo mostrar otros atributos

print("Velocidad del Avion: ", avion.v_max)


#-----------------4--------------

#-----------------5--------------
#Puedo definir otros métodos
#Debemos crear un metodo que se encargue de proporcionar esas propiedades de cada objeto     

class Transporte:
    ruedas= 4 #Atributo de clase
    
    #Metodo constructor
    #parametro obligatorio, el primero: self (es el nombre del objeto que estoy construyendo)
    def constructor(self, medio, empresa, v_max,color="sin color"):
        #Atributos de instancia, varian de un objeto a otro
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color
        

    def imprimir(self):
        #print(f"Me desplazo por {self.medio}")
        print(f"Me desplazo por {self.medio} y uso {self.combustible}")



#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

avion = Transporte()
avion.constructor("aire", "A. Arg.", 1400, "azul y blanco")
tren = Transporte()
tren.constructor("tierra", "F. Sarmiento", 60, "celeste")


avion.imprimir()
tren.imprimir()


#-----------------5--------------

#-----------------6--------------
#Puedo definir nuevos atributos de instancias con la notacion punto por fuera de la clase
class Transporte:
    ruedas= 4 #Atributo de clase
    
    #Metodo constructor
    #parametro obligatorio, el primero: self (es el nombre del objeto que estoy construyendo)
    def constructor(self, medio, empresa, v_max,color="sin color"):
        #Atributos de instancia, varian de un objeto a otro
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color
        

    def imprimir(self):
        #print(f"Me desplazo por {self.medio}")
        print(f"Me desplazo por {self.medio} y uso {self.combustible}")


#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

avion = Transporte()
avion.constructor("aire", "A. Arg.", 1400, "azul y blanco")
tren = Transporte()
tren.constructor("tierra", "F. Sarmiento", 60, "celeste")


#Puedo definir nuevos atributos de instancia con la notacion punto
#Pero el atributo solo es válido para ese objeto
avion.combustible = "JP1"

print(avion.combustible)


#No esta definido
#print(tren.combustible)


#-----------------6--------------



#-----------------7--------------

#Para evitar tener que definirlo ese atributo para cada objeto lo definimos en el constructor

class Transporte:
    ruedas= 4 #Atributo de clase
    
    #Metodo constructor
    
    def constructor(self, medio, empresa, combustible,v_max,color="sin color"):
        #Atributos de instancia, varian de un objeto a otro
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color
        self.combustible = combustible
        

    def imprimir(self):
        #print(f"Me desplazo por {self.medio}")
        print(f"Me desplazo por {self.medio} y uso {self.combustible}")

#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla


avion = Transporte()
avion.constructor("aire", "A. Arg.", 1400, "azul y blanco", "JP1")
tren = Transporte()
tren.constructor("tierra", "F. Sarmiento", 60, "celeste", "Gasoil")
#barco = Transporte()
#barco.constructor("mar", "Caribbean", 50, "azul", "viento")


avion.imprimir()
tren.imprimir()
#barco.imprimir() #ERROR! #Definir el constructor


#-----------------7--------------


#-----------------8--------------
#El proceso de inicializar un objeto es muy comun por lo tanto python nos brinda el metodo  __init__ para hacerlo


class Transporte:
    ruedas= 4 #Atributo de clase
    
#Debemos crear un metodo que se encargue de proporcionar esas propiedades de cada objeto     
    #Metodo constructor
    def __init__(self, medio, empresa, combustible,v_max,color="sin color"):
        #Atributos de instancia, varian de un objeto a otro
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color
        self.combustible = combustible
#Podemos definir otros métodos
    def imprimir(self):
        #print(f"Me desplazo por {self.medio}")
        print(f"Me desplazo por {self.medio} y uso {self.combustible}")


#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla



#En vez de:
#avion= Transporte()
#avion.constructor("aire", "A. Arg.", 1400, "azul y blanco", "JP1")

#hacemos:

avion = Transporte("aire", "A. Arg.", 1400, "azul y blanco", "JP1")

#
#tren = Transporte()
#tren = Transporte("aire", "A. Arg.", 1400, "azul y blanco", "JP1")

#hacemos:

tren =  Transporte("mar", "Caribbean", 50, "azul", "viento")


#barco = Transporte("mar", "Caribbean", 50, "azul", "viento")


#-----------------8--------------

#-----------------9--------------


#En realidad no estamos mostrando un  atributo de clase  sino que con la notacion punto estamos creando
#Un atributo de instancia con el mismo nombre que el atributo de clase



class Transporte:
    ruedas= 4 #Atributo de clase
    

    #Metodo constructor
    def __init__(self, medio, empresa, combustible,v_max,color="sin color"):
        #Atributos de instancia, varian de un objeto a otro
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color
        self.combustible = combustible
#Podemos definir otros métodos
    def imprimir(self):
        #print(f"Me desplazo por {self.medio}")
        print(f"Me desplazo por {self.medio} y uso {self.combustible}")


#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

#En realidad no estamos mostrando un  atributo de clase  sino que con lanotacion punto estamos creando
#Un atributo de instancia con el mismo nombre que el atributo de clase



avion = Transporte("aire", "A. Arg.", 1400, "azul y blanco", "JP1")
tren = Transporte("tierra", "F. Sarmiento", 60, "celeste", "Gasoil")
barco = Transporte("mar", "Caribbean", 50, "azul", "viento")


print(f"Cantidad de ruedas del banco", barco.ruedas)
print(f"Cantidad de ruedas del tren", tren.ruedas)
print(f"Cantidad de ruedas del avion", avion.ruedas)

#print("-"*30)
#barco.ruedas=0
#tren.ruedas = 50
#print(f"Cantidad de ruedas del banco", barco.ruedas)
#print(f"Cantidad de ruedas del tren", tren.ruedas)
#print(f"Cantidad de ruedas del avion", avion.ruedas)
#Puedo cambiar los atributos de clase con la notacion punto de la siguiente forma:

print("-"*30)
Transporte.ruedas = 18
print(f"Cantidad de ruedas del banco", barco.ruedas)
print(f"Cantidad de ruedas del tren", tren.ruedas)
print(f"Cantidad de ruedas del avion", avion.ruedas)



#-----------------9--------------



#-----------------10--------------

#Método __str__



class Transporte:
    ruedas= 4 #Atributo de clase
    
    def __init__(self, medio, empresa,v_max,color, combustible):
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color
        self.combustible = combustible

    def imprimir(self):
        
        return f"Me desplazo por {self.medio} y uso {self.combustible}"
        return f"Soy un objeto mas.Chau!"

    def __str__(self):
        return f"Me desplazo por {self.medio} y uso {self.combustible}"
         
    

print("\033[H\033[J")          # Limpiamos la pantalla



avion = Transporte("aire", "A. Arg.", 1400, "azul y blanco", "JP1")
tren = Transporte("aire", "A. Arg.", 1400, "azul y blanco", "JP1")
barco = Transporte("mar", "Caribbean", 50, "azul", "viento")

print(avion) #me ofrece datos de ubicacion de memoria y nada mas si no esta definido __str__
print(barco)

#-----------------10--------------


#-----------------11--------------
#Podemos tener miles de objetos creados y a veces necesitamos eliminar o destruir algunos de ellos
#Eliminar objeto
#Es comun tener miles de objetos en memoria. Por ejemplo: lo puntos de una función lineal
#Por lo tanto es comun eliminarnos para no ocupar tanto espacio en memoria


class Transporte:
    ruedas= 4 #Atributo de clase
    
    def __init__(self, medio, empresa, combustible,v_max,color):
        #Atributos de instancia, varian de un objeto a otro
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color
        self.combustible = combustible
#Podemos definir otros métodos
    def imprimir(self):
        #print(f"Me desplazo por {self.medio}")
        print(f"Me desplazo por {self.medio} y uso {self.combustible}")
    def __str__(self):
        #return(f"Soy un objeto mas.Chau!")
        return(f"Me desplazo por {self.medio} y uso {self.combustible}")

print("\033[H\033[J")          # Limpiamos la pantalla


avion = Transporte("aire", "A. Arg.", 1400, "azul y blanco", "JP1")
tren = Transporte("aire", "A. Arg.", 1400, "azul y blanco", "JP1")
barco = Transporte("mar", "Caribbean", 50, "azul", "viento")

del barco #Eliminamos objeto en memoria. Si nos olvidamos de elimiar todos los objetos, python se encarga de eliminarlos

print(avion) 
print(tren)
print(barco)
#-----------------11--------------
'''
#-----------------12--------------
#Eliminamos objeto en memoria. Si nos olvidamos de elimiar todos los objetos, python se encarga de eliminarlos
#Python provee de una función: __del__



class Transporte:
    ruedas= 4 #Atributo de clase
    
    def __init__(self, medio, empresa, combustible,v_max,color="sin color"):
        #Atributos de instancia, varian de un objeto a otro
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color
        self.combustible = combustible
#Podemos definir otros métodos

    def __str__(self):
        #return(f"Soy un objeto mas.Chau!")
        return(f"Me desplazo por {self.medio} y uso {self.combustible}")

#Se ejecuta cada vez que un objeto se destruye
    def __del__(self):
        print(f"Borrado el objeto que se desplaza por {self.medio}")

print("\033[H\033[J")          # Limpiamos la pantalla

avion = Transporte("aire", "A. Arg.", 1400, "azul y blanco", "JP1")
tren = Transporte("tierra", "A. Arg.", 1400, "azul y blanco", "JP1")
barco = Transporte("mar", "Caribbean", 50, "azul", "viento")


del barco #Eliminamos objeto en memoria

print(avion)
print(tren)

#Al terminarse la ejecucuión del programa python elimina las objetos restantes con le función __del__
#ademas de los eliminados explicitamente

#-----------------12--------------

#Ir al ejemplo 6
