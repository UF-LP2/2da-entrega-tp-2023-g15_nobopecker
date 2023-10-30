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
        nodo_enfermedad= comparar_sintomas(sintomas)
        nombre_enfermedad=nodo_enfermedad.value
        #inicializo una enfermedad cualquiera y despues tapo los datos con lo que me devuelve el arbol
        aux=cEnfermedad(eColor.indefinido, 0, eEnfermedad.no_urgencia, 0,0)
        if nombre_enfermedad=="politraumatismo_grave":
            aux.color=eColor.rojo
            aux.enfermedad=eEnfermedad.politraumatismo_grave
            aux.prioridad=100
            aux.tiempo_restante=int(eColor.rojo)
            aux.duracion=5

        elif nombre_enfermedad=="isquemia":
            aux.color = eColor.naranja
            aux.enfermedad = eEnfermedad.isquemia
            aux.prioridad =10
            aux.tiempo_restante =int(eColor.naranja)
            aux.duracion = 20

        elif nombre_enfermedad=="convulsiones":
            aux.color = eColor.naranja
            aux.enfermedad = eEnfermedad.convulsiones
            aux.prioridad =15
            aux.tiempo_restante =int(eColor.naranja)
            aux.duracion = 10

        elif nombre_enfermedad=="coma":
            aux.color = eColor.naranja
            aux.enfermedad = eEnfermedad.coma
            aux.prioridad =10
            aux.tiempo_restante =int(eColor.naranja)
            aux.duracion = 10

        elif nombre_enfermedad=="hemorragia_digestiva":
            aux.color = eColor.naranja
            aux.enfermedad = eEnfermedad.hemorragia_digestiva
            aux.prioridad =10
            aux.tiempo_restante =int(eColor.naranja)
            aux.duracion = 12

        elif nombre_enfermedad=="hipertension_arterial":
            aux.color = eColor.amarillo
            aux.enfermedad = eEnfermedad.hipertension_arterial
            aux.prioridad =7
            aux.tiempo_restante =int(eColor.amarillo)
            aux.duracion = 20

        elif nombre_enfermedad=="vertigo":
            aux.color = eColor.amarillo
            aux.enfermedad = eEnfermedad.vertigo
            aux.prioridad =7
            aux.tiempo_restante =int(eColor.amarillo)
            aux.duracion = 15

        elif nombre_enfermedad=="cefalea_brusca":
            aux.color = eColor.amarillo
            aux.enfermedad = eEnfermedad.cefalea_brusca
            aux.prioridad =8
            aux.tiempo_restante =int(eColor.amarillo)
            aux.duracion = 15

        elif nombre_enfermedad=="paresia":
            aux.color = eColor.amarillo
            aux.enfermedad = eEnfermedad.paresia
            aux.prioridad =8
            aux.tiempo_restante =int(eColor.amarillo)
            aux.duracion = 25

        elif nombre_enfermedad =="esguince":
            aux.color = eColor.verde
            aux.enfermedad = eEnfermedad.esguince
            aux.prioridad =5
            aux.tiempo_restante =int(eColor.verde)
            aux.duracion = 45

        elif nombre_enfermedad=="odontalgia":
            aux.color = eColor.verde
            aux.enfermedad = eEnfermedad.odontalgia
            aux.prioridad =4
            aux.tiempo_restante =int(eColor.verde)
            aux.duracion = 35

        elif nombre_enfermedad=="dolor_inespecifico_leve":
            aux.color = eColor.verde
            aux.enfermedad = eEnfermedad.dolor_inespecifico_leve
            aux.prioridad =3
            aux.tiempo_restante =int(eColor.verde)
            aux.duracion = 30

        elif nombre_enfermedad=="otalgias":
            aux.color = eColor.verde
            aux.enfermedad = eEnfermedad.otalgia
            aux.prioridad =4
            aux.tiempo_restante =int(eColor.verde)
            aux.duracion = 30

        elif nombre_enfermedad=="sincope":
            aux.color = eColor.amarillo
            aux.enfermedad = eEnfermedad.sincope
            aux.prioridad =9
            aux.tiempo_restante =int(eColor.amarillo)
            aux.duracion = 15

        elif nombre_enfermedad=="urgencia_psiquiatrica":
            aux.color = eColor.amarillo
            aux.enfermedad = eEnfermedad.urgencia_psiquiatrica
            aux.prioridad =6
            aux.tiempo_restante =int(eColor.amarillo)
            aux.duracion = 25

        else:#azul
            aux.color = eColor.azul
            aux.enfermedad = eEnfermedad.no_urgencia
            aux.prioridad =2
            aux.tiempo_restante =int(eColor.azul)
            aux.duracion = 5





        return enfermedad

    def comparar_sintomas(sintomas)->Node:
        if arbol_sintomas.right==null and arbol_sintomas.left==null: #hoja
            return arbol_sintomas
        else:
            return comparar_sintomas(sintomas, arbol_sintomas.left) if arbol_sintomas.value in sintomas else comparar_sintomas(sintomas, arbol_sintomas.right)




































































                .



















