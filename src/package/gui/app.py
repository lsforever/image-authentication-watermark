import tkinter as tk
from tkinter import *
from tkinter import ttk
# TODO add ttk widgets to this one

import src.package.gui.extentions as U
#import extentions as U

#import pages
from src.package.gui.pages.home_page import HomePage
from src.package.gui.pages.validation_page import Validation
from src.package.gui.pages.methods.method_1.m1_page_1 import M1_Page_1


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting up Initial Things
        self.title("Image Authentication")
        self.geometry("720x550")
        self.resizable(True, True)
        self.iconphoto(False, tk.PhotoImage(
            file="src/package/resources/img/assasin_logo.png"))
        self.minsize(500, 300)

        # Creating a container
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize Frames
        self.frames = {}
        self.HomePage = HomePage
        self.Validation = Validation

        # method 01 frames
        self.m1_frames = {}
        self.M1_Page_1 = M1_Page_1

        # Defining Frames and Packing it
        for F in {
            HomePage,
            Validation, 
        }:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # menubar = frame.create_menubar(self)
        menubar = create_menubar(self, self)
        self.configure(menu=menubar)
        frame.tkraise()  # This line will put the frame on front
    
    # method 1 frames
    def show_m1_frame(self, cont):
        frame = self.m1_frames[cont]
        if cont == self.M1_Page_1:
            pass
        elif cont == self.M1_Page_1:
            pass
        else:
            return
        
        menubar = create_menubar(self, self)
        self.configure(menu=menubar)
        frame.tkraise()
        


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


if __name__ == "__main__":
    app = App()
    app.mainloop()
