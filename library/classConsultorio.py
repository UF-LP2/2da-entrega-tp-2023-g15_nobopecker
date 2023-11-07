import time
from library.classPaciente import cPaciente
from library.classEnfermero import cEnfermero
from library.classPriorityQueuePaciente import PriorityQueuePaciente
class cConsultorio:

    def __init__(self, ocupado = False):
        self.consultorio=ocupado

    def curar(self, paciente:cPaciente) -> None: #metodo de curar paciente
        if  paciente.diagnostico.tiempo_restante > 0:
            paciente.estado = "sano"
            print("Paciente: ", paciente.nombre_apellido, " de color ", paciente.diagnostico.color, " curado :)")
        else:# se canso y se fue
            paciente.estado = "enfermo"
            print("El paciente: ", paciente.nombre_apellido, " ha abandonado la sala de espera :|")
        return


    @staticmethod
    def atender_urgencia (paciente: cPaciente) ->None: #metodo de curar paciente static para atender urgencias sin importar consultorios libres
        if paciente.diagnostico.tiempo_restante>0:
           paciente.estado= "sano"
           print("Paciente: ", paciente.nombre_apellido, " de color ", paciente.diagnostico.color, " curado :)")
        else:#fallecio
            paciente.estado="muerto"
            print("El paciente: ", paciente.nombre_apellido," ha fallecido :(")
        return

    def atender_DC(self, lista:list[cPaciente], enfermero: cEnfermero)->None:
        if len(lista)==0: #caso base: no hay mas elementos en la lista
            return
        paciente:cPaciente=enfermero.elegir_paciente_optimo(lista) #elijo el paciente que maximiza prioridad/duracion
        lista.remove(paciente) #lo saco de la lista
        self.ocupado=True #el consultorio esta ocupado hasta que termino de atenderlo
        cConsultorio.curar(self, paciente)
        time.sleep(paciente.diagnostico.duracion/100) #detengo el programa la duracion de la consulta
        self.ocupado = False #desocupo el consultorio
        cConsultorio.atender_DC(self, lista, enfermero) #sigo atendiendo la lista

    def atender_G(self, filaA:PriorityQueuePaciente, filaB:PriorityQueuePaciente, contador:int )->None:
        if filaA.is_empty() and filaB.is_empty(): #caso base: no hay elementos en las filas
            return
        if contador%5==0: #para respetar proporcion 5:1, si es multiplo de 5 atiendo a la fila B
            fila=filaB
            suma=1
        else: #sino, atiendo a la fila A
            fila=filaA
            suma=5-(contador%5)
        if fila.is_empty(): #si la lista en la q estoy parada esta vacia, sigo con la otra
            contador=contador+suma
            cConsultorio.atender_G(self,filaA,filaB, contador)
        else:
            paciente=fila.pop() #paciente q voy a atender es el primero en la priority queue y lo saco de la fila
            self.ocupado=True #atiendo
            cConsultorio.curar(self,paciente)
            time.sleep(paciente.diagnostico.duracion/100)
            self.ocupado=False
            cConsultorio.atender_G(self,filaA,filaB, contador+1) #sigo con el proximo





