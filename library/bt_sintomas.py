from binarytree import Node

def arbol_sintomas():

    #inicializo nodos
    respiracion_irregular=Node(100)
    pulsaciones_agitadas= Node(30)
    dolor= Node(150)
    nauseas= Node(15)
    inconsciente= Node(50)
    isquemia= Node(10)
    convulsiones =Node(200)
    coma = Node(40)
    hemorragia_digestiva = Node(60)
    mareo_desmayo = Node(120)
    vision_borrosa = Node(110)
    hipertension_arterial = Node(105)
    vertigo = Node(115)
    hinchazon = Node(140)
    lagrimeo = Node(130)
    cefalea_brusca = Node(125)
    esguince = Node(135)
    hemorragia = Node(145)
    odontalgia = Node(142)
    dolor_inespecifico_leve = Node(148)
    aturdimiento= Node(180)
    picazon = Node(160)
    otalgia = Node(155)
    sincope = Node(165)
    ambulancia = Node(200)
    politraumatismo_grave = Node(190)
    urgencia_psiquiatrica_s = Node(220)
    urgencia_psiquiatrica_e = Node(210)
    no_urgencia = Node(230)

    #arbol
    respiracion_irregular.left=pulsaciones_agitadas
    pulsaciones_agitadas.left=nauseas
    nauseas.left=isquemia
    nauseas.right=convulsiones
    pulsaciones_agitadas.right=inconsciente
    inconsciente.left=coma
    inconsciente.right=hemorragia_digestiva

    respiracion_irregular.right=dolor
    dolor.left=mareo_desmayo
    mareo_desmayo.left=pulsaciones_agitadas
    vision_borrosa.left=hipertension_arterial
    vision_borrosa.right=vertigo

    mareo_desmayo.right=hinchazon
    hinchazon.left=lagrimeo
    lagrimeo.left=cefalea_brusca
    lagrimeo.right=esguince
    hinchazon.right=hemorragia
    hemorragia.left=odontalgia
    hemorragia.right=dolor_inespecifico_leve

    dolor.right=aturdimiento
    aturdimiento.left=picazon
    picazon.left=otalgia
    picazon.right=sincope

    aturdimiento.right=ambulancia
    ambulancia.left=politraumatismo_grave
    ambulancia.right=urgencia_psiquiatrica_s
    urgencia_psiquiatrica_s.left=urgencia_psiquiatrica_e
    urgencia_psiquiatrica_s.right=no_urgencia

    print (respiracion_irregular)

if __name__ == "__main__":
    arbol_sintomas()


