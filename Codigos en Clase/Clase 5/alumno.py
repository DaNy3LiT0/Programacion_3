class Alumno:
    nro_alumnos = 0 #Cantidad de legajos existentes

#Constructor
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        Alumno.nro_alumnos +=1 #Agregamos un legajo

    #Mostrar datos del objeto

    def __str__(self):
        return f"Nombre: {self.nombre} (nota: {self.nota})"

    #damos de baja al alumno

    def __del__(self):
        Alumno.nro_alumno -=1 #Agregamos un legajo
        print("Alumno dado de baja.")
        print(f"{Alumno.nro_alumnos} legajos restantes")

    def mostrar_estado(self):
        print(f"El estado de {self.nombre} es ", end="")
        if self.nota <= 4:
            print("regular") 
        elif self.nota < 9:
            print("bueno")
        else:
            print("excelente")


#Programa principal
print("\033[H\033[J")

alumno1 = Alumno("Aldo López", 8)
alumno2 = Alumno("Juana Martín", 3)
print(alumno1)
print(alumno2)
alumno1.mostrar_estado()
alumno2.mostrar_estado()
input("Pulse enter para salir")