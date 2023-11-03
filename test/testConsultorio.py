import queue

import pytest
from library.classConsultorio import cConsultorio
from library.classPaciente import cPaciente
from library.classEnfermedad import cEnfermedad
from library.classEnfermero import cEnfermero
from queue import PriorityQueue

def test_curar():
    enfermedad_aux=cEnfermedad("indefinido",0,"indefinido",0,0)
    sintomas_aux=["urgencia_psiquiatrica_s"]
    paciente_aux=cPaciente("0011","Maria Susana",enfermedad_aux,"ninguno",sintomas_aux,"enfermo")
    consultorio_aux=cConsultorio(2,paciente_aux,False)
    consultorio_aux.curar(paciente_aux)
    assert paciente_aux.estado=="sano"

def test_atender_urgencia():
    enfermedad_aux = cEnfermedad("indefinido", 0, "indefinido", 0, 0)
    sintomas_aux=["riesgo_vital"]
    paciente_aux = cPaciente("0011", "Maria Susana", enfermedad_aux, "ninguno", sintomas_aux, "enfermo")
    cConsultorio.atender_urgencia(paciente_aux)
    assert paciente_aux.estado=="sano"

def test_atender_DC():
    consultorio=cConsultorio(1,None,False)
    enfermero= cEnfermero(3,"Emi")
    paciente1=cPaciente(6,"Agos","esguince","embarazo", "")#los sintomas no me importan
    paciente2=cPaciente(7,"Pau", "politraumatismo_grave", "ninguno","riesgo_vital")#en teoria no deberia llegar a estar pero como le pusimos una prioridad muy alta lo deberia atender
    paciente3=cPaciente(8,"Lupe","isquemia","obesidad","")
    paciente4=cPaciente(9,"Valen","no_urgencia","mayor_edad","")

    lista=list[paciente1,paciente2, paciente3, paciente4]

    consultorio.atender_DC(lista, enfermero)
    assert len(lista)==0
    assert paciente1.estado=="sano"
    assert paciente2.estado == "sano"
    assert paciente3.estado == "sano"
    assert paciente4.estado == "sano"

def test_atender_G():
    consultorio = cConsultorio(1, None, False)
    enfermero = cEnfermero(3, "Emi")
    paciente1 = cPaciente(6, "Agos", "esguince", "embarazo", "")  # los sintomas no me importan
    paciente2 = cPaciente(7, "Pau", "politraumatismo_grave", "ninguno",
                          "riesgo_vital")  # en teoria no deberia llegar a estar pero como le pusimos una prioridad muy alta lo deberia atender
    paciente3 = cPaciente(8, "Lupe", "isquemia", "obesidad", "")
    paciente4 = cPaciente(9, "Valen", "no_urgencia", "mayor_edad", "")

    filaA = PriorityQueue()
    riesgo3=enfermero.convert_fr(paciente3.factor_riesgo)
    filaA.put((paciente3.diagnostico.prioridad+riesgo3,paciente3))
