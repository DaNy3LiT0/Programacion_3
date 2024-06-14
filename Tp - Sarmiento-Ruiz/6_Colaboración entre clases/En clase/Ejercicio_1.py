"""
Plantear  una  clase  Club  y  otra  clase  Socio.  La  clase  Socio  debe  tener  los 
siguientes atributos: nombre y la antigüedad en el club (en años). 
La clase Club debe tener como atributos 3 objetos de la clase Socio. Definir 
un  método  para  imprimir  el  nombre  del  socio  con  mayor  antigüedad  en  el 
club.
"""

class Club:
    def __init__(self, socio1, socio2, socio3):
        self.__socio1 = socio1
        self.__socio2 = socio2
        self.__socio3 = socio3

    def imprimir_socio_mayor_antiguedad(self):
        socios = [self.__socio1, self.__socio2, self.__socio3]
        socios.sort(key=lambda x: x.get_antiguedad(), reverse=True)
        print(f"El socio con mayor antigüedad es: {socios[0].get_nombre()}")
        
class Socio:
    def __init__(self, nombre, antiguedad):
        self.__nombre = nombre
        self.__antiguedad = antiguedad

    def get_nombre(self):
        return self.__nombre

    def get_antiguedad(self):
        return self.__antiguedad
    
### Programa Principal

socio1 = Socio("Juan", 5)
socio2 = Socio("Maria", 10)
socio3 = Socio("Pedro", 7)

club = Club(socio1, socio2, socio3)
club.imprimir_socio_mayor_antiguedad()