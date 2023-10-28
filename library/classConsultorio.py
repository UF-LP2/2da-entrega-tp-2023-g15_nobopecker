from classPaciente import cPaciente
from enums import eEstado
class cConsultorio:

    def __init__(self, numero:int, paciente_actual: cPaciente ,ocupado = False):
        self.ocupado=ocupado
        self.numero=numero
        self.paciente_actual=paciente_actual

    def curar(self, paciente:cPaciente) -> None: #metodo de curar paciente
        paciente.estado= eEstado.sano

    def atender_urgencia (paciente: cPaciente) ->None: #metodo de curar paciente static para atender urgencias sin importar consultorios libres
        paciente.estado= eEstado.sano

