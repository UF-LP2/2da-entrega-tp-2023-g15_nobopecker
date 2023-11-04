import threading
import time
from datetime import datetime
from datetime import timedelta
from random import random
from queue import PriorityQueue

from library.classPaciente import cPaciente
from library.classEnfermedad import cEnfermedad
from library.classEnfermero import cEnfermero
from library.classConsultorio import cConsultorio
from library.classHospital import cHospital
from library.bt_sintomas import arbol_sintomas
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
  reloj=threading.Thread(target=horario())
  lista_ingresados:list[cPaciente]=[]
  ingreso_pac=threading.Thread(target=ingresar_pacientes(lista_pacientes,lista_ingresados))
  lista_enfermeros_activos:list[cEnfermero]=[]
  reloj.start()
  ingreso_pac.start()
  if hora_actual.hour in range(6,9):
    lista_enfermeros_activos=[lista_enfermeros[0],lista_enfermeros[1]]

  elif hora_actual.hour in range(10,15):
    lista_enfermeros_activos=[lista_enfermeros[2],lista_enfermeros[3],lista_enfermeros[4],lista_enfermeros[5],lista_enfermeros[6]]

  elif hora_actual.hour in range(16,22):
    lista_enfermeros_activos=[lista_enfermeros[7],lista_enfermeros[8],lista_enfermeros[9]]

  else:
    lista_enfermeros_activos = [lista_enfermeros[10]]

  ingreso_pac.join()
  reloj.join()

def horario()->None:
  global hora_actual
  while True:
    hora_actual=hora_actual+timedelta(minutes=1)
    time.sleep(1)

def tiempo_restante(lista_pac:list[cPaciente])->None:
  global hora_actual
  while True:
    for i in range (len(lista_pac)):
      lista_pac[i].diagnostico.tiempo_restante=lista_pac[i].diagnostico.tiempo_restante - 1
    time.sleep(1)

def ingresar_pacientes(lista_pacientes_total:list[cPaciente],lista_ingresados:list[cPaciente])->None:
  probabilidad=int(random()*10)
  cantidad=int(random()*5 + 1)
  if probabilidad in range (0,8):
    for i in range (cantidad):
      num_pac=int(random()*(30-cantidad))
      lista_ingresados.append(lista_pacientes_total[num_pac+i])
      time.sleep(4)
  else:
    time.sleep(6)

def trabajo_enfermeros(lista_enfermeros:list[cEnfermero], lista_pacientes:list[cPaciente], fila_urgencia: PriorityQueue, fila_no_urgencia: PriorityQueue)->None:
  cont=0
  for i in range (0,len(lista_pacientes),len(lista_enfermeros)):
    cont=cont+1
    for j in range(len(lista_enfermeros)):
      lista_pacientes[i+j].diagnostico=lista_enfermeros[j].diagnosticar(lista_pacientes[i+j])
      if lista_pacientes[i+j].diagnostico.color=="rojo":
        cConsultorio.atender_urgencia(lista_pacientes[i+j])
      elif lista_pacientes[i+j].diagnostico.color in ["naranja","amarillo"]:
        fila_urgencia.put(lista_pacientes[i+j].diagnostico.prioridad,lista_pacientes[i+j])
      else:
        fila_no_urgencia.put(lista_pacientes[i+j].diagnostico.prioridad, lista_pacientes[i+j])
    if cont%3 == 0:
      lista_enfermeros[0].chequear(fila_no_urgencia,fila_urgencia)



if __name__ == "__main__":
  main()
