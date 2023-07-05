import tkinter as tk

class CustomDialog(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Custom Dialog")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Hello World!")
        self.label.pack(padx=20, pady=20)