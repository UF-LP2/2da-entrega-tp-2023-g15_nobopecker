import tkinter as tk
import random

class SistemaDeTriage:
    def __init__(self, root):

        self.ultimo_x_R = 0  # Posición x del último cuadrado agregado
        self.ultimo_x_NA = 0
        self.ultimo_x_VA = 0
        self.y = 0  # Posición y segun su color

        self.root = root
        self.root.title("Sistema de Triage")

        self.fila_urgencia = []
        self.fila_no_urgencia = []
        self.cont_pacientes = 0

        self.canvas = tk.Canvas(root, width=800, height=400, bg='white')
        self.canvas.pack()

        self.process_button = tk.Button(root, text="Atender Paciente", command=self.procesar_paciente)
        self.process_button.pack()
        self.chequear_fila_no_urgencia()
        self.generar_paciente()

    def generar_paciente(self):
        color_paciente = 'gray'
        prioridad = random.choice(['rojo', 'naranja', 'amarillo', 'verde', 'azul'])
        if prioridad == 'rojo':
            color_paciente = 'red'
            self.y=100
            self.ultimo_x_R=self.ultimo_x_R+50
            x=self.ultimo_x_R
        elif prioridad == 'naranja':
            color_paciente = 'orange'
            self.y=150
            self.ultimo_x_NA = self.ultimo_x_NA + 50
            x=self.ultimo_x_NA
        elif prioridad == 'amarillo':
            color_paciente = 'yellow'
            self.y=150
            self.ultimo_x_NA = self.ultimo_x_NA + 50
            x=self.ultimo_x_NA
        elif prioridad == 'verde':
            color_paciente = 'green'
            self.y=200
            self.ultimo_x_VA = self.ultimo_x_VA + 50
            x = self.ultimo_x_VA
        elif prioridad == 'azul':
            color_paciente = 'blue'
            self.y=200
            self.ultimo_x_VA = self.ultimo_x_VA + 50
            x=self.ultimo_x_VA


        # Crea el paciente en la nueva posición
        paciente_cuadrado = self.canvas.create_rectangle(x, self.y, x + 50, self.y + 50, fill=color_paciente)
        if prioridad in ['naranja', 'amarillo']:
            self.fila_urgencia.append(paciente_cuadrado)
        elif prioridad in ['verde', 'azul']:
            self.fila_no_urgencia.append(paciente_cuadrado)
        else:
            self.canvas.move(paciente_cuadrado, 0, 200)

        # Llama a la función para generar el próximo paciente después de 1000 milisegundos (1 segundo)
        self.root.after(1000, self.generar_paciente)

    def procesar_paciente(self):
        if self.fila_urgencia:
            patient = self.fila_urgencia.pop(0)
            self.canvas.move(patient, 0, 150)
            self.chequear_fila_no_urgencia()
        elif self.fila_no_urgencia:
            patient = self.fila_no_urgencia.pop(0)
            self.canvas.move(patient, 0, 100)

        self.generar_paciente()
        self.chequear_fila_no_urgencia()

    def chequear_fila_no_urgencia(self):
        if len(self.fila_urgencia) % 5 == 0 and self.fila_no_urgencia:
            patient = self.fila_no_urgencia.pop(0)
            self.canvas.move(patient, 150, 0)
            self.chequear_fila_no_urgencia()


if __name__ == "__main__":
    root = tk.Tk()
    triage_system = SistemaDeTriage(root)
    root.mainloop()
