
#Herencia
'''
#----------------------------1------------------------------#

#Superclase para coches y camiones

class Vehiculo:
    def __init__(self, marca,color):
        self.marca = marca
        self.color = color

    def arrancar(self):
        print("Estoy en marcha")
    
    def detener(self):
        print ("Estoy detenido.")
    
    
    #Programa principal
    
    
    print("\033[H\033[J")             # Limpiamos la pantalla
    
v1 = Vehiculo("Ford", "blanco")
print(v1.color)
v1.detener()
#----------------------------1------------------------------#

#----------------------------2------------------------------#
#Defino subclases
class Vehiculo:
    def __init__(self, marca,color):
        self.marca = marca
        self.color = color

    def arrancar(self):
        print("Estoy en marcha")
    
    def detener(self):
        print ("Estoy detenido.")
    
    
    #Programa principal
    
class Coche(Vehiculo):
    
    def __init__(self, marca, color, baul):
        self.baul = baul
        super().__init__(marca, color)
        

    
    print("\033[H\033[J")             # Limpiamos la pantalla
    
v1 = Vehiculo("Ford", "blanco")
print(v1.color)
v1.detener()
print()
coche1 = Coche("Renault","azul", 503)
print(coche1.color) #Atributo de la superclase
coche1.detener()     #Metodo de la superclase

#----------------------------2------------------------------#


#----------------------------3------------------------------#

#Defino la clase camion
#Defino subclases
class Vehiculo:
    def __init__(self, marca,color):
        self.marca = marca
        self.color = color

    def arrancar(self):
        print("Estoy en marcha")
    
    def detener(self):
        print ("Estoy detenido.")
    
    
    #Programa principal
    
class Coche(Vehiculo):
    
    def __init__(self, marca, color, baul):
        self.baul = baul
        super().__init__(marca, color)
        
class Camion(Vehiculo):
    
    def __init__(self, marca, color, ruedas):
        self.ruedas = ruedas
        super().__init__(marca, color)

    
    print("\033[H\033[J")             # Limpiamos la pantalla
    
v1 = Vehiculo("Ford", "blanco")
print(v1.color)
v1.detener()
#----------------------------------------------------------#
coche1 = Coche("Renault","azul", 503)
print(coche1.color) #Atributo de la superclase
coche1.detener()     #Metodo de la superclase

#----------------------------------------------------------#
cam1 = Camion ("Ford","Rojo","18") 
print(cam1.marca)
cam1.detener()


#----------------------------3------------------------------#

#----------------------------4------------------------------#

#Defino un metodo str para vehiculos
class Vehiculo:
    def __init__(self, marca,color):
        self.marca = marca
        self.color = color

    def arrancar(self):
        print("Estoy en marcha")
    
    def detener(self):
        print ("Estoy detenido.")
        
    def __str__(self):
        return f"Soy {self.marca} color {self.color}"
    
    
    #Programa principal
    
class Coche(Vehiculo):
    
    def __init__(self, marca, color, baul):
        self.baul = baul
        super().__init__(marca, color)
        
class Camion(Vehiculo):
    
    def __init__(self, marca, color, ruedas):
        self.ruedas = ruedas
        super().__init__(marca, color)

    
    print("\033[H\033[J")             # Limpiamos la pantalla
    

coche1 = Coche("Renault","azul", 503)
cam1 = Camion ("Ford","Rojo","18") 
print(cam1)
print(coche1)

#----------------------------4------------------------------#


#----------------------------5------------------------------#

#Defino un metodo str para el camion.para que muestre sus propios atributos
class Vehiculo:
    def __init__(self, marca,color):
        self.marca = marca
        self.color = color

    def arrancar(self):
        print("Estoy en marcha")
    
    def detener(self):
        print ("Estoy detenido.")
        
    def __str__(self):
        return f"Soy {self.marca} color {self.color}"
    
    
    #Programa principal
    
class Coche(Vehiculo):
    
    def __init__(self, marca, color, baul):
        self.baul = baul
        super().__init__(marca, color)
        
class Camion(Vehiculo):
    
    def __init__(self, marca, color, ruedas):
        self.ruedas = ruedas
        super().__init__(marca, color)

    def __str__(self):
        return f"Soy un camion {self.marca} color {self.color} y tengo {self.ruedas} ruedas"
    
    


print("\033[H\033[J")             # Limpiamos la pantalla
    

coche1 = Coche("Renault","azul", 503)
cam1 = Camion ("Ford","Rojo","18") 
print(coche1)

print(cam1) #Reemplace el metodo de la superclase (__str__) por el __str___ de la clase hija

#----------------------------5------------------------------#



#----------------------------6------------------------------#

#Puedo optimizar mi código
class Vehiculo:
    def __init__(self, marca,color):
        self.marca = marca
        self.color = color

    def arrancar(self):
        print("Estoy en marcha")
    
    def detener(self):
        print ("Estoy detenido.")
        
    def __str__(self):
        return f"Soy un vehiculo {self.marca} color {self.color} y tengo {self.ruedas} ruedas"
    
    
    #Programa principal
    
class Coche(Vehiculo):
    
    def __init__(self, marca, color, ruedas):
        self.ruedas = ruedas
        super().__init__(marca, color)
        
class Camion(Vehiculo):
    
    def __init__(self, marca, color, ruedas):
        self.ruedas = ruedas
        super().__init__(marca, color)


print("\033[H\033[J")             # Limpiamos la pantalla
    

coche1 = Coche("Renault","azul", 4)
cam1 = Camion ("Ford","Rojo",18) 
print(coche1)

print(cam1) #Reemplace el metodo de la superclase (__str__) por el __str___ de la clase hija

#----------------------------6------------------------------#
'''
#----------------------------7------------------------------#

#Puedo optimizar mi código. Si tengo ruedas en todas las subclasepodemos poner como atributo en la superclase
class Vehiculo:
    def __init__(self, marca,color,ruedas):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas

    def arrancar(self):
        print("Estoy en marcha")
    
    def detener(self):
        print ("Estoy detenido.")
        
    def __str__(self):
        return f"Soy un vehiculo {self.marca} color {self.color} y tengo {self.ruedas} ruedas"
    
    
    #Programa principal
    
class Coche(Vehiculo):
    
    def __init__(self, marca, color,ruedas):
        super().__init__(marca, color, ruedas)
        
class Camion(Vehiculo):
    
    def __init__(self, marca, color,ruedas):
        super().__init__(marca, color, ruedas)


print("\033[H\033[J")             # Limpiamos la pantalla
    

coche1 = Coche("Renault","azul", 4)
cam1 = Camion ("Ford","Rojo",18) 
print(coche1)

print(cam1) #Reemplace el metodo de la superclase (__str__) por el __str___ de la clase hija

#----------------------------7------------------------------#
#Ir a las diapósitivas