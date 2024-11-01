import tkinter as tk

# definimos la clase poligono
class CalculatorInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator Interface")

        # Text explaining the terms
        self.term_text = tk.Label(self.window, text="B (base)\nH (Altura)\nW (base interior)\nh (altura interior)")
        self.term_text.pack()

        # crear las entradas de variable
        self.b_label = tk.Label(self.window, text="B:")
        self.b_label.pack()
        self.b_entry = tk.Entry(self.window)
        self.b_entry.pack()

        self.w_label = tk.Label(self.window, text="W:")
        self.w_label.pack()
        self.w_entry = tk.Entry(self.window)
        self.w_entry.pack()

        self.h_label = tk.Label(self.window, text="h:")
        self.h_label.pack()
        self.h_entry = tk.Entry(self.window)
        self.h_entry.pack()

        self.H_label = tk.Label(self.window, text="H:")
        self.H_label.pack()
        self.H_entry = tk.Entry(self.window)
        self.H_entry.pack()

        # Create boton de calcular
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        # Crear texto valor
        self.result_label = tk.Label(self.window, text="Result:")
        self.result_label.pack()

    # crear la interfaz de usuario
    def calculate(self):
        try:
            b = float(self.b_entry.get())
            w = float(self.w_entry.get())
            h = float(self.h_entry.get())
            H = float(self.H_entry.get())

            print("B:", b)
            print("W:", w)
            print("h:", h)
            print("H:", H)

            result = ((b * (H ** 3)) - (w * (h ** 3))) / 12

            self.result_label['text'] = f"Result: {result}"
        except ValueError:
            self.result_label['text'] = "Error: Invalid input"

    # ejecutar la interfaz
    def run(self):
        self.window.mainloop()

def main():
    CalculatorInterface().run()

if __name__ == "__main__":
    main()