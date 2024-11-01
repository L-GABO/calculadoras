import tkinter as tk
#definimos las variables a usar en formulas
class CalculatorInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator Interface")

        # Text explaining the terms
        self.term_text = tk.Label(self.window, text="F (Fuerza tensora)\nR (Resistencia a la tracción o límite elástico)\nV (Factor de seguridad)\nG (Grosor de PTR)\nA (Ancho de PTR)")
        self.term_text.pack()

        self.F_label = tk.Label(self.window, text="F (N):")
        self.F_label.pack()
        self.F_entry = tk.Entry(self.window)
        self.F_entry.pack()

        self.R_label = tk.Label(self.window, text="R (Pa):")
        self.R_label.pack()
        self.R_entry = tk.Entry(self.window)
        self.R_entry.pack()

         # maginutudes para Pa
        self.R_unit_label = tk.Label(self.window, text="Unit:")
        self.R_unit_label.pack()
        self.R_unit_var = tk.StringVar()
        self.R_unit_var.set("Pa")  # valor predeterminado
        self.R_unit_option = tk.OptionMenu(self.window, self.R_unit_var, "Pa", "MPa", "GPa", "kPa")
        self.R_unit_option.pack()

        self.v_label = tk.Label(self.window, text="v:")
        self.v_label.pack()
        self.v_entry = tk.Entry(self.window)
        self.v_entry.pack()

        self.G_label = tk.Label(self.window, text="G (m):")
        self.G_label.pack()
        self.G_entry = tk.Entry(self.window)
        self.G_entry.pack()

        self.A_label = tk.Label(self.window, text="A (m):")
        self.A_label.pack()
        self.A_entry = tk.Entry(self.window)
        self.A_entry.pack()

        # Crear boton de calcular
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        # Crear texto resultado
        self.result_label = tk.Label(self.window, text="Result:")
        self.result_label.pack()

    # Crear formulas y variables
    def calculate(self):
        try:
            F = float(self.F_entry.get())
            R = float(self.R_entry.get())
            R_unit = self.R_unit_var.get()

            # Convert R to Pa based on selected unit
            if R_unit == "MPa":
                R *= 1e6
            elif R_unit == "GPa":
                R *= 1e9
            elif R_unit == "kPa":
                R *= 1e3

            v = float(self.v_entry.get())
            G = float(self.G_entry.get())
            A = float(self.A_entry.get())

            print("F:", F)
            print("R:", R)
            print("v:", v)
            print("G:", G)
            print("A:", A)

            S = G * A

            result1 = F / S
            result2 = R / v
            result3 = result2 * S

            self.result_label['text'] = f"Tension de traccion: {result1} Pa\nTensión de tracción permitida: {result2} Pa\nfuerza de traccion permitida: {result3} N"

        except ValueError:
            self.result_label['text'] = "Error: Invalid input"
        except ZeroDivisionError:
            self.result_label['text'] = "Error: Division by zero"

    # Crear ventana
    def run(self):
        self.window.mainloop()

# funcion main
def main():
    CalculatorInterface().run()

if __name__ == "__main__":
    main()