from src.archivos import leerPaciente
from library.classPaciente import cPaciente
from unittest import TestCase

class TestLeerPaciente(TestCase):
    def test_listapacientes(self):
        lista_pac:list[cPaciente]=leerPaciente()
        assert (lista_pac[1].nombre_apellido=="Cesar Crossley") == True
        assert (lista_pac[0].factor_riesgo=="obesidad")==True
        assert (lista_pac[27].ID=="4659")==True