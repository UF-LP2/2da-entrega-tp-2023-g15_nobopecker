import csv
from library.classPaciente import cPaciente
from library.classEnfermero import cEnfermero
from library.classEnfermedad import cEnfermedad

def leerPaciente() -> list[cPaciente]:
    pacientes: list[cPaciente]=[]
    dummy=cEnfermedad("indefinido",0,"indefinido",0,0 )
    with open("PACIENTES.csv") as file:
        reader=csv.reader(file)
        next(file)
        for row in reader:
            lista_sintomas=row[2].split()
            paciente_aux=cPaciente(row[0],row[1],dummy,row[2],lista_sintomas,"enfermo")
            pacientes.append(paciente_aux)
    return pacientes

def leerEnfermero() -> list[cEnfermero]: #para mi es al pedo, el ID lo puedo generar con un random y listo, no tienen por q ser los mismos q ayer
    enfermeros:list[cEnfermero]=[]
    with open("ENFERMEROS.csv") as file:
        reader=csv.reader(file)
        next(file)
        for row in reader:
            enfermero_aux=cEnfermero(row[0], row[1])
            enfermeros.append(enfermero_aux)
    return enfermeros