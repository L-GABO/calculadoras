import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from sympy import *

class Calcular:
    gravedad = 9.81 #constante

    #asignar varintes
    def __init__(self):
        self.x, self.y, self.z = symbols('x y z')
        self.f = self.x * self.y * self.z

    #funcion de peso
    def peso(self, area, longitud, densidad):
        peso = area * longitud * densidad
        return peso

    #funcion de grosor 3 ancho (no es un area de el PTR)
    def area(self, grosor, ancho):
        area = grosor * ancho
        return area
    
    #funcion de resistencia
    def resistencia(self, fuerza, area):
        resistencia = fuerza / area
        return resistencia

    def peso_total(self, peso_libre, peso_carga):
        peso_total = peso_libre + peso_carga
        return peso_total

    #funcion de fuerza
    def fuerza(self, peso, gravedad, peso_total):
        fuerza = peso_total * gravedad
        return fuerza
        
    def peso_libre(self, ancho, grosor, Longitud, densidad):
        peso_libre = (Longitud * densidad * (ancho - (2*grosor)) ** 2)
        return peso_libre

    def resistencia_permitida(self, YoT_fuerza, factor):
        resistencia_permitida = YoT_fuerza / factor
        return resistencia_permitida

    def fuerza_permitida(self, resistencia_permitida, ancho, grosor,area):
        fuerza_permitida = resistencia_permitida * (area)
        return fuerza_permitida

class interfaz:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("optimizacion peso")
        self.calcular = Calcular()

        self.longitud_label = tk.Label(self.window, text="Longitud (m):")
        self.longitud_label.pack()
        self.longitud_entry = tk.Entry(self.window)
        self.longitud_entry.pack()

        # Crear un menu desplegable para la unidad de longitud
        self.longitud_unit_label = tk.Label(self.window, text="Unidad:")
        self.longitud_unit_label.pack()
        self.longitud_unit = tk.StringVar(self.window)
        self.longitud_unit.set("m")  # valor predeterminado|
        self.longitud_unit_options = ["m", "cm", "mm"]
        self.longitud_unit_menu = tk.OptionMenu(self.window, self.longitud_unit, *self.longitud_unit_options)
        self.longitud_unit_menu.pack()

        self.densidad_label = tk.Label(self.window, text="Densidad (kg/m^3):")
        self.densidad_label.pack()
        self.densidad_entry = tk.Entry(self.window)
        self.densidad_entry.pack()

        self.grosor_label = tk.Label(self.window, text="grosor")
        self.grosor_label.pack()
        self.grosor_entry = tk.Entry(self.window)
        self.grosor_entry.pack()

        # Crear un menu desplegable para la unidad de grosor
        self.grosor_unit_label = tk.Label(self.window, text="Unidad:")
        self.grosor_unit_label.pack()
        self.grosor_unit = tk.StringVar(self.window)
        self.grosor_unit.set("m")  # default value
        self.grosor_unit_options = ["m", "cm", "mm"]
        self.grosor_unit_menu = tk.OptionMenu(self.window, self.grosor_unit, *self.grosor_unit_options)
        self.grosor_unit_menu.pack()

        self.ancho_label = tk.Label(self.window, text="ancho")
        self.ancho_label.pack()
        self.ancho_entry = tk.Entry(self.window)
        self.ancho_entry.pack()
        
        # Crear un menu desplegable para la unidad de ancho
        self.ancho_unit_label = tk.Label(self.window, text="Unidad:")
        self.ancho_unit_label.pack()
        self.ancho_unit = tk.StringVar(self.window)
        self.ancho_unit.set("m")  # default value
        self.ancho_unit_options = ["m", "cm", "mm"]
        self.ancho_unit_menu = tk.OptionMenu(self.window, self.ancho_unit, *self.ancho_unit_options)
        self.ancho_unit_menu.pack()

        self.peso_carga_label = tk.Label(self.window, text="peso a cargar")
        self.peso_carga_label.pack()
        self.peso_carga_entry = tk.Entry(self.window)
        self.peso_carga_entry.pack()

        self.YoT_fuerza_label = tk.Label(self.window, text="Resistencia a la tracción o límite elástico")
        self.YoT_fuerza_label.pack()
        self.YoT_fuerza_entry = tk.Entry(self.window)
        self.YoT_fuerza_entry.pack()

        #Seleccion de unidad
        self.YoT_fuerza_unit_label = tk.Label(self.window, text="Unidad:")
        self.YoT_fuerza_unit_label.pack()
        self.YoT_fuerza_unit = tk.StringVar(self.window)
        self.YoT_fuerza_unit.set("Pa")  # Valor predeterminado
        self.YoT_fuerza_unit_options = ["Pa", "KPa", "MPa", "GPa"]
        self.YoT_fuerza_unit_menu = tk.OptionMenu(self.window, self.YoT_fuerza_unit, *self.YoT_fuerza_unit_options)
        self.YoT_fuerza_unit_menu.pack()

        self.factor_label = tk.Label(self.window, text="factor de seguridad")
        self.factor_label.pack()
        self.factor_entry = tk.Entry(self.window)
        self.factor_entry.pack()

        self.resistencia_result_label = tk.Label(self.window, text="resistencia (Pa):")
        self.resistencia_result_label.pack()

        self.fuerza_label = tk.Label(self.window, text="fuerza (N):")
        self.fuerza_label.pack()

        self.peso_total_label = tk.Label(self.window, text="peso total (kg):")
        self.peso_total_label.pack()

        self.fuerza_permitida_label = tk.Label(self.window, text="fuerza permitida (N):")
        self.fuerza_permitida_label.pack()

        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

    def calculate(self):
        try:
            longitud = float(self.longitud_entry.get())
            densidad = float(self.densidad_entry.get())
            grosor = float(self.grosor_entry.get())
            ancho = float(self.ancho_entry.get())
            peso_carga = float(self.peso_carga_entry.get())
            YoT_fuerza = float(self.YoT_fuerza_entry.get())
            factor = float(self.factor_entry.get())

            # Convertir la unidad de longitud a metros
            longitud = float(self.longitud_entry.get())
            if self.longitud_unit.get() == "cm":
                longitud /= 100
            elif self.longitud_unit.get() == "mm":
                longitud /= 1000

            grosor = float(self.grosor_entry.get())
            if self.grosor_unit.get() == "cm":
                grosor /= 100
            elif self.grosor_unit.get() == "mm":
                grosor /= 1000

            ancho = float(self.ancho_entry.get())
            if self.ancho_unit.get() == "cm":
                ancho /= 100
            elif self.ancho_unit.get() == "mm":
                ancho /= 1000
                
            # Convertir la unidad de resistencia a Pa
            YoT_fuerza = float(self.YoT_fuerza_entry.get())
            if self.YoT_fuerza_unit.get() == "KPa":
                YoT_fuerza *= 1e3
            elif self.YoT_fuerza_unit.get() == "MPa":    
                YoT_fuerza *= 1e6
            elif self.YoT_fuerza_unit.get() == "GPa":
                YoT_fuerza *= 1e9

            # Calcular el area
            area = self.calcular.area(grosor, ancho)

            # Calcular el peso
            peso = self.calcular.peso(area, longitud, densidad)

            # Calcular el peso total
            peso_total = self.calcular.peso_total(peso, peso_carga)

            # Calcular la fuerza
            fuerza = self.calcular.fuerza(peso, Calcular.gravedad, peso_total)

            # Calcular la resistencia
            resistencia = self.calcular.resistencia(fuerza, area)

            # Calcular la resistencia permitida
            resistencia_permitida = self.calcular.resistencia_permitida(YoT_fuerza, factor)

            # Calcular la fuerza permitida
            fuerza_permitida = self.calcular.fuerza_permitida(resistencia_permitida, ancho, grosor, area)

            # mostrar el resultado
            self.resistencia_result_label['text'] = f"resistencia: {resistencia} Pa\n"
            self.peso_total_label['text'] = f"peso total: {peso_total} kg"
            self.fuerza_label['text'] = f"fuerza: {fuerza} N"
            self.resistencia_result_label['text'] += f"resistencia permitida: {resistencia_permitida} Pa"
            self.fuerza_permitida_label['text'] = f"fuerza permitida: {fuerza_permitida} N"

        except ValueError:
            self.result_label['text'] = "Error: Invalid input"

    def run(self):
        self.window.mainloop()

def main():
        Calcular()
        interfaz().run()

if __name__ == "__main__":
    main()

def main():
        Calcular()
        interfaz().run()

if __name__ == "__main__":
    main()
