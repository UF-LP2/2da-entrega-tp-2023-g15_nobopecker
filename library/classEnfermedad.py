from enums import eColor
from enums import eEnfermedad
class cEnfermedad:
    def __init__(self, color: eColor, duracion: int, enfermedad: eEnfermedad, prioridad: int, tiempo_restante:int):
        self.color=color
        self.duracion=duracion
        self.enfermedad=enfermedad
        self.prioridad=prioridad
        self.tiempo_restante=tiempo_restante
