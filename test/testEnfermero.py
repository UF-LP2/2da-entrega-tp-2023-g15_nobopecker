from library.classEnfermero import cEnfermero
from library.bt_sintomas import arbol_sintomas

def test_comprarsintomas():
    enfermero=cEnfermero(1,"Pepe")
    sintomas:list[str]=["riesgo_vital"]
    enfermedad=enfermero.comparar_sintomas(sintomas, arbol_sintomas()).name
    assert enfermedad =="politraumatismo_grave"

def test_convertfr():
    assert cEnfermero.embarazo == cEnfermero.convert_fr("embarazo")
