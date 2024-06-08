"""
Modelar un sanatorio donde los pacientes tienen los siguientes atributos: dni, obra 
social, nombre, apellido, número habitación, estado (habitación común, terapia 
intermedia, terapia intensiva). Implementar métodos que permitan ver los datos de 
los pacientes, ver su estado y cambiar de estado
"""

class ObraSocial:
    def __init__(self, nombre, numero_asociado, tipo_plan):
        self.nombre = nombre
        self.numero_asociado = numero_asociado
        self.tipo_plan = tipo_plan

    def __str__(self):
        return f"{self.nombre} - N° {self.numero_asociado} - {self.tipo_plan}"


class Paciente:
    def __init__(self, dni, obra_social, nombre, apellido, numero_habitacion, estado):
        self.dni = dni
        self.obra_social = obra_social
        self.nombre = nombre
        self.apellido = apellido
        self.numero_habitacion = numero_habitacion
        self.estado = estado

    def ver_datos(self):
        return f"DNI: {self.dni}, Obra Social: {self.obra_social}, Nombre: {self.nombre} {self.apellido}, Habitación: {self.numero_habitacion}, Estado: {self.estado}"

    def ver_estado(self):
        return self.estado

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado


### Programa Principal ###

obra_social = ObraSocial("OSDE", "123456", "Plan Premium")
paciente = Paciente("12345678", obra_social, "Agustin", "Ruiz", 101, "Habitación común")
print(paciente.ver_datos())
print(paciente.ver_estado())
paciente.cambiar_estado("Terapia intermedia")
print(paciente.ver_datos())