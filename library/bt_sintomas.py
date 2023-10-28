from binarytree import Node
from enums import eSintomas
from enums import eEnfermedad
def arbol_sintomas():
    eSintomas.respiracion_irregular=Node

    respiracion_irregular.left=pulsaciones_agitadas
    pulsaciones_agitadas.left=nauseas
    nauseas.left=isquemia
    nauseas.right=convoluciones
    pulsaciones_agitadas.right=inconsiente
    inconsciente.left=coma
    inconsciente.right=hemorragia_digestiva

    respitacion_irregular.right=dolor
    dolor.left=mareo_desmayo
    mareo_desmayo.left=pulsaciones_agitadas
    pulsaciones_agitadas.left=hipertension_arterial
    pulsaciones_agitadas.right=vertigo

    mareo_demsayo.right=hinchazon
    hinchazon.left=lagrimeo
    lagrimeo.left=cefalea_brusca
    lagrimeo.right=esguince
    hinchazon.right=hemorragia
    hemorragia.left=odontalgia
    hemorragia.right=dolor_inespecifico_leve

    dolor.right=aturdimiento
    atrurdimiento.left=picazon
    picazon.left=otalgia
    picazon.right=sincope

    aturdimiento.right=ambulancia
    ambulancia.left=politraumatismo_grave
    ambulancia.right=urgencia_psiquiatrica
    urgencia_psiquiatrica.left=urgencia_psiquiatrica
    urgencia_psiquiatrica.right=no_urgencia


