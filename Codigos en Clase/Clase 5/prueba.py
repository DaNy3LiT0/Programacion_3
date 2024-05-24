class Transporte:
    ruedas= 4 #Atributo de clase
    
#Debemos crear un metodo que se encargue de proporcionar esas propiedades de cada objeto     
    #Metodo constructor
    #parametro obligatorio, el primero: self (es el nombre del objeto que estoy construyendo)
    def constructor(self, medio, empresa, v_max,color="sin color"):
        #Atributos de instancia, varian de un objeto a otro
        self.medio = medio #(ej. avion.medio = aire)
        self.empresa = empresa
        self.v_max = v_max
        self.color = color


#Debemos definir atributos que sean propios para cada instancia del objeto
#Debemos crear un Metodo iniciador o constructor para definir atributos propios de ese objeto

print("\033[H\033[J")          # Limpiamos la pantalla

avion = Transporte()
avion.constructor("aire", "A. Arg.", 1400, "azul y blanco")
tren = Transporte()
tren.constructor("tierra", "F. Sarmiento", 60, "celeste")
print(avion)