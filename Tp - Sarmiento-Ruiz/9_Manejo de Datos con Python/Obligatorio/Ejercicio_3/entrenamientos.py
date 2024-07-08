import conectarDB
import datetime

conn, cursor = conectarDB.connect_db()
conectarDB.create_tables(conn, cursor)

def calcular_edad(fecha_nacimiento):
    hoy = datetime.date.today()
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad

def insertar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    email = input("Ingrese el email del usuario: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del usuario (YYYY-MM-DD): ")
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    fecha_nacimiento_str = fecha_nacimiento.strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO usuarios (nombre, apellido, email, fecha_nacimiento) VALUES (?, ?, ?, ?)", (nombre, apellido, email, fecha_nacimiento_str))
    conn.commit()
    print("Usuario insertado correctamente!")
    print(f"La edad del usuario es {calcular_edad(fecha_nacimiento)} años")

def insertar_entrenamiento():
    fecha = input("Ingrese la fecha del entrenamiento (YYYY-MM-DD): ")
    tipo_ejercicio = input("Ingrese el tipo de ejercicio: ")
    duración = int(input("Ingrese la duración del entrenamiento (en minutos): "))
    rendimiento = float(input("Ingrese el rendimiento del entrenamiento (0-100): "))

    # Mostrar lista de usuarios registrados
    cursor.execute("SELECT id, nombre, apellido FROM usuarios")
    usuarios = cursor.fetchall()
    print("Seleccione un usuario:")
    for i, usuario in enumerate(usuarios):
        print(f"{i+1}. {usuario[1]} {usuario[2]} (ID: {usuario[0]})")
    opción = int(input("Ingrese el número del usuario: ")) - 1
    id_usuario = usuarios[opción][0]

    # Insertar entrenamiento
    cursor.execute("INSERT INTO entrenamientos (fecha, tipo_ejercicio, duración, rendimiento) VALUES (?,?,?,?)", (fecha, tipo_ejercicio, duración, rendimiento))
    conn.commit()
    id_entrenamiento = cursor.lastrowid

    # Insertar relación entre entrenamiento y usuario
    cursor.execute("INSERT INTO entrenamientos_usuarios (id_entrenamiento, id_usuario) VALUES (?,?)", (id_entrenamiento, id_usuario))
    conn.commit()

    print("Entrenamiento insertado correctamente!")

def mostrar_entrenamientos_usuario():
    cursor.execute("SELECT id, nombre, apellido FROM usuarios")
    usuarios = cursor.fetchall()
    print("Seleccione un usuario:")
    for i, usuario in enumerate(usuarios):
        print(f"{i+1}. {usuario[1]} {usuario[2]} (ID: {usuario[0]})")
    opción = int(input("Ingrese el número del usuario: ")) - 1
    id_usuario = usuarios[opción][0]
    cursor.execute("""
        SELECT e.fecha, e.tipo_ejercicio, e.duración, e.rendimiento
        FROM entrenamientos e
        INNER JOIN entrenamientos_usuarios eu ON e.id = eu.id_entrenamiento
        WHERE eu.id_usuario = ?
    """, (id_usuario,))
    entrenamientos = cursor.fetchall()
    print("Entrenamientos realizados:")
    print("Fecha|Tipo de ejercicio|Duración (min)|Rendimiento (%)")
    for entrenamiento in entrenamientos:
        print(f"{entrenamiento[0]}|{entrenamiento[1]}|{entrenamiento[2]}|{entrenamiento[3]}%")

def menu():
    while True:
        print("Menú:")
        print("1. Insertar usuario")
        print("2. Insertar entrenamiento")
        print("3. Mostrar entrenamientos de un usuario")
        print("4. Salir")
        opción = input("Ingrese una opción: ")
        if opción == "1":
            insertar_usuario()
        elif opción == "2":
            insertar_entrenamiento()
        elif opción == "3":
            mostrar_entrenamientos_usuario()
        elif opción == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    menu()
    conn.close()