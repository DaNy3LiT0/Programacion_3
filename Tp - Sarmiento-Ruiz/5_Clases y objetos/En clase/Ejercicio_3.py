"""Escribir una clase en python con 2 métodos: get_string y print_string. get_string 
acepta una cadena ingresada por el usuario y print_string imprime la cadena en 
mayúsculas"""

class MyClass:
    def get_string(self):
        self.cadena = input("Ingrese una cadena: ")
        return self.cadena

    def print_string(self):
        print(self.cadena.upper())


mi_clase = MyClass()

mi_clase.get_string()

mi_clase.print_string()