""" 
Desarrollar un reloj de horas, minutos y segundos utilizando el módulo datetime con la hora 
actual. Hazlo en un script llamado reloj.py y ejecútalo en la terminal
"""

import datetime
import time

def obtener_hora_actual():
    ahora = datetime.datetime.now()
    hora = ahora.hour
    minutos = ahora.minute
    segundos = ahora.second
    return hora, minutos, segundos

def formatear_hora(hora, minutos, segundos):
    return f"{hora:02d}:{minutos:02d}:{segundos:02d}"


ahora = datetime.datetime.now()
hora_formateada = ahora.strftime("%H:%M:%S")
print(f"Hora actual: {hora_formateada}")

