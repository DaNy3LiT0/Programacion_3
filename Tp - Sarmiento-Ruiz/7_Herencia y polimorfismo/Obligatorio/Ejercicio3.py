'''Sistema de ventas en línea: Crea una jerarquía de clases para modelar un sistema de ventas en línea. Con una clase base "Producto" que contenga atributos comunes como nombre, precio y disponibilidad. Luego, crea clases derivadas como "Electrodoméstico", "Ropa" y "Juguete" que hereden de la clase base y proporcionen implementaciones específicas para características y métodos relacionados con cada tipo de producto. '''


class Producto:
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Disponibilidad: {self.disponibilidad}"

class Electrodoméstico(Producto):
    def __init__(self, nombre, precio, disponibilidad, marca, modelo):
        super().__init__(nombre, precio, disponibilidad)
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return (super().__str__() + f", Marca: {self.marca} y Modelo: {self.modelo}")

class Ropa(Producto):
    def __init__(self, nombre, precio, disponibilidad, talla, color):
        super().__init__(nombre, precio, disponibilidad)
        self.talla = talla
        self.color = color

    def __str__(self):
        return (super().__str__() + f", Talle: {self.talla} y color: {self.color}")

class Juguete(Producto):
    def __init__(self, nombre, precio, disponibilidad, edad, tamaño, categoría):
        super().__init__(nombre, precio, disponibilidad)
        self.edad = edad
        self.tamaño = tamaño
        self.categoría = categoría

    def __str__(self):
        return (super().__str__() + f", Edad Recomendada: {self.edad}, Tamaño: {self.tamaño} y categoría: {self.categoría}")



electrodoméstico = Electrodoméstico("Licuadora", 150.00, True, "Gafa", "X21R2")
ropa = Ropa("Camiseta", 25.00, True, "M", "Gris")
juguete = Juguete("Lego", 50.00, False, 6, "Mediano", "Niños")

print(electrodoméstico)
print(ropa)
print(juguete)