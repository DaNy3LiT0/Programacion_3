print("\033[H\033[J")          # Limpiamos la pantalla


class Persona:
    piernas = 2
    
    
    #Constructor
    def inicializar(self, dni,nombre, apellido):
        self.dni = dni
        self.nombre= nombre
        self.apellido = apellido
        
    def imprimir(self):
        print(f"Nombre : {self.apellido}, {self.nombre} con DNI: {self.dni}")
    
    def caminar():
        return
    def hablar():
        return
    def comer():
        return

mari = Persona()
mari.inicializar("20.564.674", "Maria de los Angeles","Pérez")
mari.imprimir()

