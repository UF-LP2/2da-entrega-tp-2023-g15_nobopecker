from library.classEnfermero import cEnfermero
from library.bt_sintomas import arbol_sintomas

def testcomprarsintomas():
    enfermero=cEnfermero(1,"Pepe")
    sintomas:list[str]=["riesgo_vital"]
    enfermedad=enfermero.comparar_sintomas(sintomas, arbol_sintomas()).value
    assert enfermedad =="politraumatismo_grave"
