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
  hospital_NoboPecker=cHospital(consultorio,lista_pacientes,lista_enfermeros)

  #funcion que simula el paso del tiempo
  reloj=threading.Thread(target=horario) #para achicar la escala de tiempo (1hora=1min, 1min=1seg)

  #auxiliares
  lista_enfermeros_activos:list[cEnfermero]=[]
  fila_urgencia=PriorityQueuePaciente()
  fila_no_urgencia=PriorityQueuePaciente()
  fin_del_dia:datetime=hora_actual+timedelta(hours=5)#para que termine el programa

  #empiezan a correr el reloj
  reloj.start()

  primera_vez:bool=True
  cambio_de_turno:bool=False
  turno_actual=""

  while hora_actual<=fin_del_dia:

    #segun el horario varia la cantidad de enfermeros activos
    if hora_actual.hour in range(6,9):
      if turno_actual=="nocturno":
        cambio_de_turno=True
      turno_actual="mañana"
      lista_enfermeros_activos=[lista_enfermeros[0],lista_enfermeros[1]]

    elif hora_actual.hour in range(10,15):
      if turno_actual=="mañana":
        cambio_de_turno=True
      turno_actual="hora_pico"
      lista_enfermeros_activos=[lista_enfermeros[2],lista_enfermeros[3],lista_enfermeros[4],lista_enfermeros[5],lista_enfermeros[6]]

    elif hora_actual.hour in range(16,22):
      if turno_actual=="hora_pico":
        cambio_de_turno=True
      turno_actual="tarde"
      lista_enfermeros_activos=[lista_enfermeros[7],lista_enfermeros[8],lista_enfermeros[9]]

    else:
      if turno_actual=="tarde":
        cambio_de_turno=True
      turno_actual="nocturno"
      lista_enfermeros_activos = [lista_enfermeros[10]]

    if primera_vez or cambio_de_turno:
      trabajo_enf = threading.Thread(target=trabajo_enfermeros, args=(lista_enfermeros_activos, lista_pacientes, fila_urgencia, fila_no_urgencia,consultorio))
      trabajo_enf.start()
      cambio_de_turno=False
      primera_vez=False


  trabajo_enf.join()
  reloj.join()

def horario()->None:
  global hora_actual
  while True:
    hora_actual=hora_actual+timedelta(minutes=1)
    time.sleep(1)

def tiempo_restante(lista_pac:list[cPaciente])->None: #voy bajando el tiempo restante de espera de los pacientes que ya ingresaron
  global hora_actual
  cambio=10 if int(random()*2)==1 else 1 #cada tanto restamos 10 en el tiempo restante para llegar al caso donde el paciente exceda su tiempo maximo de espera
  for i in range (len(lista_pac)):
    lista_pac[i].diagnostico.tiempo_restante=lista_pac[i].diagnostico.tiempo_restante - cambio
  time.sleep(1)

def ingresar_pacientes(lista_pacientes_total:list[cPaciente])->list[cPaciente]:

  lista_ingresados: list[cPaciente]=[]
  #hay un 80% de probabilidad de que entren pacientes nuevos (cada 4 segundos o 6 si no ingresaron)
  probabilidad=int(random()*10)
  #entra una cantidad random de pacientes
  cantidad=int(random()*5 + 5)
  if probabilidad in range (0,8):
    if cEnfermero.ultimo_paciente_ingresado+cantidad<64:
      num_pac=cEnfermero.ultimo_paciente_ingresado+1
      cEnfermero.ultimo_paciente_ingresado=num_pac+cantidad
    else:
      num_pac=0
      cEnfermero.ultimo_paciente_ingresado=cantidad

    for i in range (cantidad):
      lista_ingresados.append(lista_pacientes_total[num_pac+i])
  return lista_ingresados

def trabajo_enfermeros(lista_enfermeros:list[cEnfermero], lista_pacientes:list[cPaciente], fila_urgencia: PriorityQueuePaciente, fila_no_urgencia: PriorityQueuePaciente, consultorio: cConsultorio)->None:
  lista_ingresados = ingresar_pacientes(lista_pacientes)
  cont = 0
  while True:
    tiempo_restante(lista_ingresados)
    for i in range (0,len(lista_ingresados)-len(lista_enfermeros),len(lista_enfermeros)): #recorro la lista de pacientes (con paso cantidad de enfermeros activos, ya que por cada iteracion van a atender un paciente cada uno)
      cont=cont+1
      for j in range(len(lista_enfermeros)):
        lista_ingresados[i+j].diagnostico=lista_enfermeros[j].diagnosticar(lista_ingresados[i+j])
        if lista_ingresados[i+j].diagnostico.color=="rojo":
          cConsultorio.atender_urgencia(lista_ingresados[i+j])
        elif lista_ingresados[i+j].diagnostico.color in ["naranja","amarillo"]:
          fila_urgencia.push(lista_ingresados[i+j].diagnostico.prioridad,lista_ingresados[i+j])
        else:
          fila_no_urgencia.push(lista_ingresados[i+j].diagnostico.prioridad,lista_ingresados[i+j])
      if cont%3 == 0:#cada 3 iteraciones actualizo la prioridad de los pacientes en caso de que su tiempo de espera haya disminuido y "cambie de categoria"
        lista_enfermeros[0].chequear(fila_no_urgencia,fila_urgencia)
        consultorio.atender_G(fila_urgencia, fila_no_urgencia, 1)
        time.sleep(1) #para dejar pasar al menos 1 minuto para que ingresen mas pacientes
        lista_ingresados=lista_ingresados+ingresar_pacientes(lista_pacientes)




if __name__ == "__main__":
  main()
