class Pelicula:
    
    def __init__(self,titulo,duración,lanzamiento):
        self.titulo = titulo
        self.duración = duración
        self.lanzamiento = lanzamiento
        print(f'Se ha creado la película: {self.titulo}')
    
    def __str__(self):
        return f'{self.titulo} {self.lanzamiento}'


class Catalogo:
    peliculas = [] # Lista de objetos de la clase Película
    # Constructor de clase
    def __init__(self, peliculas=[]):
        Catalogo.peliculas = peliculas

    def agregar(self, p): # p es un objeto Pelicula
        Catalogo.peliculas.append(p)

    def mostrar(self):
        for p in Catalogo.peliculas:
            print(p) # Print toma por defecto str(p)

#Programa principal

print("\033[H\033[J")          # Limpiamos la pantalla

# Instanciamos una película
#peli1 = Pelicula("El Padrino", 175, 1972)
#c = Catalogo([peli1])
#c.mostrar()
#c.agregar(Pelicula("El padrino: Parte 2", 202,1974))
#c.mostrar()

#----------------------------------------------#
#Podemos agregar de a aun las peliculas
#peli1 = Pelicula("Batman I", 175, 2000)
#peli2 = Pelicula("Batman II", 170, 2002)
#peli3 = Pelicula("Batman III", 165, 2005)
#peli4 = Pelicula("Batman IV", 160, 2010)
#c = Catalogo()
#c.agregar(peli1)
#c.agregar(peli2)
#c.agregar(peli3)
#c.mostrar()

#---------------------------------------------------#


#peli1 = Pelicula("Batman I", 175, 2000)
#peli2 = Pelicula("Batman II", 170, 2002)
#peli3 = Pelicula("Batman III", 165, 2005)
#peli4 = Pelicula("Batman IV", 160, 2010)

#c = Catalogo()
#c = Catalogo([peli1,peli2,peli3,peli4])
#c.mostrar()

#---------------------------------------------------#

#El problema es que puedo acceder a estos atributos libremente y cambiarlos

peli1 = Pelicula("Batman I", 175, 2000)
peli2 = Pelicula("Batman II", 170, 2002)
c = Catalogo()
c = Catalogo([peli1,peli2])

print(peli1.titulo)
peli2.titulo="Los bañeros más locos del mundo"
c.mostrar()

#Diapositivas, encapsulacion

