class Cromos:
    def __init__(self, nombre, marca, edicion, copias, estado):
        self.nombre = nombre
        self.edicion = edicion
        self.copias = copias
        self.estado = estado
        self.marca = marca

    def __str__(self):
        return f'{self.nombre} - {self.marca} | {self.edicion} | {self.copias} | {self.estado}'

    def rarezas(self):
        rareza = ''
        if self.copias > 10000000:
            rareza = 'común'
        elif self.copias > 1000000:
            rareza = 'poco común'
        elif self.copias > 100000:
            rareza = 'raro'
        elif self.copias > 10000:
            rareza = 'super raro'
        elif self.copias > 10:
            rareza = 'ultra raro'
        elif self.copias <= 10:
            rareza = 'único'
        return rareza

    def precio(self):
        if self.copias <= 10:
            precio = 4**self.estado / self.copias
        else:
            precio = 3 ** self.estado / self.copias
        return precio
# Cambiar el precio y hacer que dependa también de demanda o del estado.

