import tkinter as tk
from tkinter import *

# ---------------------------------------- Validation PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class Validation(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Validation Page", font=('Times', '20'))
        label.pack(pady=0, padx=0)

        # ADD CODE HERE TO DESIGN THIS PAGE