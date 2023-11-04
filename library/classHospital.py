from library.classEnfermero import cEnfermero
from library.classPaciente import cPaciente
from library.classConsultorio import cConsultorio
class cHospital:

    def __init__(self, consultorio:cConsultorio, pacientes: list[cPaciente], enfermeros: list[cEnfermero]):
        self.consultorio=consultorio
        self.pacientes=pacientes
        self.enfermeros=enfermeros




