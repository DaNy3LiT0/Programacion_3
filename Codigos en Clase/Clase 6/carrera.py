class Materia:
    def __init__(self,nombre,profesor,fecha):
        self.nombre = nombre
        self.profesor = profesor
        self.fecha_inicio = fecha
        
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self,fecha):
        if  fecha < 2006:
            self.__fecha_inicio = 2006
        else:
            self.__fecha_inicio = fecha

class Carrera:
    def __init__(self,nombre):
        self.nombre = nombre
        self.materias = {}
        
    def agregar_materia(self,materia, codigo):
        self.materias[codigo] = materia



#Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla


carrera1 = Carrera("Ingenieria en sistemas")
algebra = Materia("Algebra", "Juan Quinteros", 2004)
fisica = Materia("Fisica", "Calderon de la Vega", 2012)
programacion =Materia("Programacion", "Jose Alvarez", 2010)


carrera1.agregar_materia(algebra,201)
carrera1.agregar_materia(fisica,202)
carrera1.agregar_materia(programacion,203)

print(f"La fecha de inicio es {algebra.nombre} es {algebra.fecha_inicio}" )
print(f"La fecha de inicio es {fisica.nombre} es {fisica.fecha_inicio}" )
print(f"La fecha de inicio es {programacion.nombre} es {programacion.fecha_inicio}" )