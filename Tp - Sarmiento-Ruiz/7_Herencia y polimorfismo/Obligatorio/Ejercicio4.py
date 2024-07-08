"""Sistema de cálculo de impuestos: Crea una jerarquía de clases para representar diferentes tipos de contribuyentes, como "PersonaFísica", "PersonaJurídica" y "PersonaExtranjera". Cada clase debe tener un método llamado "calcular_impuesto()" que calcule el impuesto correspondiente para ese tipo de contribuyente. Luego, crea una función llamada "calcular_impuesto_total()" que tome una lista de contribuyentes y calcule el impuesto total utilizando el polimorfismo."""

class Contribuyente:
    def __init__(self, nombre, ingresos_anuales):
        self.nombre = nombre
        self.ingresos_anuales = ingresos_anuales

    def calcular_impuesto(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def __str__(self):
        return f"Nombre: {self.nombre}, Ingresos Anuales: ${self.ingresos_anuales:.2f}"

class PersonaFísica(Contribuyente):
    def __init__(self, nombre, ingresos_anuales):
        super().__init__(nombre, ingresos_anuales)

    def calcular_impuesto(self):
        impuesto = self.ingresos_anuales * 0.15
        return impuesto

class PersonaJurídica(Contribuyente):
    def __init__(self, nombre, ingresos_anuales):
        super().__init__(nombre, ingresos_anuales)

    def calcular_impuesto(self):
        impuesto = self.ingresos_anuales * 0.20
        return impuesto

class PersonaExtranjera(Contribuyente):
    def __init__(self, nombre, ingresos_anuales):
        super().__init__(nombre, ingresos_anuales)

    def calcular_impuesto(self):
        impuesto = self.ingresos_anuales * 0.25
        return impuesto

def Calcular_Impuesto_Total(contribuyentes):
    total_impuesto = 0
    for contribuyente in contribuyentes:
        total_impuesto += contribuyente.calcular_impuesto()
    return total_impuesto

persona_física = PersonaFísica("Juan Pérez", 50000)
persona_jurídica = PersonaJurídica("Sancor", 200000)
persona_extranjera = PersonaExtranjera("Miley Cyrus", 75000)

contribuyentes = [persona_física, persona_jurídica, persona_extranjera]

for contribuyente in contribuyentes:
    print(f"{contribuyente} - Impuesto: ${contribuyente.calcular_impuesto():.2f}")

total_impuesto = Calcular_Impuesto_Total(contribuyentes)
print(f"Impuesto Total: ${total_impuesto:.2f}")