import pytest
from library.classConsultorio import cConsultorio
from library.classPaciente import cPaciente
from library.classEnfermedad import cEnfermedad
from library.classEnfermero import cEnfermero
from library.classPriorityQueuePaciente import PriorityQueuePaciente

def test_curar():
    enfermedad_aux=cEnfermedad("indefinido",0,"indefinido",0,0)
    sintomas_aux=["urgencia_psiquiatrica_s"]
    paciente_aux=cPaciente("0011","Maria Susana",enfermedad_aux,"ninguno",sintomas_aux,"enfermo")
    consultorio_aux=cConsultorio()
    consultorio_aux.curar(paciente_aux)
    assert paciente_aux.estado=="sano"

def test_atender_urgencia():
    enfermedad_aux1 = cEnfermedad("indefinido", 0, "indefinido", 0, 0)
    enfermedad_aux2 = cEnfermedad("indefinido", 0, "indefinido", 0, -200)
    sintomas_aux=["riesgo_vital"]
    paciente_aux1 = cPaciente("0011", "Maria Susana", enfermedad_aux1, "ninguno", sintomas_aux, "enfermo")
    paciente_aux2 = cPaciente("0011", "Maria Susana", enfermedad_aux2, "ninguno", sintomas_aux, "enfermo")
    try:
        cConsultorio.atender_urgencia(paciente_aux1)
        cConsultorio.atender_urgencia(paciente_aux2)
    except Exception as e:
        print(e.args)
    assert paciente_aux1.estado=="sano"
    assert paciente_aux2.estado=="muerto"

def test_atender_DC():
    #test 1
    enfermedad1=cEnfermedad("verde",45,"esguince",5,cEnfermero.tmax_verde)
    enfermedad2=cEnfermedad("rojo",5,"politraumatismo_grave",100,0)
    enfermedad3=cEnfermedad("naranja",20,"isquemia",10,cEnfermero.tmax_naraja)
    enfermedad4=cEnfermedad("azul",5,"no_urgencia",2,cEnfermero.tmax_azul)

    consultorio=cConsultorio()
    enfermero= cEnfermero(3,"Emi")

    lista_sintomas:list[str]=[]

    paciente1=cPaciente(6,"Agos",enfermedad1,"embarazo",lista_sintomas )#los sintomas no me importan para este test
    paciente2=cPaciente(7,"Pau", enfermedad2, "ninguno",lista_sintomas)#en teoria no deberia llegar a estar pero como le pusimos una prioridad muy alta lo deberia atender
    paciente3=cPaciente(8,"Lupe",enfermedad3,"obesidad",lista_sintomas)
    paciente4=cPaciente(9,"Valen",enfermedad4 ,"mayor_edad",lista_sintomas)

    lista:list[cPaciente]=[paciente1,paciente2, paciente3, paciente4]

    consultorio.atender_DC(lista, enfermero)
    assert len(lista)==0
    assert paciente1.estado=="sano"
    assert paciente2.estado == "sano"
    assert paciente3.estado == "sano"
    assert paciente4.estado == "sano"

def test_atender_G():
    consultorio = cConsultorio( False)

    enfermedad1=cEnfermedad("verde",45,"esguince",5,cEnfermero.tmax_verde)
    enfermedad3=cEnfermedad("naranja",20,"isquemia",10,cEnfermero.tmax_naraja)
    enfermedad4=cEnfermedad("azul",5,"no_urgencia",2,cEnfermero.tmax_azul)

    lista_sintomas: list[str] = []

    paciente1 = cPaciente(6, "Agos", enfermedad1, "embarazo", lista_sintomas)  # los sintomas no me importan
    paciente3 = cPaciente(8, "Lupe", enfermedad3, "obesidad", lista_sintomas)
    paciente4 = cPaciente(9, "Valen", enfermedad4, "mayor_edad", lista_sintomas)

    filaA=PriorityQueuePaciente()
    filaA.push(paciente3.diagnostico.prioridad,paciente3)
    filaB=PriorityQueuePaciente()
    filaB.push(paciente1.diagnostico.prioridad,paciente1)
    filaB.push(paciente4.diagnostico.prioridad,paciente4)

    consultorio.atender_G(filaA,filaB,0)

    assert filaA.is_empty()==True
    assert filaB.is_empty()==True


