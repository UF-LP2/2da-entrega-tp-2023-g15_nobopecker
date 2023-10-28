from enum import Enum
class eEstado(Enum):
    sano=0
    enfermo=1
    muerto=2

class eSintomas_Enfermedades(Enum):
    #sintomas
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
    #enfermedades
    politraumatismo_grave=23
    coma=24
    convulsiones=25
    hemorragia_digestiva=26
    isquemia=27
    cefalea_brusca=28
    paresia=29
    hipertension_arterial=30
    vertigo=31
    sincope=32
    #urgencia_psiquiatrica=19
    otalgia=33
    odontalgia=34
    dolor_inespecifico_leve=35
    esguince=36
    no_urgencia=37

class eColor(Enum):
    rojo=0
    naranja=1
    amarillo=2
    verde=3
    azul=4
    indefinido=5