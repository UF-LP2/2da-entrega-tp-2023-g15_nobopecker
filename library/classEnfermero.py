from classPaciente import  cPaciente
from classConsultorio import cConsultorio
from enums import eSintomas
from enums import eEnfermedad
from binarytree import Node
class cEnfermero:
    #arbol_sintomas =
    def __init__(self, ID, turno):
        self.ID=ID
        self.turno=turno

    def diagnosticar(paciente:cPaciente)-> cEnfermedad:
       return definir_enfermedad(paciente.sintomas)

    def definir_enfermedad(sintomas:eSintomas)->cEnfermedad:
        nombre_enfermedad= (eEnfermedad)comparar_sintomas(sintomas)
        enfermedad=cEnfermedad()
        return

    def comparar_sintomas(sintomas)->Node:
        if arbol_sintomas.right==null and arbol_sintomas.left==null: #hoja
            return arbol_sintomas.value
        else:
            return comparar_sintomas(sintomas, arbol_sintomas.left) if arbol_sintomas.value in sintomas else comparar_sintomas(sintomas, arbol_sintomas.right)




