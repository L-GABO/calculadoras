import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from sympy import *

class CalculatorInterface:
    #textos en terminologia
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("optimizacion peso")

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

        # Crear boton de calcular
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        # Crear texto resultado
        self.result_label = tk.Label(self.window, text="Result:")
        self.result_label.pack()

    def calculate(self):
        try:
            longitud = float(self.longitud_entry.get())
            densidad = float(self.densidad_entry.get())
            grosor = float(self.grosor_entry.get())
            ancho = float(self.ancho_entry.get())

            # Calcular area
            area = grosor * ancho

            # Calcular peso
            weight = area  * densidad

            # Define the variables as sympy symbols
            x, y, z = symbols('x y z')

            # Define the function to calculate the weight
            f = x * y * z

            # Calculate the first derivative
            change_reason = diff(f, x).subs({x: grosor, y: ancho, z: densidad}) + \
                            diff(f, y).subs({x: grosor, y: ancho, z: densidad}) + \
                            diff(f, z).subs({x: grosor, y: ancho, z: densidad})

            # Calculate the second derivative
            change_reason_above = diff(diff(f, x), x).subs({x: grosor, y: ancho, z: densidad}) + \
                                diff(diff(f, y), y).subs({x: grosor, y: ancho, z: densidad}) + \
                                diff(diff(f, z), z).subs({x: grosor, y: ancho, z: densidad})

            
            # Create a function for the graphic
            def weight_function(x):
                return (change_reason * x) + (grosor * ancho * densidad)

            # Create a 2D plot of weight vs. area
            x_values = np.linspace(0, 10, 10)  # area values
            y_values = [weight_function(x) for x in x_values]

            plt.plot(x_values, y_values)
            plt.xlabel('grosor * ancho (m^2)')
            plt.ylabel('Weight (kg)')
            plt.title('Weight vs. Area')
            plt.grid(True)
            plt.show()

            # Mostrar resultados
            self.result_label['text'] = f"peso: {weight} kg\n"
            self.result_label['text'] += f"primera derivada: {change_reason}\n"
            self.result_label['text'] += f"segunda derivada: {change_reason_above}\n"
            self.area_result_label['text'] = f"grosor * ancho: {area}"

        except ValueError:
            self.result_label['text'] = "Error: Invalid input"

    def run(self):
        self.window.mainloop()

# funcion main
def main():
    CalculatorInterface().run()

if __name__ == "__main__":
    main()