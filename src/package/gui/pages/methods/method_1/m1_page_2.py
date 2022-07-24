import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

from src.package.utils.constants import *

# ---------------------------------------- M1_Page_2 FRAME / CONTAINER ------------------------------------------------------------------------

class M1_Page_2(tk.Frame):
    
    
    
    def __init__(self, parent, container, data):
        super().__init__(container)
        
        # ADD CODE HERE TO DESIGN THIS PAGE
        self.data = data
        print(data)
        
        def home():
            parent.show_frame(parent.HomePage)
            
        def back():
            parent.show_m1_frame(parent.M1_Page_1)
            
        b1 = ttk.Button(self, text="Home",
                        command=home)
        
        b2 = ttk.Button(self, text="Back",
                        command=back)
        
        b1.grid(row=0, column=0, sticky=W, pady=2, padx=5)
        b2.grid(row=1, column=0, sticky=W, pady=2, padx=5)
        
        
        self.a1 = ImageTk.PhotoImage(Image.fromarray(self.data[ORIGINAL_IMAGE_GRAY_ARRAY]))
        img1 = ttk.Label(self, image=self.a1)
        img1.grid(row=2, column=0, sticky=W, pady=2, padx=5)
    
    # ------------------------------------------------------------------------------------------
    