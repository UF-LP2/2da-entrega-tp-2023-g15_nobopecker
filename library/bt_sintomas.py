from typing import Type

from binarytree import Node
from enums import eSintomas
from enums import eEnfermedad
def arbol_sintomas():

    #inicializo nodos
    eSintomas.respiracion_irregular=Node(100)
    eSintomas.pulsaciones_agitadas= Node(30)
    eSintomas.dolor= Node(150)
    eSintomas.nauseas= Node(15)
    eSintomas.inconsciente= Node(50)
    eEnfermedad.isquemia= Node(10)
    eEnfermedad.convulsiones =Node(200)
    eEnfermedad.coma = Node(40)
    eEnfermedad.hemorragia_digestiva = Node(60)
    eSintomas.mareo_desmayo = Node(120)
    eSintomas.vision_borrosa = Node(110)
    eEnfermedad.hipertension_arterial = Node(105)
    eEnfermedad.vertigo = Node(115)
    eSintomas.hinchazon = Node(140)
    eSintomas.lagrimeo = Node(130)
    eEnfermedad.cefalea_brusca = Node(125)
    eEnfermedad.esguince = Node(135)
    eSintomas.hemorragia = Node(145)
    eEnfermedad.odontalgia = Node(142)
    eEnfermedad.dolor_inespecifico_leve = Node(148)
    eSintomas.aturdimiento= Node(180)
    eSintomas.picazon = Node(160)
    eEnfermedad.otalgia = Node(155)
    eEnfermedad.sincope = Node(165)
    eSintomas.ambulancia = Node(200)
    eEnfermedad.politraumatismo_grave = Node(190)
    eSintomas.urgencia_psiquiatrica = Node(220)
    eEnfermedad.urgencia_psiquiatrica = Node(210)
    eEnfermedad.no_urgencia = Node(230)

    #arbol
    eSintomas.respiracion_irregular.left=eSintomas.pulsaciones_agitadas
    eSintomas.pulsaciones_agitadas.left=eSintomas.nauseas
    eSintomas.nauseas.left=eEnfermedad.isquemia
    eSintomas.nauseas.right=eEnfermedad.convulsiones
    eSintomas.pulsaciones_agitadas.right=eSintomas.inconsciente
    eSintomas.inconsciente.left=eEnfermedad.coma
    eSintomas.inconsciente.right=eEnfermedad.hemorragia_digestiva

    eSintomas.respiracion_irregular.right=eSintomas.dolor
    eSintomas.dolor.left=eSintomas.mareo_desmayo
    eSintomas.mareo_desmayo.left=eSintomas.pulsaciones_agitadas
    eSintomas.vision_borrosa.left=eEnfermedad.hipertension_arterial
    eSintomas.vision_borrosa.right=eEnfermedad.vertigo

    eSintomas.mareo_desmayo.right=eSintomas.hinchazon
    eSintomas.hinchazon.left=eSintomas.lagrimeo
    eSintomas.lagrimeo.left=eEnfermedad.cefalea_brusca
    eSintomas.lagrimeo.right=eEnfermedad.esguince
    eSintomas.hinchazon.right=eSintomas.hemorragia
    eSintomas.hemorragia.left=eEnfermedad.odontalgia
    eSintomas.hemorragia.right=eEnfermedad.dolor_inespecifico_leve

    eSintomas.dolor.right=eSintomas.aturdimiento
    eSintomas.aturdimiento.left=eSintomas.picazon
    eSintomas.picazon.left=eEnfermedad.otalgia
    eSintomas.picazon.right=eEnfermedad.sincope

    eSintomas.aturdimiento.right=eSintomas.ambulancia
    eSintomas.ambulancia.left=eEnfermedad.politraumatismo_grave
    eSintomas.ambulancia.right=eSintomas.urgencia_psiquiatrica
    eSintomas.urgencia_psiquiatrica.left=eEnfermedad.urgencia_psiquiatrica
    eSintomas.urgencia_psiquiatrica.right=eEnfermedad.no_urgencia

    print (eSintomas.respiracion_irregular)

if __name__ == "__main__":
    arbol_sintomas()


