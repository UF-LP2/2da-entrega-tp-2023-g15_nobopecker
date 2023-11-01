import csv
from classPaciente import cPaciente
from classEnfermero import cEnfermero
from classEnfermedad import cEnfermedad

def leerPaciente() -> list[cPaciente]:
    pacientes: list[cPaciente]=[]
    dummy=cEnfermedad("indefinido",0,"indefinido",0,0 )
    with open("PACIENTES.csv") as file:
        reader=csv.reader(file)
        next(file)
        for row in reader:
            #hay q hacer la conversion de factor de riesgo a str y viceversa, lo mismo para sintomas
            #a los sintomas los pongo en la misma columna separados por guiones y desp uso split -
            paciente_aux=cPaciente(row[0],dummy,row[1],row[2],"enfermo")
            pacientes.append(paciente_aux)
    return pacientes

def leerEnfermero() -> list[cEnfermero]: #para mi es al pedo, el ID lo puedo generar con un random y listo, no tienen por q ser los mismos q ayer
    enfermeros:list[cEnfermero]=[]
    with open("ENFERMEROS.csv") as file:
        reader=csv.reader(file)
        next(file)
        for row in reader:
            enfermero_aux=cEnfermero(row[0])
            enfermeros.append(enfermero_aux)
    return enfermeros