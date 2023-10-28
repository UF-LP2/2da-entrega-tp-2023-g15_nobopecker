from enums import eColor
from enums import eEnfermedad
class cEnfermedad:
    def __init__(self, color: eColor, duracion: int, enfermedad: eEnfermedad, prioridad: int):
        self.color=color
        self.duracion=duracion
        self.enfermedad=enfermedad
        self.prioridad=prioridad
