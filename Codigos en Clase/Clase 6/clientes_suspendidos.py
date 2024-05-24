class Cliente:
    suspendidos=[]
    
    def __init__(self,codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        
    def imprimir(self):    
        print(f"codigo :{self.codigo}")
        print(f"nombre :{self.nombre}")
        self.esta_suspendido()
    
    def suspender(self):
        Cliente.suspendidos.append(self.codigo)
    
    def  esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Está suspendido")
        else:
            print("No está suspendido")
        print("-"*20)


#Programa principal

print("\033[H\033[J")          # Limpiamos la pantalla
c1 = Cliente(1,"Jose")        
c2 = Cliente(2, "Fabian")
c3 = Cliente(3,"Mariano")

c2.suspender()
c3.suspender()

c2.imprimir()
c2.imprimir()
c2.imprimir()

                        