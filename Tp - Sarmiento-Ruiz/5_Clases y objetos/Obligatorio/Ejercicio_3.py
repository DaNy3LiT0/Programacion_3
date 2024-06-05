"""
Realizar una clase que administre una agenda. Se debe almacenar para cada 
contacto el nombre, el teléfono y el email. Además, deberá mostrar un menú con las
siguientes opciones
    - Añadir contacto
    - Lista de contacto
    - Buscar contacto
    - Editar contacto
    - Cerrar agenda
"""
class Agenda:
    def __init__(self):
        self.contacto = {}

    def agregar(self):
        apellido = input("Ingresa el apellido del contacto: ").capitalize()
        nombre = input("Ingresa el nombre del contacto: ").capitalize()
        telefono = input("Ingresa el teléfono del contacto: ")
        email = input("Ingresa el email del contacto: ")
        contacto_AyN = (apellido, nombre)
        contacto_Datos = {"telefono": telefono, "email": email}
        self.contacto[contacto_AyN] = contacto_Datos
        print("Contacto agregado exitosamente!")

    def listar(self):
        if not self.contacto:
            print("No hay contacto en la agenda.")
        else:
            print("Contactos en la agenda:")
            for i, (apellido, nombre) in enumerate(self.contacto.keys(), 1):
                contacto_Datos = self.contacto[(apellido, nombre)]
                print(f"{i}. {apellido} {nombre} - {contacto_Datos['telefono']} - {contacto_Datos['email']}")

    def buscar(self):
        apellido = input("Ingresa el apellido del contacto a buscar: ").capitalize()
        nombre = input("Ingresa el nombre del contacto a buscar: ").capitalize()
        contacto_AyN = (apellido, nombre)
        if contacto_AyN in self.contacto:
            contacto_Datos = self.contacto[contacto_AyN]
            print(f"Contacto encontrado: {apellido} {nombre} - {contacto_Datos['telefono']} - {contacto_Datos['email']}")
        else:
            print("Contacto no encontrado.")

    def editar(self):
        apellido = input("Ingresa el apellido del contacto a editar: ").capitalize()
        nombre = input("Ingresa el nombre del contacto a editar: ").capitalize()
        contacto_AyN = (apellido, nombre)
        if contacto_AyN in self.contacto:
            contacto_Datos = self.contacto[contacto_AyN]
            contacto_Datos["telefono"] = input("Ingresa el nuevo teléfono: ")
            contacto_Datos["email"] = input("Ingresa el nuevo email: ")
            print("Contacto editado exitosamente!")
        else:
            print("Contacto no encontrado.")

    def run(self):
        while True:
            print("Agenda")
            print("1. Añadir contacto")
            print("2. Lista de contacto")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            option = input("Ingresa una opción: ")
            if option == "1":
                self.agregar()
            elif option == "2":
                self.listar()
            elif option == "3":
                self.buscar()
            elif option == "4":
                self.editar()
            elif option == "5":
                print("Agenda cerrada.")
                break
            else:
                print("Opción invalida. Intenta de nuevo.")

agenda = Agenda()
agenda.run()

