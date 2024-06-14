"""
Crea  un  sistema  de  almacén  con  clases  "Producto"  y  "Proveedor".  Un  objeto 
"Almacén" puede contener una lista de objetos "Producto", y cada "Producto" puede 
tener un objeto "Proveedor" asociado. Implementar métodos para: agregar 
productos al almacén, agregar proveedores al almacén, mostrar los productos que 
venden al almacén los proveedores y gestionar el inventario del almacén (altas de 
productos y modificaciones de precio y listado de productos sin stock)
"""

class Proveedor:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_productos(self):
        for producto in self.__productos:
            print(f"Producto: {producto.nombre}, Precio: {producto.precio}")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def productos(self):
        return self.__productos


class Producto:
    def __init__(self, nombre, precio, proveedor=None):
        self.__nombre = nombre
        self.__precio = precio
        self.__proveedor = proveedor
        self.__stock = 0

    def alta_producto(self, cantidad):
        self.__stock += cantidad

    def modificar_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @property
    def proveedor(self):
        return self.__proveedor

    @property
    def stock(self):
        return self.__stock

    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: {self.__precio}, Stock: {self.__stock}"


class Almacen:
    def __init__(self):
        self.__productos = []
        self.__proveedores = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def agregar_proveedor(self, proveedor):
        self.__proveedores.append(proveedor)

    def mostrar_productos_proveedor(self, proveedor):
        for producto in self.__productos:
            if producto.proveedor == proveedor:
                print(producto)

    def gestionar_inventario(self):
        for producto in self.__productos:
            if producto.stock == 0:
                print(f"Producto sin stock: {producto.nombre}")
            else:
                print(producto)

    @property
    def productos(self):
        return self.__productos

    @property
    def proveedores(self):
        return self.__proveedores

    def __str__(self):
        return f"Almacén con {len(self.__productos)} productos y {len(self.__proveedores)} proveedores"


# Example usage
almacen = Almacen()

proveedor1 = Proveedor("Proveedor 1")
proveedor2 = Proveedor("Proveedor 2")

producto1 = Producto("Producto 1", 10.0, proveedor1)
producto2 = Producto("Producto 2", 20.0, proveedor1)
producto3 = Producto("Producto 3", 30.0, proveedor2)

almacen.agregar_producto(producto1)
almacen.agregar_producto(producto2)
almacen.agregar_producto(producto3)

almacen.agregar_proveedor(proveedor1)
almacen.agregar_proveedor(proveedor2)

print(almacen)

proveedor1.mostrar_productos()

almacen.mostrar_productos_proveedor(proveedor1)

producto1.alta_producto(10)
producto2.alta_producto(20)

almacen.gestionar_inventario()

producto1.precio = 15.0

almacen.gestionar_inventario()