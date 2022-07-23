import tkinter as tk
from tkinter import ttk
from tkinter import *

# ---------------------------------------- Validation PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class Validation(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        # ADD CODE HERE TO DESIGN THIS PAGE
        
        label = ttk.Label(self, text="Validation Page", font=('Times', '20'))
        label.grid(row = 0, column = 0, sticky = W, pady = 2)
        
        
        


# import tkinter as tk
# from tkinter import ttk
# from tkinter import *

# # ---------------------------------------- M1_Page_2 FRAME / CONTAINER ------------------------------------------------------------------------

# class M1_Page_2(tk.Frame):
#     def __init__(self, parent, container):
#         super().__init__(container)

#         # ADD CODE HERE TO DESIGN THIS PAGE
        
#         label = ttk.Label(self, text="Validation Page", font=('Times', '20'))
#         label.grid(row = 0, column = 0, sticky = W, pady = 2)
        
        