class Figura:
    def __init__(self, nombre, marca, modelo, copias, alto, ancho, largo, estado):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.copias = copias
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        self.estado = estado

    def tam(self):
        return self.alto * self.largo * self.ancho

    def rarezas(self):
        rareza = ''
        if self.copias > 1000000:
            rareza = 'común'
        elif self.copias > 100000:
            rareza = 'poco común'
        elif self.copias > 10000:
            rareza = 'raro'
        elif self.copias > 1000:
            rareza = 'super raro'
        elif self.copias > 100:
            rareza = 'ultra raro'
        elif self.copias == 1:
            rareza = 'único'
        return rareza
