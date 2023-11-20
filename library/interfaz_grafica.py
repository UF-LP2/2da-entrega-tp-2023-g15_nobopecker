import tkinter as tk
import time
import random

class Paciente:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = "gray"
        self.diagnostico = ""
        self.fila = None
        self.cuadrado = self.canvas.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill=self.color)


    def diagnosticar(self):
        self.diagnostico = random.choice(["red", "orange", "yellow", "green", "blue"])
        self.canvas.itemconfig(self.cuadrado, fill=self.diagnostico)
        if self.diagnostico in ["orange", "yellow"]:
            self.fila = "urgencia"
        elif self.diagnostico in ['green', 'blue']:
            self.fila="no urgencia"
        else:
            self.fila="atencion directa"

    def eliminar(self):
        self.canvas.delete(self.cuadrado)


class SistemaDeTriage:

    # static de proporcion:
    cont = 1

    def __init__(self, root):

        self.ultimo_x_R = 0  # posición x del último cuadrado agregado
        self.ultimo_x_NA = 0
        self.ultimo_x_VA = 0
        self.y = 0  # posición y segun su color

        self.root = root
        self.root.title("Sistema de Triage")

        self.fila_urgencia = []
        self.fila_no_urgencia = []
        self.cont_pacientes = 0
        self.tiempo = 0

        #pantalla en blanco
        self.canvas = tk.Canvas(root, width=1000, height=600, bg='white')
        self.canvas.pack()

        #texto en la parte de arriba
        self.ingreso_label = tk.Label(root, text="Ingreso de Pacientes", font=("Arial", 14))
        self.ingreso_label.pack(side="top", pady=10)

        #para centrarlo
        window_width = self.root.winfo_reqwidth()
        label_width = self.ingreso_label.winfo_reqwidth()
        x = (window_width - label_width) // 2
        self.ingreso_label.place(x=x, y=0)

        #simulacion de ingreso de pacientes
        self.pacientes = []
        self.simular_ingreso_pacientes()

        #reloj
        self.reloj=tk.Label(root, text="", font=("Arial", 14))
        self.reloj.pack()
        self.reloj.place(x=800, y=0)
        self.actualizar_reloj()

        #botones y titulos
        self.atencion_label = tk.Label(root, text="Atención de Pacientes", font=("Arial", 14))
        self.atencion_label.pack()

        self.process_button = tk.Button(root, text="Atender Paciente", command=self.procesar_paciente)
        self.process_button.pack(pady=10)
        self.generar_paciente()

        self.reiniciar_button = tk.Button(root, text="Reiniciar Simulación", command=self.reiniciar_simulacion)
        self.reiniciar_button.pack()
        self.generar_paciente()


    def simular_ingreso_pacientes(self):
        x = 10
        y= 50
        for _ in range(5):  # simular 15 pacientes ingresando
            paciente = Paciente(self.canvas, x, y)
            self.pacientes.append(paciente)
            x += 40
            self.root.update()
            time.sleep(1)
            self.root.update()

        for paciente in self.pacientes:
            paciente.diagnosticar()
            paciente.eliminar()

        self.ingreso_label.config(text="Sala de Espera")

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


        # crea el paciente en la nueva posición
        paciente_cuadrado = self.canvas.create_rectangle(x, self.y, x + 20, self.y + 20, fill=color_paciente)
        if prioridad in ['naranja', 'amarillo']:
            self.fila_urgencia.append(paciente_cuadrado)
        elif prioridad in ['verde', 'azul']:
            self.fila_no_urgencia.append(paciente_cuadrado)
        else:
            self.canvas.move(paciente_cuadrado, 0, 200)

        self.tiempo += 1
        self.actualizar_reloj()

        #llama a la función para generar el próximo paciente después de 1500 milisegundos (1,5 segundos)
        self.root.after(1500, self.generar_paciente)

    def actualizar_reloj(self):
        #obtener la hora actual en el formato HH:MM:SS
        hora_actual = time.strftime("%H:%M:%S")
        self.reloj.config(text="Hora: {}".format(hora_actual))

    def reiniciar_simulacion(self): #de nuevo

        self.ultimo_x_R = 0
        self.ultimo_x_NA = 0
        self.ultimo_x_VA = 0
        self.y = 0

        #limpiar listas de pacientes
        self.fila_urgencia = []
        self.fila_no_urgencia = []

        #borrar todos los elementos de la pantalla
        self.canvas.delete("all")

        #volver a generar pacientes
        self.generar_paciente()

    def procesar_paciente(self):
        if self.fila_urgencia and not SistemaDeTriage.cont%3==0:
            patient = self.fila_urgencia.pop(0)
            self.canvas.move(patient, 0, 200)
        elif self.fila_no_urgencia and SistemaDeTriage.cont%3==0:
            patient = self.fila_no_urgencia.pop(0)
            self.canvas.move(patient, 0, 200)
        #self.generar_paciente()
        SistemaDeTriage.cont+=1


if __name__ == "__main__":
    root = tk.Tk()
    triage_system = SistemaDeTriage(root)
    root.mainloop()
