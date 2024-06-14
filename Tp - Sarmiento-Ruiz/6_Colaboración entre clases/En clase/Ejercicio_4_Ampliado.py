"""
Crea  un  sistema  de  almacén  con  clases  "Producto"  y  "Proveedor".  Un  objeto 
"Almacén" puede contener una lista de objetos "Producto", y cada "Producto" puede 
tener un objeto "Proveedor" asociado. Implementar métodos para: agregar 
productos al almacén, agregar proveedores al almacén, mostrar los productos que 
venden al almacén los proveedores y gestionar el inventario del almacén (altas de 
productos y modificaciones de precio y listado de productos sin stock)
"""

class Proveedor:
    def __init__(self, nombre, celular):
        self.__nombre = nombre
        self.__celular = celular
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def celular(self):
        return self.__celular

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_productos(self):
        print(f"Productos de {self.__nombre}:")
        for producto in self.__productos:
            print(f"- {producto.nombre}")

    def __str__(self):
        return f"Proveedor {self.__nombre} - Celular: {self.__celular}"


class Producto:
    def __init__(self, nombre, precio, proveedor, marca, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__proveedor = proveedor
        self.__marca = marca
        self.__stock = stock

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
    def marca(self):
        return self.__marca

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = nuevo_stock

    def __str__(self):
        return f"{self.__nombre} - Marca: {self.__marca} - Precio: {self.__precio} - Stock: {self.__stock}"


class Almacen:
    def __init__(self):
        self.__productos = []
        self.__proveedores = []
        self.cargar_datos_desde_archivo()
        
    def get_proveedores(self):
        return self.__proveedores

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def agregar_proveedor(self, proveedor): #se usa para agregar un objeto Proveedor existente a la lista
        self.__proveedores.append(proveedor)
        
    def alta_proveedor(self, nombre, celular):#crea un nuevo objeto Proveedor y lo agrega a la lista
        proveedor = Proveedor(nombre, celular)
        self.__proveedores.append(proveedor)
        self.guardar_datos_en_archivo()  # Guardar datos en archivo

    def mostrar_productos_por_proveedor(self, proveedor_nombre):
        proveedor = next((p for p in self.__proveedores if p.nombre == proveedor_nombre), None)
        if proveedor:
            proveedor.mostrar_productos()
        else:
            print(f"No se encontró el proveedor {proveedor_nombre}")

    def gestionar_inventario(self):
        print("Inventario del almacén:")
        for producto in self.__productos:
            print(producto)
        print()

    def alta_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        print("Seleccione un proveedor:")
        for i, proveedor in enumerate(self.__proveedores):
            print(f"{i+1}. {proveedor.nombre} - Celular: {proveedor.celular}")
        opcion = input("Ingrese el número del proveedor o 'n' para agregar uno nuevo: ")
        if opcion.lower() == 'n':
            proveedor_nombre = input("Ingrese el nombre del proveedor: ")
            proveedor_celular = input("Ingrese el celular del proveedor: ")
            proveedor = Proveedor(proveedor_nombre, proveedor_celular)
            self.__proveedores.append(proveedor)
        else:
            proveedor = self.__proveedores[int(opcion) - 1]
        producto = Producto(nombre, marca, precio, proveedor, stock)  # Modificar aquí
        self.__productos.append(producto)
        self.guardar_datos_en_archivo()  # Guardar datos en archivo
        
 
    def modificar_precio(self, nombre, nuevo_precio):
        producto_encontrado = self.__buscar_producto(nombre)
        if producto_encontrado:
            producto_encontrado.precio = nuevo_precio
            self.guardar_datos_en_archivo()  # Guardar datos en archivo

    def productos_sin_stock(self):
        print("Productos sin stock:")
        for producto in self.__productos:
            if producto.stock == 0:
                print(producto.nombre)
        print()

    def __buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.nombre == nombre:
                return producto
        return None

    def __buscar_proveedor(self, nombre):
        for proveedor in self.__proveedores:
            if proveedor.nombre == nombre:
                return proveedor
        return None
    
    def modificar_proveedor(self, nombre, nuevo_celular):
        proveedor_encontrado = self.__buscar_proveedor(nombre)
        if proveedor_encontrado:
            proveedor_encontrado.celular = nuevo_celular
            self.guardar_datos_en_archivo()  # Guardar datos en archivo
    
    def guardar_datos_en_archivo(self):
        with open("almacen.txt", "w") as archivo:
            for proveedor in self.__proveedores:
                archivo.write(f"Proveedor:{proveedor.nombre}:{proveedor.celular}\n")
            for producto in self.__productos:
                archivo.write(f"Producto:{producto.nombre}:{producto.marca}:{producto.precio}:{producto.stock}:{producto.proveedor.nombre}\n")

    def cargar_datos_desde_archivo(self):
        try:
            with open("almacen.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(":")
                    if datos[0] == "Proveedor":
                        if len(datos) >= 3:  # Verificar que la lista tenga al menos 3 elementos
                            nombre = datos[1]
                            celular = datos[2]
                            proveedor = Proveedor(nombre, celular)
                            self.__proveedores.append(proveedor)
                        else:
                            print(f"La línea '{linea}' no tiene la estructura correcta. Se ignora.")
        except FileNotFoundError:
            pass

### Programa Principal ###

almacen = Almacen()
almacen.cargar_datos_desde_archivo()

while True:
        print("###### Menu de Inicio al Sistema Almacen ######")
        print("#                                             #")
        print("#  1. Alta de Producto                        #")
        print("#  2. Mostrar Productos por Proveedor         #")
        print("#  3. Gestionar Inventario                    #")
        print("#  4. Modificar Precio de un Producto         #")
        print("#  5. Mostrar Productos sin Stock             #")
        print("#  6. Salir                                   #")
        print("#                                             #")
        print("###### Menu de Inicio al Sistema Almacen ######")
        print()
        opcion = input("Ingrese una opción: ")
        print()
        print('#'*50)
        print()

        if opcion == "1":
            almacen.alta_producto()
            print()
            print('#'*50)

        elif opcion == "2":
            if not almacen.get_proveedores():
                print("Error: No se encontraron proveedores. Por favor, agregue proveedores antes de continuar.")
                print()
                print('#'*50)
                continue
            print("Seleccione un proveedor:")
            for i, proveedor in enumerate(almacen.get_proveedores()):
                print(f"{i+1}. {proveedor.nombre} - Celular: {proveedor.celular}")
            while True:
                try:
                    opcion_proveedor = int(input("Ingrese el número del proveedor: "))
                    proveedor_seleccionado = almacen.get_proveedores()[opcion_proveedor - 1]
                    proveedor_encontrado = almacen.__buscar_proveedor(proveedor_seleccionado.nombre)
                    if proveedor_encontrado:
                        print("Productos del proveedor:")
                        for producto in proveedor_encontrado.productos:
                            print(producto.nombre)
                    else:
                        print("Proveedor no encontrado")
                    break
                except (ValueError, IndexError):
                    print("Error: ingresaste un valor no válido. Por favor ingresa un número entre 1 y", len(almacen.get_proveedores()))
        
        elif opcion == "3":
            almacen.gestionar_inventario()
            print()
            print('#'*50)

        elif opcion == "4":
            nombre_producto = input("Ingrese el nombre del producto: ")
            producto_encontrado = almacen.__buscar_producto(nombre_producto)
            if producto_encontrado:
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                producto_encontrado.precio = nuevo_precio
                print("Precio del producto actualizado")
            else:
                print("Producto no encontrado")

        elif opcion == "5":
            print("Productos sin stock:")
            for producto in almacen.__productos:
                if producto.stock == 0:
                    print(producto.nombre)

        elif opcion == "6":
            almacen.guardar_datos_en_archivo()
            print("Modificaciones del día Guardadas en archivo.")
            print("Saliendo del Sistema....")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            print()
            print('#'*50)