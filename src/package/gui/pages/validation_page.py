import tkinter as tk
from tkinter import *

# ---------------------------------------- Validation PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class Validation(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Validation Page", font=('Times', '20'))
        label.pack(pady=0, padx=0)

        # ADD CODE HERE TO DESIGN THIS PAGE

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED,
                        activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(
            label="New Project", command=lambda: parent.show_frame(parent.Validation))
        filemenu.add_command(
            label="Close", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)

        # proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        # help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=U.about)
        help_menu.add_separator()

        return menubar