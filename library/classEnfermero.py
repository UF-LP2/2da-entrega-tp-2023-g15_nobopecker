from library.classPaciente import cPaciente
from library.classEnfermedad import cEnfermedad
from library.classNodos import Nodo
from library.bt_sintomas import arbol_sintomas
from library.classPriorityQueuePaciente import PriorityQueuePaciente

class cEnfermero:

    #statics:
    #tiempo maximo de espera segun color
    tmax_rojo=0
    tmax_naraja=10
    tmax_amarillo=60
    tmax_verde=120
    tmax_azul=240
    ultimo_paciente_ingresado=-1


    def __init__(self,ID, nombre_apellido:str):
        self.ID=ID
        self.nombre_apellido=nombre_apellido

    def diagnosticar(self, paciente:cPaciente)->cEnfermedad:
        enfermedad=cEnfermero.definir_enfermedad(self, paciente.sintomas)
        valor_fr=(cEnfermedad.convert_fr(paciente.factor_riesgo))
        paciente.diagnostico.prioridad=enfermedad.prioridad+valor_fr
        return enfermedad

    def definir_enfermedad(self, sintomas:list[str])->cEnfermedad:
        nodo_enfermedad= cEnfermero.comparar_sintomas(self, sintomas, arbol_sintomas())
        nombre_enfermedad=nodo_enfermedad.name
        #inicializo una enfermedad cualquiera y despues tapo los datos con lo que me devuelve el arbol
        aux=cEnfermedad("indefinido", 0, "indefinido", 0,0)

        if nombre_enfermedad=="politraumatismo_grave":
            aux.color="rojo"
            aux.enfermedad="politraumatismo_grave"
            aux.prioridad=100
            aux.tiempo_restante=cEnfermero.tmax_rojo
            aux.duracion=5

        elif nombre_enfermedad=="isquemia":
            aux.color = "naranja"
            aux.enfermedad = "isquemia"
            aux.prioridad =10
            aux.tiempo_restante =cEnfermero.tmax_naraja
            aux.duracion = 20

        elif nombre_enfermedad=="convulsiones":
            aux.color = "naranja"
            aux.enfermedad = "convulsiones"
            aux.prioridad =15
            aux.tiempo_restante =cEnfermero.tmax_naraja
            aux.duracion = 10

        elif nombre_enfermedad=="coma":
            aux.color = "naranja"
            aux.enfermedad = "coma"
            aux.prioridad =10
            aux.tiempo_restante =cEnfermero.tmax_naraja
            aux.duracion = 10

        elif nombre_enfermedad=="hemorragia_digestiva":
            aux.color = "naranja"
            aux.enfermedad = "hemorragia_digestiva"
            aux.prioridad =10
            aux.tiempo_restante =cEnfermero.tmax_naraja
            aux.duracion = 12

        elif nombre_enfermedad=="hipertension_arterial":
            aux.color = "amarillo"
            aux.enfermedad = "hipertension_arterial"
            aux.prioridad =7
            aux.tiempo_restante =cEnfermero.tmax_amarillo
            aux.duracion = 20

        elif nombre_enfermedad=="vertigo":
            aux.color = "amarillo"
            aux.enfermedad = "vertigo"
            aux.prioridad =7
            aux.tiempo_restante =cEnfermero.tmax_amarillo
            aux.duracion = 15

        elif nombre_enfermedad=="cefalea_brusca":
            aux.color = "amarillo"
            aux.enfermedad = "cefalea_brusca"
            aux.prioridad =8
            aux.tiempo_restante =cEnfermero.tmax_amarillo
            aux.duracion = 15

        elif nombre_enfermedad=="paresia":
            aux.color = "amarillo"
            aux.enfermedad = "paresia"
            aux.prioridad =8
            aux.tiempo_restante =cEnfermero.tmax_amarillo
            aux.duracion = 25

        elif nombre_enfermedad =="esguince":
            aux.color = "verde"
            aux.enfermedad = "esguince"
            aux.prioridad =5
            aux.tiempo_restante =cEnfermero.tmax_verde
            aux.duracion = 45

        elif nombre_enfermedad=="odontalgia":
            aux.color = "verde"
            aux.enfermedad = "odontalgia"
            aux.prioridad =4
            aux.tiempo_restante =cEnfermero.tmax_verde
            aux.duracion = 35

        elif nombre_enfermedad=="dolor_inespecifico_leve":
            aux.color = "verde"
            aux.enfermedad = "dolor_inespecifico_leve"
            aux.prioridad =3
            aux.tiempo_restante =cEnfermero.tmax_verde
            aux.duracion = 30

        elif nombre_enfermedad=="otalgias":
            aux.color = "verde"
            aux.enfermedad = "otalgia"
            aux.prioridad =4
            aux.tiempo_restante =cEnfermero.tmax_verde
            aux.duracion = 30

        elif nombre_enfermedad=="sincope":
            aux.color = "amarillo"
            aux.enfermedad = "sincope"
            aux.prioridad =9
            aux.tiempo_restante =cEnfermero.tmax_amarillo
            aux.duracion = 15

        elif nombre_enfermedad=="urgencia_psiquiatrica_e":
            aux.color = "amarillo"
            aux.enfermedad = "urgencia_psiquiatrica_e"
            aux.prioridad =6
            aux.tiempo_restante =cEnfermero.tmax_amarillo
            aux.duracion = 25

        else:#azul
            aux.color = "azul"
            aux.enfermedad = "no_urgencia"
            aux.prioridad =2
            aux.tiempo_restante =cEnfermero.tmax_azul
            aux.duracion = 5

        return aux
    def comparar_sintomas(self, sintomas: list[str], arbol_sintomas)->Nodo:
        if arbol_sintomas.right==None and arbol_sintomas.left==None: #hoja
            return arbol_sintomas
        else:
            return cEnfermero.comparar_sintomas(self, sintomas, arbol_sintomas.left) if arbol_sintomas.name in sintomas else cEnfermero.comparar_sintomas(self, sintomas, arbol_sintomas.right)

    def elegir_paciente_optimo(self, lista:list[cPaciente])-> cPaciente:
        if len(lista)==1:
            return lista[0]
        elif len(lista)==2:
            aux1=lista[0].diagnostico.prioridad/lista[0].diagnostico.duracion
            aux2 =lista[1].diagnostico.prioridad/lista[1].diagnostico.duracion

            return lista[0] if aux1>aux2 else lista[1]
        else:
            optimo_primera_mitad=cEnfermero.elegir_paciente_optimo(self, lista[:(int)(len(lista)/2)])
            optimo_seguda_mitad=cEnfermero.elegir_paciente_optimo(self, lista[(int)(len(lista)/2):])
            nueva_lista:list[cPaciente]=[optimo_primera_mitad,optimo_seguda_mitad]
            return cEnfermero.elegir_paciente_optimo(self, nueva_lista)



    def chequear(self, filaA: PriorityQueuePaciente, filaB: PriorityQueuePaciente)-> None:
        filaA_aux=PriorityQueuePaciente()
        filaB_aux = PriorityQueuePaciente()

        i=0
        while not filaA.is_empty():
            pac_aux:cPaciente=filaA.pop()
            valor_fr=cEnfermedad.convert_fr(pac_aux.factor_riesgo)
            if pac_aux.diagnostico.tiempo_restante<=2:
                pac_aux.diagnostico.prioridad=100 #asignamos prioridad de rojo para que se lo atienda urgentemente
            elif pac_aux.diagnostico.tiempo_restante<=10: #si el tiempo restante es menor al tiempo maximo de espera naranja, cambiamos la prioridad a la minima del grupo naranja + factor de riesgo
                pac_aux.diagnostico.prioridad= 10 + valor_fr
            filaA_aux.push(pac_aux.diagnostico.prioridad, pac_aux)
            i = i + 1

        while not filaA_aux.is_empty():
            aux:cPaciente=filaA_aux.pop()
            filaA.push(aux.diagnostico.prioridad, aux)

        j = 0
        while not filaB.is_empty():
            pac_aux:cPaciente=filaB.pop()
            valor_fr = cEnfermedad.convert_fr(pac_aux.factor_riesgo)
            if pac_aux.diagnostico.tiempo_restante<=60: #mismo para amarillo
                pac_aux.diagnostico.prioridad = 6 + valor_fr
            elif pac_aux.diagnostico.tiempo_restante<=120: #mismo para verde
                pac_aux.diagnostico.prioridad = 3 + valor_fr
            filaB_aux.push(pac_aux.diagnostico.prioridad,pac_aux)
            j = j + 1

        while not filaB_aux.is_empty():
            aux: cPaciente = filaB_aux.pop()
            filaB.push(aux.diagnostico.prioridad, aux)

