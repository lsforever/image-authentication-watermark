import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from src.package.utils.scrollable_frame import ScrollableFrame

from src.package.utils.constants import *

# ---------------------------------------- M1_Page_2 FRAME / CONTAINER ------------------------------------------------------------------------


class M1_Page_2(tk.Frame):

    def __init__(self, parent, container, data):
        super().__init__(container)

        # ADD CODE HERE TO DESIGN THIS PAGE
        self.data = data
        
        # Scrolling code start
        scroll = ScrollableFrame(self)
        scroll.pack(fill='both', expand=True)
        #scroll.pack(fill='both', expand=1)
        view = scroll.scrollable_frame
        # Scrolling code end
        
        
        ###########
        part_details = ttk.LabelFrame(view, text='Details')
        
        
        
        ###########
        part_gray = ttk.LabelFrame(view, text='Input Images')
        
        ###########
        part_dwt = ttk.LabelFrame(view, text='Level 1 DWT')
        
        ###########
        part_blend = ttk.LabelFrame(view, text='Embeding (Alpha Blend)')
        
        
        ###########
        part_nav = ttk.LabelFrame(view, text='Navigate')
        def home():
            parent.show_frame(parent.HomePage)

        def back():
            parent.show_m1_frame(parent.M1_Page_1)
            
        def next():
            pass

        b1 = ttk.Button(part_nav, text="Home",
                        command=home)
        b2 = ttk.Button(part_nav, text="Back",
                        command=back)
        b2 = ttk.Button(part_nav, text="Next",
                        command=next)
        b1.grid(row=0, column=0, pady=5, padx=10)
        b2.grid(row=0, column=1, pady=5, padx=10)
        b2.grid(row=0, column=2, pady=5, padx=10)

      

    # ------------------------------------------------------------------------------------------
