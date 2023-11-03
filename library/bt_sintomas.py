from library.classNodos import Nodo
from binarytree import Node

def arbol_sintomas() -> Nodo:

    #inicializo nodos
    respiracion_irregular=Nodo(100,"respiracion_irregular")
    pulsaciones_agitadas= Nodo(30,"pulsaciones_agitadas")
    dolor= Nodo(150,"dolor")
    nauseas= Nodo(15,"nauseas")
    inconsciente= Nodo(50,"inconsciente")
    isquemia= Nodo(10,"isquemia")
    convulsiones =Nodo(200,"convulsiones")
    coma = Nodo(40,"coma")
    hemorragia_digestiva = Nodo(60,"hemorragia_digestiva")
    mareo_desmayo = Nodo(120,"mareo_desmayo")
    vision_borrosa = Nodo(110,"vision_borrosa")
    hipertension_arterial = Nodo(105,"hipertension_arterial")
    vertigo = Nodo(115,"vertigo")
    hinchazon = Nodo(140,"hinchazon")
    lagrimeo = Nodo(130,"lagrimeo")
    cefalea_brusca = Nodo(125,"cefalea_brusca")
    esguince = Nodo(135,"esguince")
    hemorragia = Nodo(145,"hemorragia")
    odontalgia = Nodo(142,"odontalgia")
    dolor_inespecifico_leve = Nodo(148,"dolor_inespecifico_leve")
    aturdimiento= Nodo(180,"aturdimiento")
    picazon = Nodo(160,"picazon")
    otalgia = Nodo(155,"otalgia")
    sincope = Nodo(165,"sincope")
    riesgo_vital = Nodo(200,"riesgo_vital")
    politraumatismo_grave = Nodo(190,"politraumatismo_grave")
    urgencia_psiquiatrica_s = Nodo(220,"urgencia_psiquiatrica_s")
    urgencia_psiquiatrica_e = Nodo(210,"urgencia_psiquiatrica_e")
    no_urgencia = Nodo(230,"no_urgencia")

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

    aturdimiento.right=riesgo_vital
    riesgo_vital.left=politraumatismo_grave
    riesgo_vital.right=urgencia_psiquiatrica_s
    urgencia_psiquiatrica_s.left=urgencia_psiquiatrica_e
    urgencia_psiquiatrica_s.right=no_urgencia

    return respiracion_irregular



