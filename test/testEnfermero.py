from unittest import TestCase
from src.classEnfermero import cEnfermero
from src.bt_sintomas import arbol_sintomas


class test_cEnfermero(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_comprar_sintomas(self):
        enfermero=cEnfermero(1,"Pepe")
        enfermedad=enfermero.comparar_sintomas("riesgo_vital", arbol_sintomas()).value
        self.assertEquals(enfermedad,"politraumatismo_grave")
