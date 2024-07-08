'''Juego de rol: Crea una jerarquía de clases para modelar un juego de rol con una clase base "Personaje" que contenga atributos comunes como puntos de vida, puntos de ataque y puntos de defensa. Luego, crea clases derivadas como "Guerrero", "Mago" y "Arquero" que hereden de la clase base y proporcionen implementaciones específicas para habilidades y características únicas de cada tipo de personaje.'''

class Personaje:
    def __init__(self, vida, ataque, defensa):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

class Guerrero(Personaje):
    def __init__(self, vida, ataque, defensa, fuerza):
        super().__init__(vida, ataque, defensa)
        self.fuerza = fuerza

    def __str__(self):
        return f"Soy el Guerrero con vida: {self.vida}, ataque: {self.ataque}, defensa: {self.defensa}, velocidad: {self.fuerza}"


class Mago(Personaje):
    def __init__(self, vida, ataque, defensa, magia):
        super().__init__(vida, ataque, defensa)
        self.magia = magia

    def __str__(self):
        return f"Soy el Mago con vida: {self.vida}, ataque: {self.ataque}, defensa: {self.defensa}, velocidad: {self.magia}"

class Arquero(Personaje):
    def __init__(self, vida, ataque, defensa, velocidad):
        super().__init__(vida, ataque, defensa)
        self.velocidad = velocidad

    def __str__(self):
        return f"Soy el Arquero con vida: {self.vida}, ataque: {self.ataque}, defensa: {self.defensa}, velocidad: {self.velocidad}"

guerrero1 = Guerrero(500, 250, 150, 1500)
mago1 = Mago(300, 200, 100, 1000)
arquero1 = Arquero(400, 220, 120, 1200)

print(f"{guerrero1}\n{mago1}\n{arquero1}")