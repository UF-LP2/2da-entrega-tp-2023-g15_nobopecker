from enum import Enum
class eEstado(Enum):
    sano=0
    enfermo=1
    muerto=2

class eSintomas(Enum):
    ambulancia=0
    inconsciente=1
    respiracion_irregular=2
    babea=3
    pulsaciones_agitadas=4
    nauseas=5
    dolor=6
    mareo_desmayo=7
    cansancio=8
    palidez=9
    sudoracion=10
    enrojecimiento_ocular=11
    lagrimeo=12
    congestion_nasal=13
    hinchazon=14
    perdida_control_muscular=15
    vision_borrosa=16
    aturdimiento=17
    sensacion_calor=18
    urgencia_psiquiatrico=19
    picazon=20
    hemorragia=21
    fiebre=22

class eEnfermedad(Enum):
    politraumatismo_grave=0
    coma=1
    convulsiones=2
    hemorragia_digestiva=3
    isquemia=4
    cefalea_brusca=5
    paresia=6
    hipertension_arterial=7
    vertigo=8
    sincope=9
    urgencia_psiquiatrica=10
    otalgia=11
    odontalgia=12
    dolor_inespecifico_leve=13
    esguince=14
    no_urgencia=15

class eColor(Enum):#el nro de la derecha corresponde al tiempo max de espera
    rojo=0
    naranja=10
    amarillo=60
    verde=120
    azul=240
    indefinido=5

class eFactor_Riesgo(Enum): #el nro de la derecha es un entero que se sumará a la prioridad de la enfermedad del paciente
    #condiciones
    embarazo=6
    mayor_edad=3
    #complicaciones o enfermedades preexistentes
    obesidad=2
    diabetes=1
    enf_cardiovasculares=5
    enf_respiratorias=4
    #no tiene factores de riesgo adicionales a su enfermedad
    ninguno=0