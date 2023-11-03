from library.classEnfermero import cEnfermero
from library.bt_sintomas import arbol_sintomas

def testcomprarsintomas(self):
    enfermero=cEnfermero(1,"Pepe")
    enfermedad=enfermero.comparar_sintomas("riesgo_vital", arbol_sintomas()).value
    assert enfermedad =="politraumatismo_grave"
