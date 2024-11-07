import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.text_input = tk.Text(self)
        self.text_input.pack()

        self.save_button = tk.Button(self)
        self.save_button["text"] = "Save"
        self.save_button["command"] = self.save_text
        self.save_button.pack()

        self.display_label = tk.Label(self)
        self.display_label.pack()

    def save_text(self):
        text = self.text_input.get("1.0", tk.END)
        self.display_label["text"] = text

root = tk.Tk()
app = Application(master=root)
app.mainloop()