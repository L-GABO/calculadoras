import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from sympy import *

class CalculatorInterface:
    #textos en terminologia
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("optimizacion peso")

        self.area_label = tk.Label(self.window, text="Area (m^2):")
        self.area_label.pack()
        self.area_entry = tk.Entry(self.window)
        self.area_entry.pack()

        self.longitud_label = tk.Label(self.window, text="Longitud (m):")
        self.longitud_label.pack()
        self.longitud_entry = tk.Entry(self.window)
        self.longitud_entry.pack()

        self.densidad_label = tk.Label(self.window, text="Densidad (kg/m^3):")
        self.densidad_label.pack()
        self.densidad_entry = tk.Entry(self.window)
        self.densidad_entry.pack()

        self.cedula_label = tk.Label(self.window, text="cedula")
        self.cedula_label.pack()
        self.cedula_entry = tk.Entry(self.window)
        self.cedula_entry.pack()

        # Crear boton de calcular
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        # Crear texto resultado
        self.result_label = tk.Label(self.window, text="Result:")
        self.result_label.pack()

    def calculate(self):
        try:
            area = float(self.area_entry.get())
            longitud = float(self.longitud_entry.get())
            densidad = float(self.densidad_entry.get())

            # Calcular peso
            weight = area * longitud * densidad

            # Define the variables as sympy symbols
            x, y, z = symbols('x y z')

            # Define the function to calculate the weight
            f = x * y * z

            # Calculate the first derivative
            change_reason = diff(f, x).subs({x: area, y: longitud, z: densidad}) + \
                            diff(f, y).subs({x: area, y: longitud, z: densidad}) + \
                            diff(f, z).subs({x: area, y: longitud, z: densidad})

            # Calculate the second derivative
            change_reason_above = diff(diff(f, x), x).subs({x: area, y: longitud, z: densidad}) + \
                                diff(diff(f, y), y).subs({x: area, y: longitud, z: densidad}) + \
                                diff(diff(f, z), z).subs({x: area, y: longitud, z: densidad})

            
            # Create a function for the graphic
            def weight_function(x):
                return change_reason * x + area * longitud * densidad

            # Create a 2D plot of weight vs. area
            x_values = np.linspace(0, 10, 10)  # area values
            y_values = [weight_function(x) for x in x_values]

            plt.plot(x_values, y_values)
            plt.xlabel('Area (m^2)')
            plt.ylabel('Weight (kg)')
            plt.title('Weight vs. Area')
            plt.grid(True)
            plt.show()

            # Mostrar resultados
            self.result_label['text'] = f"peso: {weight} kg\n"
            self.result_label['text'] += f"primera derivada: {change_reason}\n"
            self.result_label['text'] += f"segunda derivada: {change_reason_above}\n"

        except ValueError:
            self.result_label['text'] = "Error: Invalid input"

    def run(self):
        self.window.mainloop()

# funcion main
def main():
    CalculatorInterface().run()

if __name__ == "__main__":
    main()