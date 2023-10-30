from classPaciente import  cPaciente
from classEnfermedad import cEnfermedad
from enums import eSintomas
from enums import eEnfermedad
from enums import eColor
from binarytree import Node
from bt_sintomas import arbol_sintomas

class cEnfermero:

    def __init__(self, ID, turno):
        self.ID=ID
        self.turno=turno

    @staticmethod
    def diagnosticar(paciente:cPaciente)-> cEnfermedad:
       return cEnfermero.definir_enfermedad(paciente.sintomas)

    @staticmethod
    def definir_enfermedad(sintomas:eSintomas)->cEnfermedad:
        nodo_enfermedad= cEnfermero.comparar_sintomas(sintomas, arbol_sintomas())
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

        return aux

    @staticmethod
    def comparar_sintomas(sintomas, arbol_sintomas)->Node:
        if arbol_sintomas.right==None and arbol_sintomas.left==None: #hoja
            return arbol_sintomas
        else:
            return cEnfermero.comparar_sintomas(sintomas, arbol_sintomas.left) if arbol_sintomas.value in sintomas else cEnfermero.comparar_sintomas(sintomas, arbol_sintomas.right)

    @staticmethod
    def elegir_paciente_optimo(lista:list[cPaciente])->cPaciente:
        if len(lista)==1:
            return lista
        elif len(lista)==2:
            aux1=(lista[0].diagnostico.prioridad + lista[0].factor_riesgo)/lista[0].diagnostico.duracion
            aux2 = (lista[1].diagnostico.prioridad + lista[1].factor_riesgo) / lista[1].diagnostico.duracion

            return lista[0] if aux1>aux2 else lista[1]
        else:
            optimo_primera_mitad=cEnfermero.elegir_paciente_optimo(lista[:len(lista)/2])
            optimo_seguda_mitad=cEnfermero.elegir_paciente_optimo(lista[len(lista)/2:])
            nueva_lista:list[cPaciente]=[optimo_primera_mitad,optimo_seguda_mitad]
            return cEnfermero.elegir_paciente_optimo(nueva_lista)










            return
