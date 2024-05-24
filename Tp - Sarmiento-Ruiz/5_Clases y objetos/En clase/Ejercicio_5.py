"""Realizar un programa que tenga una clase Persona con las siguientes características.
La clase tendrá como atributos el nombre y la edad de una persona. Implementar los
métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la 
persona es mayor de edad o no"""

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

        if self.edad >= 18:
            print("La persona es mayor de edad.")
        else:
            print("La persona no es mayor de edad.")


persona = Persona()
persona.mostrar_datos()