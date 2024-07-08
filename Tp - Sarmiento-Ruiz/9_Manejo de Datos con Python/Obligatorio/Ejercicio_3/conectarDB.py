import sqlite3
import os

def connect_db():
    db_path = os.path.join(os.path.dirname(__file__), 'entrenamientos.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return conn, cursor

def create_tables(conn, cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            apellido TEXT,
            email TEXT,
            fecha_nacimiento DATE
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entrenamientos (
            id INTEGER PRIMARY KEY,
            fecha DATE,
            tipo_ejercicio TEXT,
            duración INTEGER,
            rendimiento REAL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entrenamientos_usuarios (
            id_entrenamiento INTEGER,
            id_usuario INTEGER,
            PRIMARY KEY (id_entrenamiento, id_usuario),
            FOREIGN KEY (id_entrenamiento) REFERENCES entrenamientos (id),
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
        );
    """)
    conn.commit()