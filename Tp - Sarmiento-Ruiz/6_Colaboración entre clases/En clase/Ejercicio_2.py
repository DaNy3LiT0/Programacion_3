""" 
Crea un sistema de tienda en línea con clases como "Producto", 
"Carrito" y "Cliente". Un objeto "Carrito" puede contener una 
lista de productos que el cliente ha agregado, y el objeto "Cliente" 
puede tener un objeto "Carrito" asociado. 
Implementar métodos para agregar clientes a la tienda, agregar 
productos al carrito, calcular el total de la compra y procesar el pago.
"""



class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

class Carrito:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def get_productos(self):
        return self.__productos

    def calcular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.get_precio()
        return total

class Cliente:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrito = Carrito()

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_carrito(self):
        return self.__carrito

    def procesar_pago(self):
        total = self.__carrito.calcular_total()
        print(f"Nombre: {self.get_apellido()} {self.get_nombre()}")
        print(f"El total de la compra es: ${total:.2f}")
        print("Pago procesado con éxito")
        print()  # Agregamos un salto de línea para separar los resultados

        
class Tienda:
    def __init__(self):
        self.__clientes = []
        
    def get_clientes(self):
        return self.__clientes

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)


### Programa Principal ###

tienda = Tienda()

cliente1 = Cliente("Daniel", "Sarmiento")
cliente1.get_carrito().agregar_producto(Producto("Producto 1", 99.99))
cliente1.get_carrito().agregar_producto(Producto("Producto 2", 149.99))
cliente1.get_carrito().agregar_producto(Producto("Producto 4", 29.99))

tienda.agregar_cliente(cliente1)

cliente2 = Cliente("Agustin", "Ruiz")
cliente2.get_carrito().agregar_producto(Producto("Producto 3", 79.99))
cliente2.get_carrito().agregar_producto(Producto("Producto 5", 49.99))

tienda.agregar_cliente(cliente2)

# Llamamos a procesar_pago para cada cliente
for cliente in tienda.get_clientes():
    cliente.procesar_pago()

