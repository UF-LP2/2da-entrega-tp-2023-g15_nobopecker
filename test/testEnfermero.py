from unittest import TestCase
from library.classEnfermero import cEnfermero
from binarytree import Node
from library.bt_sintomas import arbol_sintomas

class test_cEnfermero(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_comprar_sintomas(self):
        enfermero=cEnfermero(1,"Pepe")
        enfermedad=enfermero.comparar_sintomas("riesgo_vital", arbol_sintomas()).value
        self.assertEquals()