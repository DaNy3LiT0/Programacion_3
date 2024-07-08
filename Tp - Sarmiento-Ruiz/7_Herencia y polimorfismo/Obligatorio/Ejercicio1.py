'''Sistema de reservas de vuelos: Crea una jerarquía de clases para modelar un sistema de reservas de vuelos.
Existe clase base "Vuelo" que contiene información común como número de vuelo, origen y destino. Luego, crea clases derivadas como
"VueloNacional" y "VueloInternacional" que hereden de la clase base y proporcionen implementaciones específicas,
como métodos para verificar requisitos de pasaporte y calcular el precio del vuelo.'''


class Vuelo():

    def __init__(self, num_vuelo, origen, destino):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino

class VueloNacional(Vuelo):
    def __init__(self, num_vuelo, origen, destino):
        super().__init__(num_vuelo, origen, destino)

    def precioNac(self, distancia, clase_vuelo):
        cost_combustible = 1000
        if clase_vuelo == 'económico':
            return distancia * cost_combustible * 0.5
        elif clase_vuelo == 'primera_clase':
            return distancia * cost_combustible * 3.5
        else:
            return "Clase de vuelo no disponible"

class VueloInternacional(Vuelo):
    def __init__(self, num_vuelo, origen, destino):
        self.pasaporte = False
        super().__init__(num_vuelo, origen, destino)

    def precio_internacional(self, distancia, clase_vuelo):
        cost_combustible = 1000
        if clase_vuelo == 'económico':
            return distancia * cost_combustible * 1.5
        elif clase_vuelo == 'primera_clase':
            return distancia * cost_combustible * 3.5
        else:
            return "Clase de vuelo no disponible"

    def verificar_pasaporte(self):
        if self.pasaporte:
            return 'El pasaporte es valido'
        else:
            return 'El pasaporte no es valido'

    def __str__(self):
        return f"Vuelo {self.num_vuelo} con salida desde {self.origen} a {self.destino}"

vi1 = VueloInternacional('V0001', 'Santiago del Estero', 'Buenos Aires')
vi1.pasaporte = True

precio = vi1.precio_internacional(1500, 'económico')
pasaporte = vi1.verificar_pasaporte()

print(f"{vi1}. El precio del vuelo es $ {precio} y {pasaporte}")