'''
#--------------------------------1---------------------------------#
#Definimos la clase cliente
class Cliente:
    def __init__(self, nombre ,monto = 0): #si no agregamos es igual al cero al iniciar
        self.nombre = nombre
        self.saldo = monto
        print (f"Cuenta abierta. ")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)
    

#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

c1 = Cliente("Ana", 1000)
#print(c1.saldo)
c2 = Cliente("Cristina")

#--------------------------------1---------------------------------#

#--------------------------------2---------------------------------#    
#Requerimos de un ID por si tenemos clientes que coinciden con el nombre
class Cliente:
    nrocuenta = 0  #Atributo de clase:compartido por todos los elementos de la clase
    def __init__(self, nombre,monto = 0):
        self.nombre = nombre
        self.saldo = monto
        Cliente.nrocuenta = Cliente.nrocuenta + 1 #Para usar los atributos de la clase debo usar la notacion punto
        self.id= Cliente.nrocuenta
        print (f"Cuenta abierta (ID: {self.id})")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)


#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

c1 = Cliente("Ana", 1000)
c2 = Cliente("Cristina")
c3 = Cliente("Graciela",2000)
    
    
#--------------------------------2---------------------------------#    

#----------------------3-----------------------------------------#
#necesitamos que los clientes puedan hacer extracciones y
class Cliente:
    nrocuenta = 0  #Atributo de clase:compartido por todos los elementos de la clase
    def __init__(self, nombre,monto = 0):
        self.nombre = nombre
        self.saldo = monto
        Cliente.nrocuenta = Cliente.nrocuenta + 1 #Para usar los atributos de la clase debo usar la notacion punto
        self.id= Cliente.nrocuenta
        print (f"Cuenta abierta (ID: {self.id})")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)
    
    def Depositar(self,monto):
        self.saldo= self.saldo + monto
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")
        print(f"Depositado: {monto}, saldo actual: {self.saldo} ")
        print ("-"*40)
    
    
    def Total(self):
        return self.saldo


#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

c1 = Cliente("Ana", 1000)
c2 = Cliente("Cristina")
c3 = Cliente("Graciela",2000)

c2.Depositar(3000)
#----------------------3-----------------------------------------#

#----------------------4-----------------------------------------#

#necesitamos que los clientes puedan hacer extracciones y
class Cliente:
    nrocuenta = 0  #Atributo de clase:compartido por todos los elementos de la clase
    def __init__(self, nombre,monto = 0):
        self.nombre = nombre
        self.saldo = monto
        Cliente.nrocuenta = Cliente.nrocuenta + 1 #Para usar los atributos de la clase debo usar la notacion punto
        self.id= Cliente.nrocuenta
        print (f"Cuenta abierta (ID: {self.id})")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)
    
    def Depositar(self,monto):
        self.saldo= self.saldo + monto
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")
        print(f"Depositado: {monto}, saldo actual: {self.saldo} ")
        print ("-"*40)
    
    def Extraer(self,monto):
        self.saldo= self.saldo - monto
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")
        print(f"Retirado: {monto}, saldo actual: {self.saldo} ")
        print ("-"*40)
    
    def Total(self):
        return self.saldo


#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

c1 = Cliente("Ana", 1000)
c2 = Cliente("Cristina")
c3 = Cliente("Graciela",2000)

c2.Depositar(3000)
c3.Extraer(1000)

#----------------------4-----------------------------------------#


#----------------------5-----------------------------------------#
#necesitamos que controle las extracciones porque si el cleinte quiere sacar un monto superior al saldo no debe dejar permitir el banco
class Cliente:
    nrocuenta = 0  #Atributo de clase:compartido por todos los elementos de la clase
    def __init__(self, nombre,monto = 0):
        self.nombre = nombre
        self.saldo = monto
        Cliente.nrocuenta = Cliente.nrocuenta + 1 #Para usar los atributos de la clase debo usar la notacion punto
        self.id= Cliente.nrocuenta
        print (f"Cuenta abierta (ID: {self.id})")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)
    
    def Depositar(self,monto):
        self.saldo= self.saldo + monto
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")
        print(f"Depositado: {monto}, saldo actual: {self.saldo} ")
        print ("-"*40)
    
    def Extraer(self,monto):
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")

        if self.saldo >= monto:
            print(f"saldo anterior: {self.saldo} ")
            self.saldo= self.saldo - monto
            print(f"Extraido: {monto}, saldo actual: {self.saldo} ")
        else:
            print(f"DENEGADO: {monto}, saldo actual: {self.saldo} ")
        
        print ("-"*40)
    
    def Total(self):
        return self.saldo

#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

c1 = Cliente("Ana", 1000)
c2 = Cliente("Cristina")
c3 = Cliente("Graciela",2000)

c2.Depositar(3000)
c3.Extraer(10000)


#----------------------5-----------------------------------------#

#----------------------6-----------------------------------------#
#Necesitamos tener un metodo que retorne los saldos de  cada cliente   
class Cliente:
    nrocuenta = 0  #Atributo de clase:compartido por todos los elementos de la clase
    def __init__(self, nombre,monto = 0):
        self.nombre = nombre
        self.saldo = monto
        Cliente.nrocuenta = Cliente.nrocuenta + 1 #Para usar los atributos de la clase debo usar la notacion punto
        self.id= Cliente.nrocuenta
        print (f"Cuenta abierta (ID: {self.id})")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)
    
    def Depositar(self,monto):
        self.saldo= self.saldo + monto
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")
        print(f"Depositado: {monto}, saldo actual: {self.saldo} ")
        print ("-"*40)
    
    def Extraer(self,monto):
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")

        if self.saldo >= monto:
            print(f"saldo anterior: {self.saldo} ")
            self.saldo= self.saldo - monto
            print(f"Extraido: {monto}, saldo actual: {self.saldo} ")
        else:
            print(f"DENEGADO: {monto}, saldo actual: {self.saldo} ")
        
        print ("-"*40)
    
    def Total(self):
        return self.saldo

#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla

c1 = Cliente("Ana", 1000)
c2 = Cliente("Cristina")
c3 = Cliente("Graciela",2000)

c2.Depositar(3000)
c3.Extraer(10000)

print(c3.Total()+c2.Total()+c1.Total())

#----------------------6-----------------------------------------#


#----------------------7-----------------------------------------#
#Requerimos ahora crear la clase banco

class Cliente:
    nrocuenta = 0  #Atributo de clase:compartido por todos los elementos de la clase
    def __init__(self, nombre,monto = 0):
        self.nombre = nombre
        self.saldo = monto
        Cliente.nrocuenta = Cliente.nrocuenta + 1 #Para usar los atributos de la clase debo usar la notacion punto
        self.id= Cliente.nrocuenta
        print (f"Cuenta abierta (ID: {self.id})")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)
    
    def Depositar(self,monto):
        self.saldo= self.saldo + monto
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")
        print(f"Depositado: {monto}, saldo actual: {self.saldo} ")
        print ("-"*40)
    
    def Extraer(self,monto):
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")

        if self.saldo >= monto:
            print(f"saldo anterior: {self.saldo} ")
            self.saldo= self.saldo - monto
            print(f"Extraido: {monto}, saldo actual: {self.saldo} ")
        else:
            print(f"DENEGADO: {monto}, saldo actual: {self.saldo} ")
        
        print ("-"*40)
    
    def Total(self):
        return self.saldo

class Banco:
    def __init__(self,nombre):
        self.nombre = nombre
#requiero tres clientes en elbanco instancio la clase cliente como atriburo de la clase banco        
        self.c1 = Cliente("Germán",5000) #Colaboración entre clases


#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla


banco1 = Banco("Banco Santiago del Estero")



#----------------------7-----------------------------------------#

#----------------------8-----------------------------------------#
#Creamos los tres clientes que solicita el banco

class Cliente:
    nrocuenta = 0  #Atributo de clase:compartido por todos los elementos de la clase
    def __init__(self, nombre,monto = 0):
        self.nombre = nombre
        self.saldo = monto
        Cliente.nrocuenta = Cliente.nrocuenta + 1 #Para usar los atributos de la clase debo usar la notacion punto
        self.id= Cliente.nrocuenta
        print (f"Cuenta abierta (ID: {self.id})")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)
    
    def Depositar(self,monto):
        self.saldo= self.saldo + monto
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")
        print(f"Depositado: {monto}, saldo actual: {self.saldo} ")
        print ("-"*40)
    
    def Extraer(self,monto):
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")

        if self.saldo >= monto:
            print(f"saldo anterior: {self.saldo} ")
            self.saldo= self.saldo - monto
            print(f"Extraido: {monto}, saldo actual: {self.saldo} ")
        else:
            print(f"DENEGADO: {monto}, saldo actual: {self.saldo} ")
        
        print ("-"*40)
    
    def Total(self):
        return self.saldo

class Banco:
    def __init__(self,nombre):
        self.nombre = nombre
#requiero tres clientes en elbanco instancio la clase cliente como atriburo de la clase banco        
        self.c1 = Cliente("Germán",5000) #Colaboración entre clases
        self.c2 = Cliente("Hernán",8000) #Colaboración entre clases
        self.c3 = Cliente("Facundo",7500) #Colaboración entre clases
        

#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla



banco1 = Banco("Banco Santiago del Estero")

#----------------------8-----------------------------------------#


#----------------------9-----------------------------------------#

#Tenemos que simular las operaciones 

class Cliente:
    nrocuenta = 0  #Atributo de clase:compartido por todos los elementos de la clase
    def __init__(self, nombre,monto = 0):
        self.nombre = nombre
        self.saldo = monto
        Cliente.nrocuenta = Cliente.nrocuenta + 1 #Para usar los atributos de la clase debo usar la notacion punto
        self.id= Cliente.nrocuenta
        print (f"Cuenta abierta (ID: {self.id})")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)
    
    def Depositar(self,monto):
        self.saldo= self.saldo + monto
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")
        print(f"Depositado: {monto}, saldo actual: {self.saldo} ")
        print ("-"*40)
    
    def Extraer(self,monto):
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")

        if self.saldo >= monto:
            print(f"saldo anterior: {self.saldo} ")
            self.saldo= self.saldo - monto
            print(f"Extraido: {monto}, saldo actual: {self.saldo} ")
        else:
            print(f"DENEGADO: {monto}, saldo actual: {self.saldo} ")
        
        print ("-"*40)
    
    def Total(self):
        return self.saldo

class Banco:
    def __init__(self,nombre):
        self.nombre = nombre
#requiero tres clientes en elbanco instancio la clase cliente como atriburo de la clase banco        
        self.c1 = Cliente("Germán",5000) #Colaboración entre clases
        self.c2 = Cliente("Hernán",8000) #Colaboración entre clases
        self.c3 = Cliente("Facundo",7500) #Colaboración entre clases
        
    def operar(self):
        self.c1.Extraer(200)
        self.c3.Extraer(1200)
        self.c2.Depositar(1500)
        self.c3.Depositar(4100)
        self.c2.Extraer(10000)
        self.c1.Depositar(1100)
        
#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla



banco1 = Banco("Banco Santiago del Estero")
banco1.operar()

#----------------------9-----------------------------------------#


#----------------------10-----------------------------------------#
#Generar al final del dia la cantidad depositada en el banco
class Cliente:
    nrocuenta = 0  #Atributo de clase:compartido por todos los elementos de la clase
    def __init__(self, nombre,monto = 0):
        self.nombre = nombre
        self.saldo = monto
        Cliente.nrocuenta = Cliente.nrocuenta + 1 #Para usar los atributos de la clase debo usar la notacion punto
        self.id= Cliente.nrocuenta
        print (f"Cuenta abierta (ID: {self.id})")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)
    
    def Depositar(self,monto):
        self.saldo= self.saldo + monto
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")
        print(f"Depositado: {monto}, saldo actual: {self.saldo} ")
        print ("-"*40)
    
    def Extraer(self,monto):
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")

        if self.saldo >= monto:
            print(f"saldo anterior: {self.saldo} ")
            self.saldo= self.saldo - monto
            print(f"Extraido: {monto}, saldo actual: {self.saldo} ")
        else:
            print(f"DENEGADO: {monto}, saldo actual: {self.saldo} ")
        
        print ("-"*40)
    
    def Total(self):
        return self.saldo

class Banco:
    def __init__(self,nombre):
        self.nombre = nombre
#requiero tres clientes en elbanco instancio la clase cliente como atriburo de la clase banco        
        self.c1 = Cliente("Germán",5000) #Colaboración entre clases
        self.c2 = Cliente("Hernán",8000) #Colaboración entre clases
        self.c3 = Cliente("Facundo",7500) #Colaboración entre clases
        
    def operar(self):
        self.c1.Extraer(200)
        self.c3.Extraer(1200)
        self.c2.Depositar(1500)
        self.c3.Depositar(4100)
        self.c2.Extraer(10000)
        self.c1.Depositar(1100)
        
    def reportar(self):         
        suma = self.c3.Total() + self.c2.Total() + self.c1.Total()  #Son atributos de instancia del banco
        print (f" Banco {self.nombre}")
        print(f"TOTAL DEPOSITOS: {suma}")
        print ("-"*40)
    



#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla


banco1 = Banco("Banco Santiago del Estero")
banco1.operar()
banco1.reportar()




#----------------------10-----------------------------------------#

'''

#----------------------11-----------------------------------------#

class Cliente:
    nrocuenta = 0  #Atributo de clase:compartido por todos los elementos de la clase
    def __init__(self, nombre,monto = 0):
        self.nombre = nombre
        self.saldo = monto
        Cliente.nrocuenta = Cliente.nrocuenta + 1 #Para usar los atributos de la clase debo usar la notacion punto
        self.id= Cliente.nrocuenta
        print (f"Cuenta abierta (ID: {self.id})")
        print (f"Cliente: {self.nombre}, saldo inicial: ${self.saldo} ")
        print ("-"*40)
    
    def Depositar(self,monto):
        self.saldo= self.saldo + monto
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")
        print(f"Depositado: {monto}, saldo actual: {self.saldo} ")
        print ("-"*40)
    
    def Extraer(self,monto):
        print(f"Cuenta ID: {self.id} Cliente: {self.nombre}")

        if self.saldo >= monto:
            print(f"saldo anterior: {self.saldo} ")
            self.saldo= self.saldo - monto
            print(f"Extraido: {monto}, saldo actual: {self.saldo} ")
        else:
            print(f"DENEGADO: {monto}, saldo actual: {self.saldo} ")
        
        print ("-"*40)
    
    def Total(self):
        return self.saldo

class Banco:
    def __init__(self,nombre):
        self.nombre = nombre
#requiero tres clientes en elbanco instancio la clase cliente como atriburo de la clase banco (atributos de clase)        
        self.c1 = Cliente("Germán",5000) #Colaboración entre clases
        self.c2 = Cliente("Hernán",8000) #Colaboración entre clases
        self.c3 = Cliente("Facundo",7500) #Colaboración entre clases
        
    def operar(self):
        self.c1.Extraer(200)
        self.c3.Extraer(1200)
        self.c2.Depositar(1500)
        self.c3.Depositar(4100)
        self.c2.Extraer(10000)
        self.c1.Depositar(1100)
        
    def reportar(self):         
        suma = self.c3.Total() + self.c2.Total() + self.c1.Total()  #Son atributos de instancia del banco
        print (f" Banco {self.nombre}")
        print(f"TOTAL DEPOSITOS: {suma}")
        print ("-"*40)
    



#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla


banco1 = Banco("Banco Santiago del Estero")
banco1.operar()
banco1.reportar()



#Existen algunos atributos que deberian estar ocultos por ejemplo:


print(Cliente.nrocuenta)

#Si hago

c4 = Cliente("maria",1000)
print(c4.saldo)
c4.saldo = -3000000




print(banco1.c1.saldo)
banco1.c1.saldo = -3000000
print(banco1.c1.saldo)

#DEsde afuera puedo modicar valores de atributos y eso es malo..
#Tiene que ver con el concepto de encapsulamiento algunos atributos deberian solo medoficarse con operacioon de extraccion o depositos
#Ir a la diapositivas del ejemplo bancio

#----------------------11-----------------------------------------#









