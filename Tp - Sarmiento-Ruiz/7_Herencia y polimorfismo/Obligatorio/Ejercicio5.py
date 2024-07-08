"""Sistema de lectura de archivos: Crea una jerarquía de clases para representar diferentes tipos de archivos, como "ArchivoTexto", "ArchivoPDF" y "ArchivoImagen". Cada clase debe tener un método llamado "leer()" que muestre el contenido del archivo en la consola. Luego, crea una función llamada "leer_archivos()" que tome una lista de archivos y los lea uno por uno utilizando el polimorfismo."""

import os
import PyPDF2 # type: ignore
from PIL import Image # type: ignore


class Archivo:
    def __init__(self, nombre_archivo):
        if not os.path.exists(nombre_archivo):
            raise FileNotFoundError(f"El archivo {nombre_archivo} no existe")
        self.nombre_archivo = nombre_archivo

    def leer(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def __str__(self):
        return f"Archivo: {self.nombre_archivo}"

class ArchivoTexto(Archivo):
    def leer(self):
        with open(self.nombre_archivo, "r") as archivo:
            print(archivo.read())

class ArchivoPDF(Archivo):
    def leer(self):
        with open(self.nombre_archivo, "rb") as archivo:
            pdf = PyPDF2.PdfFileReader(archivo)
            for page in pdf.pages:
                print(page.extractText())

class ArchivoImagen(Archivo):
    def leer(self):
        from matplotlib.pyplot import imshow, show # type: ignore
        img = Image.open(self.nombre_archivo)
        imshow(img)
        show()

def leer_archivos(lista_archivos):
    for archivo in lista_archivos:
        if not isinstance(archivo, Archivo):
            raise TypeError(f"El elemento {archivo} no es un archivo")
        archivo.leer()


archivo1 = ArchivoTexto("MI SPRINT RETROSPECTIVE Santillan Sebastian.txt")
archivo2 = ArchivoPDF("documento.pdf")
archivo3 = ArchivoImagen("imagen.jpg")

lista_archivos = [archivo1, archivo2, archivo3]
leer_archivos(lista_archivos)