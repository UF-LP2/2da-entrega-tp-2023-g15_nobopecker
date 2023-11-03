from classEnfermero import cEnfermero
from src.classPaciente import cPaciente
from classConsultorio import cConsultorio
class cHospital:

    def __init__(self, consultorios: list[cConsultorio], pacientes: list[cPaciente], enfermeros: list[cEnfermero]):
        self.consultorios=consultorios
        self.pacientes=pacientes
        self.enfermeros=enfermeros




