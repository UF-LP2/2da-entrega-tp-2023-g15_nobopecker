import time

from classPaciente import cPaciente
from enums import eEstado
from classEnfermero import cEnfermero
class cConsultorio:

    def __init__(self, numero:int, paciente_actual: cPaciente ,ocupado = False):
        self.ocupado=ocupado
        self.numero=numero
        self.paciente_actual=paciente_actual

    def curar(self, paciente:cPaciente) -> None: #metodo de curar paciente
        paciente.estado= eEstado.sano

    @staticmethod
    def atender_urgencia (paciente: cPaciente) ->None: #metodo de curar paciente static para atender urgencias sin importar consultorios libres
        paciente.estado= eEstado.sano

    def atender(self, lista:list[cPaciente], enfermero: cEnfermero)->None:
        if len(lista)==0: #caso base: no hay mas elementos en la lista
            return
        paciente:cPaciente=enfermero.elegir_paciente_optimo(lista) #elijo el paciente que maximiza prioridad/duracion
        lista.remove(paciente) #lo saco de la lista
        self.ocupado=True #el consultorio esta ocupado hasta que termino de atenderlo
        cConsultorio.curar(self, paciente)
        time.sleep(paciente.diagnostico.duracion) #detengo el programa la duracion de la consulta
        self.ocupado = False #desocupo el consultorio
        cConsultorio.atender(self, lista, enfermero) #sigo atendiendo la lista




