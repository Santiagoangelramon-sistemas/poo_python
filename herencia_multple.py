class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        return f"El {self.marca} {self.modelo} está en movimiento."

class Electrico:
    def __init__(self, autonomia):
        self.autonomia = autonomia

    def cargar(self):
        return "El vehículo eléctrico se está cargando."

class CocheElectrico(Coche, Electrico):
    def __init__(self, marca, modelo, autonomia):
        Coche.__init__(self, marca, modelo)
        Electrico.__init__(self, autonomia)

    def detalles(self):
        return f"Detalles: {self.marca} {self.modelo}, Autonomía: {self.autonomia} km"

# Crear una instancia de la clase CocheElectrico
mi_coche_electrico = CocheElectrico("Tesla", "Model 3", 500)

# Acceder a métodos de ambas clases padre
print(mi_coche_electrico.conducir())
print(mi_coche_electrico.cargar())

# Acceder al método de la clase hija
print(mi_coche_electrico.detalles())