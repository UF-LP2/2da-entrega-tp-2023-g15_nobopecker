from classPaciente import cPaciente
from enums import eEstado
class cConsultorio:

    def __init__(self, numero:int ,ocupado = False):
        self.ocupado=ocupado
        self.numero=numero

    def curar(self, paciente:cPaciente) -> None:
        paciente.estado= eEstado.sano

