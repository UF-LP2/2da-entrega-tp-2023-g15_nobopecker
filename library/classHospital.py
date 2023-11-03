from library.classEnfermero import cEnfermero
from library.classPaciente import cPaciente
from library.classConsultorio import cConsultorio
class cHospital:

    def __init__(self, consultorios: list[cConsultorio], pacientes: list[cPaciente], enfermeros: list[cEnfermero]):
        self.consultorios=consultorios
        self.pacientes=pacientes
        self.enfermeros=enfermeros




