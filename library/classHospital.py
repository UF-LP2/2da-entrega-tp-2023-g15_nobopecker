from classEnfermero import cEnfermero
from classPaciente import cPaciente
from classConsultorio import cConsultorio
class cHospital:

    def __init__(self, consultorios: cConsultorio[], pacientes: cPaciente[], enfermeros):
        self.consultorios=consultorios
        self.pacientes=pacientes
        self.enfermeros=enfermeros

#
# atender_urgencia(paciente): { //método del hospital
#	para x=0 hasta hospital.consultorios.tamaño(): //recorro la lista de consultorios hasta encontrar uno libre
#		si hospital.consultorio[x].ocupado==false:
#			cortar_ciclo() //break pero en pseudo

#	si (x== hospital.consultorios.tamaño()):
#		x=hospital.liberar_un_consultorio() //esta función libera el consultorio con el paciente de menor prioridad entre los que están siendo atendidos en ese momento. Se interrumpe el tiempo de consulta y se continuará una vez que el rojo haya terminado.

#	consultorio[x].medico.curar(paciente) //curamos al paciente en el consultorio determinado
# }

def atender_urgencia(paciente: cPaciente) ->None:
    for x in range
