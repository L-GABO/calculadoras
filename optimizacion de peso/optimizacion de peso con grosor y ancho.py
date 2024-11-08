import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from sympy import *
from scipy.constants import g

def Calcular():
    def convert_unit(value, unit):
        conversions = {"neutro": 1,"centi": 0.01,"mili": 0.001,"Kilo": 1e3,"Mega": 1e6,"Giga": 1e9,}
        return value * conversions[unit]

    def peso(area, longitud, densidad):
        return area * longitud * densidad

    def area(grosor, ancho):
        return grosor * ancho

    def resistencia(fuerza, area):
        return fuerza / area

    def peso_total(peso_libre, peso_carga):
        return peso_libre + peso_carga

    def fuerza(peso, peso_total):
        return peso_total * g

    def peso_libre(ancho, grosor, longitud, densidad):
        return ((longitud * densidad) * ((ancho**2) - (ancho - 2*grosor) ** 2))

    def resistencia_permitida(YoT_fuerza, factor):
        return YoT_fuerza / factor

    def fuerza_permitida(resistencia_permitida, ancho, grosor, area):
        return resistencia_permitida * (area)

    def demostracion(ancho, grosor):
        return ((ancho**2) - (ancho - 2*grosor) ** 2)

    return {
        "convert_unit": convert_unit,"peso": peso,"area": area,"resistencia": resistencia,"peso_total": peso_total,"fuerza": fuerza,"peso_libre": peso_libre,"resistencia_permitida": resistencia_permitida,"fuerza_permitida": fuerza_permitida, "demostracion": demostracion
    }
class interfaz:
    def create_unit_menu(self, window, label, default_unit, units):
        unit_label = tk.Label(window, text=label)
        unit_label.pack()
        unit_var = tk.StringVar(window)
        unit_var.set(default_unit)
        unit_menu = tk.OptionMenu(window, unit_var, *units)
        unit_menu.pack()
        return unit_var
    def __init__(self):

        # mandar a llamar a calcular
        self.calcular = Calcular()

        # Crear una ventana
        self.window = tk.Tk()
        self.window.title("optimizacion peso")
        self.calcular = Calcular()

        # Entrada de lonitud
        self.longitud_label = tk.Label(self.window, text="Longitud (m):")
        self.longitud_label.pack()
        self.longitud_entry = tk.Entry(self.window)
        self.longitud_entry.pack()

        # Entrada de densidad
        self.densidad_label = tk.Label(self.window, text="Densidad (kg/m^3):")
        self.densidad_label.pack()
        self.densidad_entry = tk.Entry(self.window)
        self.densidad_entry.pack()

        # Entrada de grosor
        self.grosor_label = tk.Label(self.window, text="grosor")
        self.grosor_label.pack()
        self.grosor_entry = tk.Entry(self.window)
        self.grosor_entry.pack()

        # Entrada de ancho
        self.ancho_label = tk.Label(self.window, text="ancho")
        self.ancho_label.pack()
        self.ancho_entry = tk.Entry(self.window)
        self.ancho_entry.pack()

        # Entrada de peso
        self.peso_carga_label = tk.Label(self.window, text="peso a cargar")
        self.peso_carga_label.pack()
        self.peso_carga_entry = tk.Entry(self.window)
        self.peso_carga_entry.pack()

        # Entrada de fuerza
        self.YoT_fuerza_label = tk.Label(self.window, text="Resistencia a la tracción o límite elástico")
        self.YoT_fuerza_label.pack()
        self.YoT_fuerza_entry = tk.Entry(self.window)
        self.YoT_fuerza_entry.pack()

        # Entrada de factor
        self.factor_label = tk.Label(self.window, text="factor de seguridad")
        self.factor_label.pack()
        self.factor_entry = tk.Entry(self.window)
        self.factor_entry.pack()

        # salida de resistencia
        self.resistencia_result_label = tk.Label(self.window, text="resistencia (Pa):")
        self.resistencia_result_label.pack()

        # salida de fuerza
        self.fuerza_label = tk.Label(self.window, text="fuerza (N):")
        self.fuerza_label.pack()

        # Entrada de longitud
        self.longitud_unit = self.create_unit_menu(self.window, "longitud", "neutro", ["neutro", "centi", "mili"])
        self.grosor_unit = self.create_unit_menu(self.window, "grosor", "neutro", ["neutro", "centi", "mili"])
        self.ancho_unit = self.create_unit_menu(self.window, "ancho", "neutro", ["neutro", "centi", "mili"])
        self.YoT_fuerza_unit = self.create_unit_menu(self.window, "YoT_fuerza", "neutro", ["neutro", "Kilo", "Mega", "Giga"])

        self.peso_total_label = tk.Label(self.window, text="peso total (kg):")
        self.peso_total_label.pack()

        self.fuerza_permitida_label = tk.Label(self.window, text="fuerza permitida (N):")
        self.fuerza_permitida_label.pack()

        self.demostracion_label = tk.Label(self.window, text="d")
        self.demostracion_label.pack()
        
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

            # Convertir la unidad
            longitud = self.calcular["convert_unit"](float(self.longitud_entry.get()), self.longitud_unit.get())
            grosor = self.calcular["convert_unit"](float(self.grosor_entry.get()), self.grosor_unit.get())
            ancho = self.calcular["convert_unit"](float(self.ancho_entry.get()), self.ancho_unit.get())
            YoT_fuerza = self.calcular["convert_unit"](float(self.YoT_fuerza_entry.get()), self.YoT_fuerza_unit.get())

           # Calcular el area
            area = self.calcular["area"](grosor, ancho)

            # Calcular el peso
            peso = self.calcular["peso"](area, longitud, densidad)

            # Calcular el peso libre
            peso_libre = self.calcular["peso_libre"](ancho, grosor, longitud, densidad)

            # Calcular el peso total
            peso_total = self.calcular["peso_total"](peso_libre, peso_carga)

            # Calcular la fuerza
            fuerza = self.calcular["fuerza"](peso, peso_total)

            # Calcular la resistencia
            resistencia = self.calcular["resistencia"](fuerza, area)

            # Calcular la resistencia permitida
            resistencia_permitida = self.calcular["resistencia_permitida"](YoT_fuerza, factor)

            # Calcular la fuerza permitida
            fuerza_permitida = self.calcular["fuerza_permitida"](resistencia_permitida, ancho, grosor, area)
            
            # Calcular la demostracion
            demostracion = self.calcular["demostracion"](ancho, grosor)
            
            # mostrar el resultado
            self.resistencia_result_label['text'] = f"resistencia: {resistencia} Pa\n"
            self.peso_total_label['text'] = f"peso total: {peso_total} kg"
            self.fuerza_label['text'] = f"fuerza: {fuerza} N"
            self.resistencia_result_label['text'] += f"resistencia permitida: {resistencia_permitida} Pa"
            self.fuerza_permitida_label['text'] = f"fuerza permitida: {fuerza_permitida} N"

        except ValueError as e:
            self.result_label['text'] = f"Error: {e}"

    def run(self):
        self.window.mainloop()

def main():   
        interfaz().run()

if __name__ == "__main__":
    main()
