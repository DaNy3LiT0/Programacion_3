import json

class ObraSocial:
    def __init__(self, nombre, numero_asociado, tipo_plan):
        self.nombre = nombre
        self.numero_asociado = numero_asociado
        self.tipo_plan = tipo_plan

    def to_string(self):
        return f"{self.nombre};{self.numero_asociado};{self.tipo_plan}"


class Paciente:
    def __init__(self, dni, obra_social, nombre, apellido, numero_habitacion, estado):
        self.dni = dni
        self.obra_social = obra_social
        self.nombre = nombre
        self.apellido = apellido
        self.numero_habitacion = numero_habitacion
        self.estado = estado

    def ver_datos(self):
        return f"DNI: {self.dni}\nNombre: {self.nombre} {self.apellido}\nObra Social: {self.obra_social.nombre} - {self.obra_social.numero_asociado} - {self.obra_social.tipo_plan}\nHabitación: {self.numero_habitacion}\nEstado: {self.estado}"

    def ver_estado(self):
        return self.estado

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado


def cargar_datos_paciente(pacientes, dni):
    # Verificar si el DNI ya existe en el archivo
    if dni_existente(dni, pacientes):
        print("Un paciente con ese DNI ya existe.")
        return None

    apellido = input("Ingrese apellido del paciente: ")
    nombre = input("Ingrese nombre del paciente: ")

    # Consultar si el paciente tiene obra social
    tener_obra_social = input("¿Tiene obra social? (s/n): ")
    if tener_obra_social.lower() == 's':
        nombre_obra_social = input("Ingrese nombre de la obra social: ")
        try:
            numero_asociado = input("Ingrese número de asociado: ")
        except ValueError:
            print("Error: El número de asociado debe ser un numero entero")
            return None
        tipo_plan = input("Ingrese tipo de plan: ")
        obra_social = ObraSocial(nombre_obra_social, numero_asociado, tipo_plan)
    else:
        obra_social = ObraSocial("", "", "")

    estado = int(input("Ingrese estado del paciente (1: Habitación común, 2: Terapia intermedia, 3: Terapia intensiva): "))
    if estado == 1:
        estado_str = "Habitación común"
        if not pacientes:
            numero_habitacion = 100
        else:
            ultimo_paciente = pacientes[-1]
            if ultimo_paciente.estado == "Habitación común":
                numero_habitacion = ultimo_paciente.numero_habitacion + 1
            else:
                numero_habitacion = 100
    elif estado == 2:
        estado_str = "Terapia intermedia"
        if not pacientes:
            numero_habitacion = 200
        else:
            ultimo_paciente = pacientes[-1]
            if ultimo_paciente.estado == "Terapia intermedia":
                numero_habitacion = ultimo_paciente.numero_habitacion + 1
            else:
                numero_habitacion = 200
    elif estado == 3:
        estado_str = "Terapia intensiva"
        if not pacientes:
            numero_habitacion = 300
        else:
            ultimo_paciente = pacientes[-1]
            if ultimo_paciente.estado == "Terapia intensiva":
                numero_habitacion = ultimo_paciente.numero_habitacion + 1
            else:
                numero_habitacion = 300
    else:
        print("Por favor confirme los datos ingresados:")
        print(f"DNI: {dni}\nNombre: {nombre} {apellido}\nObra Social: {obra_social.nombre} - {obra_social.numero_asociado} - {obra_social.tipo_plan}\nHabitación: {numero_habitacion}\nEstado: {estado_str}")
        confirmacion = input("¿Son correctos estos datos? (s/n): ")
        if confirmacion.lower()!= '':
            print("Datos no confirmados, volviendo al menú principal.")
            return None

    paciente = Paciente(dni, obra_social, nombre, apellido, numero_habitacion, estado_str)
    confirmacion_final = input("¿Confirmar guardar datos del paciente? (s/n): ")
    if confirmacion_final.lower() == '':
        return paciente
    else:
        print("Operación cancelada.")
        return None

def guardar_datos(pacientes):
    with open('pacientes.txt', 'w') as archivo:
        for paciente in pacientes:
            archivo.write(f"{paciente.dni};{paciente.obra_social.nombre};{paciente.obra_social.numero_asociado};{paciente.obra_social.tipo_plan};{paciente.nombre};{paciente.apellido};{paciente.numero_habitacion};{paciente.estado}\n")

def cargar_datos():
    pacientes = []
    with open('pacientes.txt', 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(';')
            obra_social = ObraSocial(datos[0], datos[1], datos[2])
            paciente = Paciente(datos[3], obra_social, datos[4], datos[5], datos[6], datos[7])
            pacientes.append(paciente)
    return pacientes
    
def dni_existente(dni, pacientes):
    # Verificar si el DNI ya existe
    for paciente in pacientes:
        if paciente.dni == dni:
            return True
    return False
    
ESTADOS_PERMITIDOS = [1, 2, 3, 4]
ESTADOS_MAPEADOS = {
    1: "Habitación común",
    2: "Terapia intermedia",
    3: "Terapia intensiva",
    4: "Dado de alta"
}

def modificar_estado(paciente):
    nuevo_estado = int(input("Ingrese nuevo estado del paciente:\n1: Habitación común\n2: Terapia intermedia\n3: Terapia intensiva\n4: Dado de alta: "))
    if nuevo_estado not in ESTADOS_PERMITIDOS:
        print("Error: El estado debe ser uno de los valores permitidos.")
        return
    nuevo_estado_str = ESTADOS_MAPEADOS[nuevo_estado]
    paciente.cambiar_estado(nuevo_estado_str)


def consultar_paciente(pacientes):
    dni_consultar = input("Ingrese DNI del paciente a consultar: ")
    for paciente in pacientes:
        if paciente.dni == dni_consultar:
            print(paciente.ver_datos())
            break
    else:
        print("No se encontró paciente con el DNI ingresado")


def main():
    pacientes = cargar_datos()

    while True:
        print("#" * 20)
        print("# Menu")
        print("# 1. Cargar nuevo paciente")
        print("# 2. Modificar paciente existente")
        print("# 3. Consultar paciente")
        print("# 4. Salir")
        print("#" * 20)

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            dni = input("Ingrese DNI del paciente: ")  # Definir DNI antes de verificar si existe
            if dni_existente(dni, pacientes):
                print("Un paciente con ese DNI ya existe.")
            else:
                paciente = cargar_datos_paciente(pacientes,dni)
                if paciente:
                    pacientes.append(paciente)
                    guardar_datos(pacientes)
                    print("Paciente cargado con éxito!")
                    print("#" * 20)
                    print(paciente.ver_datos())
        elif opcion == "2":
            if len(pacientes) == 0:
                print("No hay pacientes cargados. Por favor, cargue un paciente antes de modificar")
            else:
                dni_modificar = input("Ingrese DNI del paciente a modificar: ")
                for paciente in pacientes:
                    if paciente.dni == dni_modificar:
                        modificar_estado(paciente)
                        print("Estado del paciente modificado con éxito!")
                        print(paciente.ver_datos())
                        break
                else:
                    print("No se encontró paciente con el DNI ingresado")
        elif opcion == "3":
            if len(pacientes) == 0:
                print("No hay pacientes cargados. Por favor, cargue un paciente antes de consultar")
            else:
                consultar_paciente(pacientes)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida")

        print()  # Salto de línea para separar las diferentes acciones


if __name__ == "__main__":
    main()