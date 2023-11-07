[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LcojlfsQ)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12612322)
# G***15***_***Nobo******Pecker Fasce***_TP***1/2/../Final***
  La solucion planteada para el triage utiliza un algoritmo greedy que divide a los pacientes ingresados una vez obtenido su diagnostico en dos grupos:
    Grupo A: pacientes de codigo amarillo y naranja
    Grupo B: pacientes de codigo verde y azul
    (los pacientes de codigo rojo seran atendidos inmediatamente)
  Cada grupo se almacenará en una cola de prioridad según la gravedad de su condición y posibles factores de riesgo previos a la misma. Dichas filas se atenderán en una proporción 5:1, es decir que cada 5 pacientes de la fila de mayor urgencia (fila A) se atenderá uno de la de menor urgencia (fila B). Para evitar que alguno de los pacientes en las colas se exceda de su tiempo máximo de espera, un enfermero por turno revisará las colas cada un determinado tiempo y actualizará la prioridad según el tiempo restante de espera, de modo que si un paciente espera demasiado tiempo, avanzará en la fila a pesar de que su condición no tenga riesgo vital.
  

## Integrantes
- Nobo, Maria Agostina
- Pecker Fasce, Paula

## Objetivo del proyecto
La problematica del trabajo es una simulación para un sistema de atención en Triage de un Hospital, el objetivo principal es atender a todos los pacientes que ingresan minimizando el riesgo y evitando que se exceda el tiempo máximo de espera. De esta manera se logrará atender a todos los pacientes sin que la sala de espera se torne ociosa.
## Requisitos
Librerías utilizadas:
  BinaryTree: se generó un árbol de decisión para el diagnostico de los pacientes
  Pytest: se llevaron a cabo tests de los métodos de cada clase para corroborar su funcionammiento adecuado
  PriorityQueue: se usan dos colas de prioridad para almacenar los pacientes en espera divididos según gravedad
  Exceptiongroup: para las excepciones generadas en casos particulares a lo largo del programa 

---
##### UF-FICEN LP2 2023 - GNU General Public License v3.0
