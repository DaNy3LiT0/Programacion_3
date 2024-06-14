"""
Desarrolla un sistema de gestión de proyectos con clases como "Proyecto", "Tarea" y  "Miembro  del  equipo".  
Un  objeto  "Proyecto"  puede  tener  una  lista  de  objetos "Tarea",  y  cada  "Tarea"  puede  asignarse  
a  uno  o  varios  objetos  "Miembro  del equipo".  
Los  miembros  del  equipo  pueden  acceder  a  las  tareas  asignadas  y actualizar  su  estado  (realizado  o  pendientes).  
Puedes  implementar  métodos  para agregar tareas al proyecto, asignar miembros del equipo y realizar un seguimiento 
del progreso del proyecto (listado de tareas realizadas o pendiente).
"""

class MiembroDelEquipo:
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni
        self.__clave_entrada = None
        self.__tareas_asignadas = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def dni(self):
        return self.__dni

    @property
    def clave_entrada(self):
        return self.__clave_entrada

    @clave_entrada.setter
    def clave_entrada(self, valor):
        self.__clave_entrada = valor

    @property
    def tareas_asignadas(self):
        return self.__tareas_asignadas

    def asignar_tarea(self, tarea):
        self.__tareas_asignadas.append(tarea)

    def obtener_tareas_pendientes(self):
        return [tarea.descripcion for tarea in self.__tareas_asignadas if not tarea.completada]

    def obtener_tareas_completadas(self):
        return [tarea.descripcion for tarea in self.__tareas_asignadas if tarea.completada]

    def validar_clave_entrada(self, clave):
        return self.__clave_entrada == clave

class Tarea:
    def __init__(self, descripcion):
        self.__descripcion = descripcion
        self.__completada = False
        self.__miembros_asignados = []

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def completada(self):
        return self.__completada

    @completada.setter
    def completada(self, valor):
        self.__completada = valor

    @property
    def miembros_asignados(self):
        return self.__miembros_asignados

    def asignar_a_miembro(self, miembro):
        self.__miembros_asignados.append(miembro)
        miembro.asignar_tarea(self)

    def marcar_como_completada(self):
        self.__completada = True


class Proyecto:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__tareas = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tareas(self):
        return self.__tareas

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.__tareas.append(tarea)
        return tarea

    def obtener_tareas_pendientes(self):
        return [tarea.descripcion for tarea in self.__tareas if not tarea.completada]

    def obtener_tareas_completadas(self):
        return [tarea.descripcion for tarea in self.__tareas if tarea.completada]
    
    def generar_informe(self):
        print(f"Proyecto: {self.nombre}")
        print("Miembros:")
        for miembro in self.miembros:
            print(f"  - {miembro.nombre} ({miembro.dni})")
            for tarea in miembro.tareas_asignadas:
                print(f"    - {tarea.descripcion} ({'Completada' if tarea.completada else 'Pendiente'})")


"""def crear_proyecto(miembros):
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    proyecto = Proyecto(nombre_proyecto)
    num_miembros = int(input("Ingrese el número de miembros del proyecto: "))
    for i in range(num_miembros):
        nombre_miembro = input(f"Ingrese el nombre del miembro {i+1}: ")
        dni_miembro = input(f"Ingrese el DNI del miembro {i+1}: ")
        miembro = MiembroDelEquipo(nombre_miembro, dni_miembro)
        miembros.append(miembro)
        tarea_descripcion = input(f"Ingrese la tarea para {nombre_miembro}: ")
        tarea = proyecto.agregar_tarea(tarea_descripcion)
        miembro.asignar_tarea(tarea)
    return proyecto"""

def crear_proyecto(miembros):
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    proyecto = Proyecto(nombre_proyecto)

    num_miembros = int(input("Ingrese el número de miembros del proyecto: "))
    for i in range(num_miembros):
        nombre_miembro = input(f"Ingrese el nombre del miembro {i+1}: ")
        dni_miembro = input(f"Ingrese el DNI del miembro {i+1}: ")
        miembro = MiembroDelEquipo(nombre_miembro, dni_miembro)
        miembros.append(miembro)

        tarea_descripcion = input(f"Ingrese la tarea para {nombre_miembro}: ")
        tarea = proyecto.agregar_tarea(tarea_descripcion)
        miembro.asignar_tarea(tarea)

    return proyecto

def buscar_proyecto(proyectos):
    if not proyectos:
        print("No hay proyectos cargados.")
        return None
    print("Proyectos creados:")
    for i, proyecto in enumerate(proyectos):
        print(f"{i+1}. {proyecto.nombre}")
    num_proyecto = int(input("Ingrese el número del proyecto: ")) - 1
    return proyectos[num_proyecto]

def asignar_nuevo_miembro(proyectos, miembros):
    print("Proyectos creados:")
    for i, proyecto in enumerate(proyectos):
        print(f"{i+1}. {proyecto.nombre}")
    num_proyecto = int(input("Ingrese el número del proyecto: ")) - 1
    proyecto_seleccionado = proyectos[num_proyecto]
    
    nombre_miembro = input("Ingrese el nombre del nuevo miembro: ")
    dni_miembro = input("Ingrese el DNI del nuevo miembro: ")
    miembro = MiembroDelEquipo(nombre_miembro, dni_miembro)
    miembros.append(miembro)
    tarea_descripcion = input(f"Ingrese la tarea para {nombre_miembro}: ")
    tarea = proyecto_seleccionado.agregar_tarea(tarea_descripcion)
    miembro.asignar_tarea(tarea)

def agregar_nueva_tarea(miembros, proyectos):
    dni_miembro = input("Ingrese el DNI del miembro: ")
    miembro_encontrado = None
    for miembro in miembros:
        if miembro.dni == dni_miembro:
            miembro_encontrado = miembro
            break
    if miembro_encontrado:
        print("Proyectos disponibles:")
        for i, proyecto in enumerate(proyectos):
            print(f"{i+1}. {proyecto.nombre}")
        num_proyecto = int(input("Ingrese el número del proyecto donde asignar la tarea: ")) - 1
        proyecto_seleccionado = proyectos[num_proyecto]
        tarea_descripcion = input(f"Ingrese la tarea para {miembro_encontrado.nombre}: ")
        tarea = proyecto_seleccionado.agregar_tarea(tarea_descripcion)
        miembro_encontrado.asignar_tarea(tarea)
    else:
        print("Miembro no encontrado")

def modificar_estado(miembros):
    nombre_miembro = input("Ingrese el nombre del miembro: ")
    for miembro in miembros:
        if miembro.nombre == nombre_miembro:
            print("Tareas asignadas:")
            for i, tarea in enumerate(miembro.tareas_asignadas):
                print(f"{i+1}. {tarea.descripcion} - {'Completada' if tarea.completada else 'Pendiente'}")
            num_tarea = int(input("Ingrese el número de la tarea a modificar: ")) - 1
            tarea = miembro.tareas_asignadas[num_tarea]
            estado = input("Ingrese el nuevo estado (Pendiente/Completada): ")
            if estado.lower() == "completada":
                tarea.completada = True
            else:
                tarea.completada = False
            return
    print("Miembro no encontrado")
    
def generar_informe_proyectos(proyectos):
    if not proyectos:
        print("No hay proyectos cargados.")
        return
    for proyecto in proyectos:
        proyecto.generar_informe()
        print()


### Programa Principal ###

def main():
    proyectos = []
    miembros = []

    while True:
        print("######### Menu de Inicio al Sistema #########")
        print("#                                           #")
        print("#  1. Crear Proyecto                        #")
        print("#  2. Buscar Proyecto                       #")
        print("#  3. Asignar Nuevo Miembro                 #")
        print("#  4. Agregar Nueva Tarea                   #")
        print("#  5. Modificar Estado                      #")
        print("#  6. Generar Informe de Proyectos          #")
        print("#  7. Salir                                 #")
        print("#                                           #")
        print("######### Menu de Inicio al Sistema #########")
        print()
        opcion = input("Ingrese una opción: ")
        print()
        print('#'*45)
        print()

        if opcion == "1":
            proyecto = crear_proyecto(miembros)
            proyectos.append(proyecto)
            print()
            print('#'*45)

        elif opcion == "2":
            proyecto = buscar_proyecto(proyectos)
            if proyecto is None:
                print()
                print('#'*45)
                continue
            print("Proyecto encontrado")
            print()
            print('#'*45)

        elif opcion == "3":
            asignar_nuevo_miembro(proyectos, miembros)
            print()
            print('#'*45)

        elif opcion == "4":
            agregar_nueva_tarea(miembros, proyectos)
            print()
            print('#'*45)

        elif opcion == "5":
            modificar_estado(miembros)
            print()
            print('#'*45)

        elif opcion == "6":
            generar_informe_proyectos(proyectos)
            print()
            print('#'*45)

        elif opcion == "7":
            print("Hasta luego!")
            print()
            break

        else:
            print("Opción no válida")
            print()
            print('#'*45)


if __name__ == "__main__":
    main()