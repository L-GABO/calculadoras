import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from sympy import *

class Calcular:
    def __init__(self):
        self.x, self.y, self.z = symbols('x y z')
        self.f = self.x * self.y * self.z

    def peso(self, area, longitud, densidad):
        weight = area * longitud * densidad
        return weight

    def primera_derivada(self, weight):
        change_reason = diff(self.f, self.x).subs({self.x: weight})
        return change_reason

    def funcion_peso(self, x, change_reason):
        return change_reason * x

    

class interfaz:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("optimizacion peso")
        self.calcular = Calcular()

        self.longitud_label = tk.Label(self.window, text="Longitud (m):")
        self.longitud_label.pack()
        self.longitud_entry = tk.Entry(self.window)
        self.longitud_entry.pack()

        self.densidad_label = tk.Label(self.window, text="Densidad (kg/m^3):")
        self.densidad_label.pack()
        self.densidad_entry = tk.Entry(self.window)
        self.densidad_entry.pack()

        self.grosor_label = tk.Label(self.window, text="grosor")
        self.grosor_label.pack()
        self.grosor_entry = tk.Entry(self.window)
        self.grosor_entry.pack()

        self.ancho_label = tk.Label(self.window, text="ancho")
        self.ancho_label.pack()
        self.ancho_entry = tk.Entry(self.window)
        self.ancho_entry.pack()

        self.area_result_label = tk.Label(self.window, text="Area (m^2):")
        self.area_result_label.pack()

        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(self.window, text="Result:")
        self.result_label.pack()

    def calculate(self):
        try:
            longitud = float(self.longitud_entry.get())
            densidad = float(self.densidad_entry.get())
            grosor = float(self.grosor_entry.get())
            ancho = float(self.ancho_entry.get())

            area = grosor * ancho
            weight = self.calcular.peso(area, longitud, densidad)
            change_reason = self.calcular.primera_derivada(weight)
            change_reason_func = lambdify('x', change_reason)

            x_values = np.linspace(0, 10, 10)  # area values
            y_values = [self.calcular.funcion_peso(x, change_reason).evalf() for x in x_values]

            plt.plot(x_values, y_values)
            plt.xlabel('grosor * ancho (m^2)')
            plt.ylabel('Weight (kg)')
            plt.title('Weight vs. Area')
            plt.grid(True)
            plt.show()

            self.result_label['text'] = f"peso: {weight} kg\n"
            self.result_label['text'] += f"primera derivada: {change_reason}\n"
            self.area_result_label['text'] = f"area: {area}"

        except ValueError:
            self.result_label['text'] = "Error: Invalid input"

    def run(self):
        self.window.mainloop()

def main():
        Calcular()
        interfaz().run()

if __name__ == "__main__":
    main()