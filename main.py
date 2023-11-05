import threading
import time
from datetime import datetime
from datetime import timedelta
from random import random

from library.classPriorityQueuePaciente import PriorityQueuePaciente
from library.classPaciente import cPaciente
from library.classEnfermero import cEnfermero
from library.classConsultorio import cConsultorio
from library.classHospital import cHospital
from src.archivos import leerPaciente
from src.archivos import leerEnfermero

hora_actual:datetime=datetime.now()
def main():
  #leemos los archivos
  lista_pacientes:list[cPaciente]=leerPaciente()
  lista_enfermeros:list[cEnfermero]=leerEnfermero()
  #inicializamos un consultorio
  consultorio=cConsultorio()
  #nos creamos un hospital
  hospital_NoboPecker=cHospital(consultorio,lista_pacientes,lista_enfermeros) #no hice mucho pero lo tengo
  #funciones que van a correr al mismo tiempo
  reloj=threading.Thread(target=horario()) #para achicar la escala de tiempo (1hora=1min, 1min=1seg)
  lista_ingresados:list[cPaciente]=[]
  ingreso_pac=threading.Thread(target=ingresar_pacientes(lista_pacientes,lista_ingresados))
  lista_enfermeros_activos:list[cEnfermero]=[]
  fila_urgencia=PriorityQueuePaciente()
  fila_no_urgencia=PriorityQueuePaciente()
  fin_del_dia:datetime=hora_actual+timedelta(hours=5)#para que termine el programa

  reloj.start()
  while hora_actual<=fin_del_dia:
    #segun el horario varia la cantidad de enfermeros activos
    if hora_actual.hour in range(6,9):
      lista_enfermeros_activos=[lista_enfermeros[0],lista_enfermeros[1]]

    elif hora_actual.hour in range(10,15):
      lista_enfermeros_activos=[lista_enfermeros[2],lista_enfermeros[3],lista_enfermeros[4],lista_enfermeros[5],lista_enfermeros[6]]

    elif hora_actual.hour in range(16,22):
      lista_enfermeros_activos=[lista_enfermeros[7],lista_enfermeros[8],lista_enfermeros[9]]

    else:
      lista_enfermeros_activos = [lista_enfermeros[10]]

    trabajo_enf = threading.Thread(target=trabajo_enfermeros(lista_enfermeros_activos, lista_ingresados, fila_urgencia, fila_no_urgencia))
    trabajo_enf.start()
    ingreso_pac.start()


  trabajo_enf.join()
  ingreso_pac.join()
  reloj.join()

def horario()->None:
  global hora_actual
  while True:
    hora_actual=hora_actual+timedelta(minutes=1)
    time.sleep(1)

def tiempo_restante(lista_pac:list[cPaciente])->None: #voy bajando el tiempo restante de espera de los pacientes que ya ingresaron
  global hora_actual
  while True:
    for i in range (len(lista_pac)):
      lista_pac[i].diagnostico.tiempo_restante=lista_pac[i].diagnostico.tiempo_restante - 1
    time.sleep(1)

def ingresar_pacientes(lista_pacientes_total:list[cPaciente],lista_ingresados:list[cPaciente])->None:
  #hay un 80% de probabilidad de que entren pacientes nuevos (cada 4 segundos o 6 si no ingresaron)
  probabilidad=int(random()*10)
  #entra una cantidad random de pacientes
  cantidad=int(random()*5 + 1)
  if probabilidad in range (0,8):
    for i in range (cantidad):
      num_pac=int(random()*(30-cantidad))
      lista_ingresados.append(lista_pacientes_total[num_pac+i])
      time.sleep(4)
  else:
    time.sleep(6)

def trabajo_enfermeros(lista_enfermeros:list[cEnfermero], lista_pacientes:list[cPaciente], fila_urgencia: PriorityQueuePaciente, fila_no_urgencia: PriorityQueuePaciente)->None:
  cont=0
  for i in range (0,len(lista_pacientes),len(lista_enfermeros)): #recorro la lista de pacientes (con paso cantidad de enfermeros activos, ya que por cada iteracion van a atender un paciente cada uno)
    cont=cont+1
    for j in range(len(lista_enfermeros)):
      lista_pacientes[i+j].diagnostico=lista_enfermeros[j].diagnosticar(lista_pacientes[i+j])
      if lista_pacientes[i+j].diagnostico.color=="rojo":
        cConsultorio.atender_urgencia(lista_pacientes[i+j])
      elif lista_pacientes[i+j].diagnostico.color in ["naranja","amarillo"]:
        fila_urgencia.push(lista_pacientes[i+j],lista_pacientes[i+j].diagnostico.prioridad)
      else:
        fila_no_urgencia.push(lista_pacientes[i+j], lista_pacientes[i+j].diagnostico.prioridad)
    if cont%3 == 0:#cada 3 iteraciones actualizo la prioridad de los pacientes en caso de que su tiempo de espera haya disminuido y "cambie de categoria"
      lista_enfermeros[0].chequear(fila_no_urgencia,fila_urgencia)



if __name__ == "__main__":
  main()
