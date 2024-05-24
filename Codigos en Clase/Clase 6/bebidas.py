class Bebidas:
    def __init__(self):
        self.__bebida = 'Naranja'

    @property
    def favorita(self):
        return f"La bebida preferida es: {self.__bebida}"

    @favorita.setter
    def favorita(self, bebida):
        self.__bebida = bebida


# Programa principal
print("\033[H\033[J")          # Limpiamos la pantalla


obj1 = Bebidas()
#No puedo acceder al atributo de instancia
print(obj1.__bebida)

#Como cambio naranja por pomelo
obj1.favorita = "Pomelo"
print(obj1.favorita) # Pomelo

# Los getters y los setters nos permiten realizar un control previo para leeer o moficar por afuera
#de tal forma  que su uso no sea accidental