from classPaciente import  cPaciente
from classConsultorio import cConsultorio
from enums import eSintomas_Enfermedades
class cEnfermero:

    def __init__(self, ID, turno, arbol_sintomas):
        self.ID=ID
        self.turno=turno
        arbol_sintomas=arbol_sintomas
    #def diagnosticar(paciente):
       # return definir_enfermedad(paciente.sintomas, arbol_sintomas)
    #def definir_enfermedad(sintomas, arbol_sintomas):
        #if arbol_sintomas.right==null

    def clasificar(paciente:cPaciente):
            if paciente.diagnostico.color==rojo:
                #atender_urgencia(paciente)
            elif paciente.diagnostico==eSintomas_Enfermedades.coma||paciente.diagnostico==eSintomas_Enfermedades.convulsiones||


####naranja
    coma=24
    convulsiones=25
    hemorragia_digestiva=26
    isquemia=27
    #amarillo
    cefalea_brusca=28
    paresia=29
    hipertension_arterial=30
    vertigo=31
    sincope=32
    #urgencia_psiquiatrica=19
    #verde
    otalgia=33
    odontalgia=34
    dolor_inespecifico_leve=35
    esguince=36
    #azul
    no_urgencia=37