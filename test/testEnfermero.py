from library.classEnfermero import cEnfermero
from library.bt_sintomas import arbol_sintomas
from library.classEnfermedad import cEnfermedad
from library.classPaciente import cPaciente

def test_comprarsintomas1():
    enfermero=cEnfermero(1,"Pepe")
    sintomas:list[str]=["riesgo_vital"]
    enfermedad=enfermero.comparar_sintomas(sintomas, arbol_sintomas()).name
    assert enfermedad =="politraumatismo_grave"

def test_comprarsintomas2():
    enfermero=cEnfermero(4,"Pepa")
    sintomas:list[str]=["enrojecimiento_ocular", "lagrimeo", "congestion_nasal", "hinchazon", "dolor"]
    enfermedad=enfermero.comparar_sintomas(sintomas, arbol_sintomas()).name
    assert enfermedad =="cefalea_brusca"

def test_comprarsintomas3():
    enfermero=cEnfermero(8,"Jose")
    sintomas:list[str]=["dolor", "hemorragia", "fiebre"]
    enfermedad=enfermero.comparar_sintomas(sintomas, arbol_sintomas()).name
    assert enfermedad =="odontalgia"

def test_definirenfermedad1():
    enfermero=cEnfermero(1,"Pepe")
    sintomas:list[str]=["riesgo_vital"]
    diagnostico_aux:cEnfermedad= enfermero.definir_enfermedad(sintomas)
    assert diagnostico_aux.enfermedad =="politraumatismo_grave"
    assert diagnostico_aux.color=="rojo"
    assert diagnostico_aux.prioridad==100
    assert diagnostico_aux.tiempo_restante==cEnfermero.tmax_rojo
    assert diagnostico_aux.duracion==5

def test_definirenfermedad2():
    enfermero=cEnfermero(4,"Pepa")
    sintomas:list[str]=["enrojecimiento_ocular", "lagrimeo", "congestion_nasal", "hinchazon", "dolor"]
    diagnostico_aux:cEnfermedad= enfermero.definir_enfermedad(sintomas)
    assert diagnostico_aux.enfermedad =="cefalea_brusca"
    assert diagnostico_aux.color=="amarillo"
    assert diagnostico_aux.prioridad==8
    assert diagnostico_aux.tiempo_restante==cEnfermero.tmax_amarillo
    assert diagnostico_aux.duracion==15

def test_definirenfermedad3():
    enfermero=cEnfermero(8,"Jose")
    sintomas:list[str]=["dolor", "hemorragia", "fiebre"]
    diagnostico_aux:cEnfermedad= enfermero.definir_enfermedad(sintomas)
    assert diagnostico_aux.enfermedad =="odontalgia"
    assert diagnostico_aux.color=="verde"
    assert diagnostico_aux.prioridad==4
    assert diagnostico_aux.tiempo_restante==cEnfermero.tmax_verde
    assert diagnostico_aux.duracion==35

def test_diagnosticar():
    enfermero = cEnfermero(4, "Pepa")
    dummy = cEnfermedad("indefinido", 0, "indefinido", 0, 0)
    sintomas: list[str] = ["enrojecimiento_ocular", "lagrimeo", "congestion_nasal", "hinchazon", "dolor"]
    paciente=cPaciente(0,"John Doe",dummy, "ninguno",sintomas,"enfermo")
    diagnostico_aux: cEnfermedad = enfermero.diagnosticar(paciente)
    assert diagnostico_aux.enfermedad =="cefalea_brusca"
    assert diagnostico_aux.color=="amarillo"
    assert diagnostico_aux.prioridad==8
    assert diagnostico_aux.tiempo_restante==cEnfermero.tmax_amarillo
    assert diagnostico_aux.duracion==15

def test_elegirpacienteoptimo():
    enfermero=cEnfermero(2,"Tobias")
    enf1=cEnfermedad("rojo",5,"politraumatismo_grave",100,cEnfermero.tmax_rojo)
    sint1: list[str] = ["riesgo_vital"]
    pac1=cPaciente(0,"Juan",enf1,"ninguno",sint1,"enfermo")
    enf2=cEnfermedad("amarillo",15,"cefalea_brusca",8,cEnfermero.tmax_amarillo)
    sint2: list[str] = ["enrojecimiento_ocular", "lagrimeo", "congestion_nasal", "hinchazon", "dolor"]
    pac2=cPaciente(1,"Josefina",enf2,"embarazo",sint2,"enfermo")
    enf3=cEnfermedad("verde",35,"odontalgia",4,cEnfermero.tmax_verde)
    sint3: list[str] = ["dolor", "hemorragia", "fiebre"]
    pac3=cPaciente(2,"Ricardo",enf3,"enf_cardiovascular",sint3,"enfermo")
    listita:list[cPaciente]=[]
    listita.append(pac1)
    listita.append(pac2)
    listita.append(pac3)
    optimo=pac1
    assert optimo == enfermero.elegir_paciente_optimo(listita)


def test_convertfr():
    assert cEnfermero.embarazo == cEnfermero.convert_fr("embarazo")
    assert cEnfermero.diabetes == cEnfermero.convert_fr("diabetes")
    assert cEnfermero.obesidad == cEnfermero.convert_fr("obesidad")

