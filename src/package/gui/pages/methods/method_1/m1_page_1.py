import tkinter as tk
from tkinter import ttk
from tkinter import *

# ---------------------------------------- M1_page_1 FRAME / CONTAINER ------------------------------------------------------------------------

class M1_Page_1(tk.Frame):
    
    def __init__(self, parent, container):
        super().__init__(container)
        
        # CODE FOR THIS PAGE
        
        l1 = ttk.Label(self, text = "Image Authention Using watermark", font=('Times', '15'))
        l2 = ttk.Label(self, text = "Level 1 DWT(Discrete Wawelet Transformation with 'haar' algorithm",font=('Times', '10'))
        l3 = ttk.Label(self, text = "Alpha bleding embeding algorithm",font=('Times', '10'))
        l4 = ttk.Label(self, text = "Gray Scale (Better for psnr)",font=('Times', '10'))
        l5 = ttk.Label(self, text = "Uses Encryption",font=('Times', '10'))
        
        l6 = ttk.Label(self, text = "Choose your image and watermark image below\n(Select same size images for testing psnr ratios)")
    
        l7 = ttk.Label(self, text = "Enter your encryption key")
        l8 = ttk.Label(self, text = "Generate a new encryption key")
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)

        l1.grid(row = 0, column = 0, sticky = W, pady = (2,10))
        l2.grid(row = 1, column = 0, sticky = W, pady = 2)
        l3.grid(row = 2, column = 0, sticky = W, pady = 2)
        l4.grid(row = 3, column = 0, sticky = W, pady = 2)
        l5.grid(row = 4, column = 0, sticky = W, pady = 2)
        
        l6.grid(row = 5, column = 0, sticky = W, pady = (20,2))
        l7.grid(row = 6, column = 0, sticky = W, pady = 2)
        l8.grid(row = 7, column = 0, sticky = W, pady = 2)