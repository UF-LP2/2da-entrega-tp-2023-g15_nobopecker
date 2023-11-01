import time
from classPaciente import cPaciente
from classEnfermero import cEnfermero
class cConsultorio:

    def __init__(self, numero:int, paciente_actual: cPaciente ,ocupado = False):
        self.ocupado=ocupado
        self.numero=numero
        self.paciente_actual=paciente_actual

    def curar(self, paciente:cPaciente) -> None: #metodo de curar paciente
        paciente.estado= "sano"

    @staticmethod
    def atender_urgencia (paciente: cPaciente) ->None: #metodo de curar paciente static para atender urgencias sin importar consultorios libres
        paciente.estado= "sano"

    def atender_DC(self, lista:list[cPaciente], enfermero: cEnfermero)->None:
        if len(lista)==0: #caso base: no hay mas elementos en la lista
            return
        paciente:cPaciente=enfermero.elegir_paciente_optimo(lista) #elijo el paciente que maximiza prioridad/duracion
        lista.remove(paciente) #lo saco de la lista
        self.ocupado=True #el consultorio esta ocupado hasta que termino de atenderlo
        cConsultorio.curar(self, paciente)
        time.sleep(paciente.diagnostico.duracion) #detengo el programa la duracion de la consulta
        self.ocupado = False #desocupo el consultorio
        cConsultorio.atender_DC(self, lista, enfermero) #sigo atendiendo la lista

    def atender_G(self, filaA, filaB, contador:int )->None:
        if len(filaA)==0 and len(filaB)==0: #caso base: no hay elementos en las filas
            #lanzar excepcion "filas vacias"
            return
        if contador%5==0: #para respetar proporcion 5:1, si es multiplo de 5 atiendo a la fila B
            fila=filaB
            suma=1
        else: #sino, atiendo a la fila A
            fila=filaA
            suma=5-(contador%5)
        if len(fila)==0: #si la lista en la q estoy parada esta vacia, sigo con la otra
            contador=contador+suma
            cConsultorio.atender_G(self,filaA,filaB, contador)

        paciente=fila[0] #paciente q voy a atender es el primero en la priority queue
        fila.dequeue() #lo saco de la fila
        self.ocupado=True #atiendo
        cConsultorio.curar(self,paciente)
        time.sleep(paciente.diagnostico.duracion)
        self.ocupado=False
        cConsultorio.atender_G(self,filaA,filaB, contador+1) #sigo con el proximo





