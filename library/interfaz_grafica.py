import tkinter as tk
import random

class SistemaDeTriage:

    # static de proporcion:
    cont = 1

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

        # Agrega texto en la parte superior
        self.ingreso_label = tk.Label(root, text="Ingreso de Pacientes", font=("Arial", 14))
        self.ingreso_label.pack()

        self.canvas = tk.Canvas(root, width=800, height=400, bg='white')
        self.canvas.pack()

        # Agrega texto en la parte inferior
        self.atencion_label = tk.Label(root, text="Atención de Pacientes", font=("Arial", 14))
        self.atencion_label.pack()

        self.process_button = tk.Button(root, text="Atender Paciente", command=self.procesar_paciente)
        self.process_button.pack()
        self.generar_paciente()

        self.reiniciar_button = tk.Button(root, text="Reiniciar Simulación", command=self.reiniciar_simulacion)
        self.reiniciar_button.pack()
        self.generar_paciente()

    def generar_paciente(self):
        color_paciente = 'gray'
        x=0
        prioridad = random.choice(['rojo', 'naranja', 'amarillo', 'verde', 'azul'])
        if prioridad == 'rojo':
            color_paciente = 'red'
            self.y=0
            self.ultimo_x_R=self.ultimo_x_R+50
            x=self.ultimo_x_R
        elif prioridad == 'naranja':
            color_paciente = 'orange'
            self.y=50
            self.ultimo_x_NA = self.ultimo_x_NA + 50
            x=self.ultimo_x_NA
        elif prioridad == 'amarillo':
            color_paciente = 'yellow'
            self.y=50
            self.ultimo_x_NA = self.ultimo_x_NA + 50
            x=self.ultimo_x_NA
        elif prioridad == 'verde':
            color_paciente = 'green'
            self.y=100
            self.ultimo_x_VA = self.ultimo_x_VA + 50
            x = self.ultimo_x_VA
        elif prioridad == 'azul':
            color_paciente = 'blue'
            self.y=100
            self.ultimo_x_VA = self.ultimo_x_VA + 50
            x=self.ultimo_x_VA


        # Crea el paciente en la nueva posición
        paciente_cuadrado = self.canvas.create_rectangle(x, self.y, x + 20, self.y + 20, fill=color_paciente)
        if prioridad in ['naranja', 'amarillo']:
            self.fila_urgencia.append(paciente_cuadrado)
        elif prioridad in ['verde', 'azul']:
            self.fila_no_urgencia.append(paciente_cuadrado)
        else:
            self.canvas.move(paciente_cuadrado, 0, 200)

        # Llama a la función para generar el próximo paciente después de 1000 milisegundos (1 segundos)
        self.root.after(1000, self.generar_paciente)

    def reiniciar_simulacion(self):

        self.ultimo_x_R = 0  # Posición x del último cuadrado agregado
        self.ultimo_x_NA = 0
        self.ultimo_x_VA = 0
        self.y = 0  # Posición y segun su color

        # Limpiar listas de pacientes
        self.fila_urgencia = []
        self.fila_no_urgencia = []

        # Borrar todos los elementos del lienzo
        self.canvas.delete("all")

        # Volver a generar pacientes
        self.generar_paciente()

    def procesar_paciente(self):
        if self.fila_urgencia and not SistemaDeTriage.cont%3==0:
            patient = self.fila_urgencia.pop(0)
            self.canvas.move(patient, 0, 200)
        elif self.fila_no_urgencia and SistemaDeTriage.cont%3==0:
            patient = self.fila_no_urgencia.pop(0)
            self.canvas.move(patient, 0, 200)
        self.generar_paciente()
        SistemaDeTriage.cont+=1


if __name__ == "__main__":
    root = tk.Tk()
    triage_system = SistemaDeTriage(root)
    root.mainloop()
