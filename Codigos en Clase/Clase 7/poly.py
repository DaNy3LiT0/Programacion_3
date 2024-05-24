#Polomorfismo

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def calcular(self):
        area_cuadrado = self.lado * self.lado
        return area_cuadrado

#--------------------------------------------------

class Circulo:
    
    def __init__(self, radio):
        self.radio = radio

    def calcular(self):
        area_circulo = 3.144159265359 * self.radio **2
        return area_circulo


#--------------------------------------------------

class Rectangulo:
    
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        
    def calcular(self):
        area_rect = self.lado1 * self.lado2
        return area_rect
        

#--------------------------------------------------


#Esta funcion no le importa si es un cuadrado, circulo, etc.lo que leimporta es que todos esos objets tengan elmismop metodo
#Por lo tanto puedo escribir una funcion generica que funcione con todos los objhetops
def mostrar_area(x):
    print (x.calcular())

print("\033[H\033[J")             # Limpiamos la pantalla

c1 = Cuadrado(10)
a1 = Circulo(10)
r1 = Rectangulo(5,10)

mostrar_area(c1)
mostrar_area(a1)
mostrar_area(r1)