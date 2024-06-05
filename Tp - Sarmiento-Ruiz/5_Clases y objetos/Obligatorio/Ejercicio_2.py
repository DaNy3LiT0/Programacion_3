"""
Realizar un programa en el cual se declaren dos valores enteros por teclado 
utilizando el método __init__. Calcular después la suma, resta, multiplicación y 
división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.
"""

class Calculadora:
    def __init__(self):
        self.x = int(input("Ingrese un valor: "))
        self.n = int(input("Ingrese otro valor: "))
        
    def suma(self):
        return self.x + self.n
    
    def resta(self):
        return self.x - self.n
        
    def multiplicacion(self):
        return self.x * self.n
        
    def division(self):
        return self.x / self.n
    

calculo = Calculadora()
print("El resultado de las operaciones con los valores ingresados son: ")
print("Suma ==> ", calculo.suma())
print("Resta ==> ", calculo.resta())
print("Multiplicación ==> ", calculo.multiplicacion())
print("División ==> ", calculo.division())
