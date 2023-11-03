import pytest
from library.classConsultorio import cConsultorio
from library.classPaciente import cPaciente
from library.classEnfermedad import cEnfermedad

def test_curar():
    enfermedad_aux=cEnfermedad("indefinido",0,"indefinido",0,0)
    sintomas_aux=["urgencia_psiquiatrica_s"]
    paciente_aux=cPaciente("0011","Maria Susana",enfermedad_aux,"ninguno",sintomas_aux,"enfermo")
    consultorio_aux=cConsultorio(2,paciente_aux,False)
    consultorio_aux.curar(paciente_aux)
    assert paciente_aux.estado=="sano"