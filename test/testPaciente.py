from library.classEnfermedad import cEnfermedad
from library.classPaciente import cPaciente
import pytest

def test_comparar_prioridad():
    sintomas:list[str]=[]
    enfermedad1=cEnfermedad("rojo",5,"politraumatismo_grave",100,0)
    enfermedad2=cEnfermedad("azul",5,"no_urgencia",2,240)
    pac1=cPaciente(1234,"Pepe",enfermedad1,"embarazo",sintomas)
    pac2=cPaciente(5678,"Pipi",enfermedad2,"mayor_edad",sintomas)
    assert (pac1>pac2) ==True


