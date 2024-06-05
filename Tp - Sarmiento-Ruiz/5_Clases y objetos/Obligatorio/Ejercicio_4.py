"""
Realizar un programa que modele una cuenta corriente. Cada cliente se identifica 
con un nro. de cuenta, CBU, nombre y monto total. Las operaciones permitidas para
la cuenta son: ver saldo, ver datos de la cuenta, realizar extracciones y realizar 
depósitos
"""

import random

class Cuenta:
    def __init__(self, dni, numero_cuenta, cbu, nombre, saldo):
        self.numero_cuenta = numero_cuenta
        self.cbu = cbu
        self.nombre = nombre
        self.saldo = saldo
        self.dni = dni

    def ver_saldo(self):
        print(f"Su saldo es: {self.saldo}")

    def ver_datos_cuenta(self):
        print(f"Titular: {self.nombre}")
        print(f"N° Cuenta: {self.numero_cuenta}")
        print(f"CBU: {self.cbu}")

    def realizar_extraccion(self, monto):
        if monto > self.saldo:
            print("No hay suficiente saldo para realizar la extracción")
            print(f"Su saldo es: {self.saldo}")
        else:
            self.saldo -= monto
            print(f"Extracción de {monto} realizada con éxito")

    def realizar_deposito(self, monto):
        self.saldo += monto
        print(f"Depósito de {monto} realizado con éxito")


class Banco:
    def __init__(self):
        self.cuentas = {}

    def abrir_cuenta(self, dni, nombre, saldo):
        random_prefix = str(random.randint(10, 99))
        numero_cuenta = random_prefix + dni # Agregar dos números aleatorios antes del DNI
        sucursal = "5586"
        random_middle = str(random.randint(100000, 999999))
        cbu = sucursal + random_middle + numero_cuenta
        cuenta = Cuenta(dni, numero_cuenta, cbu, nombre, saldo)
        self.cuentas[dni] = cuenta

        # Guardar datos en un archivo .txt
        with open("cuentas.txt", "a") as archivo:
            archivo.write(f"DNI: {dni}\n")
            archivo.write(f"Nombre: {nombre}\n")
            archivo.write(f"Saldo: {saldo}\n")
            archivo.write(f"Número de cuenta: {numero_cuenta}\n")
            archivo.write(f"CBU: {cbu}\n\n")

        return cuenta

    def ver_saldo(self, dni):
        cuenta = banco.cuentas.get(dni)
        if cuenta:
            cuenta.ver_saldo()
        else:
            print("No se encontró una cuenta asociada al DNI:", dni)

    def ver_datos_cuenta(self, dni):
        cuenta = banco.cuentas.get(dni)
        if cuenta:
            cuenta.ver_datos_cuenta()
        else:
            print("No se encontró una cuenta asociada al DNI:", dni)

    def realizar_extraccion(self, dni, monto):
        cuenta = banco.cuentas.get(dni)
        if cuenta:
            cuenta.realizar_extraccion(monto)
        else:
            print("No se encontró una cuenta asociada al DNI: ", dni)

    def realizar_deposito(self, dni, monto):
        cuenta = banco.cuentas.get(dni)
        if cuenta:
            cuenta.realizar_deposito(monto)
        else:
            print("No se encontró una cuenta asociada al DNI:", dni)


banco = Banco()

while True:
    print("")
    print("#" * 38)
    print("#             Menú             #")
    print("#  1. Abrir cuenta             #")
    print("#  2. Ver saldo                #")
    print("#  3. Ver datos de la cuenta   #")
    print("#  4. Realizar extracción      #")
    print("#  5. Realizar depósito        #")
    print("#  6. Salir                    #")
    print("#" * 38)
    opcion = input("Ingresa una opción: ")
    print("#" * 38)
    print("")


    if opcion == "1":
        dni = input("Ingresa tu DNI (máximo 8 dígitos): ")
        while len(dni) > 8:
            print("Error: El DNI no puede tener más de 8 dígitos")
            dni = input("Ingresa tu DNI (máximo 8 dígitos): ")
        nombre = input("Ingresa tu nombre: ")
        saldo = float(input("Ingresa el monto con el cual vas abrir la cuenta: "))
        print("#" * 38)
        print("")
        print("Verificar datos:")
        print("DNI:", dni)
        print("Nombre:", nombre)
        print("Saldo:", saldo)
        print("")
        print("#" * 38)
        confirmacion = input("¿Los datos son correctos? (s/n): ")
        if confirmacion.lower() == "s":
            dni = dni.zfill(8)
            banco.abrir_cuenta(dni, nombre, saldo)
            print("Cuenta creada con éxito!")
        else:
            print("Operación cancelada")
    
    elif opcion == "2":
        dni = input("Ingresa tu DNI: ")
        print("")
        print("#" * 38)
        print("")
        banco.ver_saldo(dni)
    
    elif opcion == "3":
        dni = input("Ingresa tu DNI: ")
        print("")
        print("#" * 38)
        print("")
        banco.ver_datos_cuenta(dni)
    
    elif opcion == "4":
        dni = input("Ingresa tu DNI: ")
        monto = float(input("Ingresa el monto a extraer: "))
        print("")
        print("#" * 38)
        print("")
        banco.realizar_extraccion(dni, monto)
    
    elif opcion == "5":
        dni = input("Ingresa tu DNI: ")
        monto = float(input("Ingresa el monto a depositar: "))
        print("")
        print("#" * 38)
        print("")
        banco.realizar_deposito(dni, monto)
    
    elif opcion == "6":
        print("Adiós!")
        break
    
    else:
        print('Opción inválida!')
        input('ENTER para continuar')