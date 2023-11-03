from library.classPaciente import cPaciente
from src.archivos import leerPaciente
from library.classEnfermero import cEnfermero
from src.archivos import leerEnfermero
import pytest

def test_leerpac1():
    lista_pac:list[cPaciente]=leerPaciente()
    assert (lista_pac[0].nombre_apellido=="Berk Torrisi")

def test_leerpac2():
    lista_pac:list[cPaciente]=leerPaciente()
    assert (lista_pac[1].factor_riesgo=="diabetes")

def test_leerpac3():
    lista_pac:list[cPaciente]=leerPaciente()
    assert (lista_pac[2].ID=="7580")

def test_leerpac4():
    lista_pac:list[cPaciente]=leerPaciente()
    assert ("dolor" in lista_pac[3].sintomas)

def test_leerenf1():
    lista_enf:list[cEnfermero]=leerEnfermero()
    assert (lista_enf[0].nombre_apellido=="Brewer Feldfisher")

def test_leerenf2():
    lista_enf:list[cEnfermero]=leerEnfermero()
    assert (lista_enf[4].ID=="3877")

