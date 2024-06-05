"""Desarrollar un programa que cargue los datos de un triángulo. Implementar una 
clase con los métodos para inicializar los atributos, imprimir el valor del lado con 
un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno)."""



class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        lados = [self.lado1, self.lado2, self.lado3] #Se crea una lista
        lados.sort() #Se ordena la lista en forma ascendente
        print(f"El lado mayor es: {lados[-1]}") #Se imprime el ultimo elemento (el MAYOR)

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

### Programa Principal ###
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

triangulo = Triangulo(lado1, lado2, lado3)

triangulo.imprimir_lado_mayor()
print(triangulo.tipo_triangulo())