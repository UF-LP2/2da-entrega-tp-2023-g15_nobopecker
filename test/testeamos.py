import pytest
from library.classEnfermero import cEnfermero
from library.bt_sintomas import arbol_sintomas

from binarytree import Node

class testEnfermero(pytest.TestCase):

    def test_comparar_sintomas(self):
        enfermedad=cEnfermero.comparar_sintomas("ambulancia",arbol_sintomas()).value
        assert enfermedad,"politraumatismo_grave"