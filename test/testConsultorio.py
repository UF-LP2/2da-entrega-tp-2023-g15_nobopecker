import pytest
from library.classConsultorio import cConsultorio
from library.classPaciente import cPaciente
from library.classEnfermedad import cEnfermedad

def test_curar():
    enfermedad_aux=cEnfermedad("indefinido",0,"indefinido",0,0)
    sintomas_aux=["urgencia_psiquiatrica_s"]
    pacientito=cPaciente("0011",enfermedad_aux,"ninguno",sintomas_aux,"enfermo")
    consultorio=cConsultorio(2,pacientito,False)
    consultorio.curar(pacientito)
    assert pacientito.estado=="sano"