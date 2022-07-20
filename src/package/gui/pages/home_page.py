import tkinter as tk
from tkinter import *
from src.package.domain.embed import *
from PIL import Image, ImageTk

# ---------------------------------------- HOME PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class HomePage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        #label = tk.Label(self, text="Home Page", font=('Times', '20'))
        #label.pack(pady=0, padx=0)

        # CODE FOR THIS PAGE
        
        self.columnconfigure(0, weight=2)
        self.rowconfigure(1, weight=3)
        
        # this will create a label widget
        l1 = Label(self, text = "Height")
        l2 = Label(self, text = "Width")
        l3 = Label(self, text = "third")
        
        
        def nextPage():
            print("aaa")
            parent.show_frame(parent.StartPage_01)
        l4 = Button(self,text="Next Page", command=nextPage,bg="#E2FF93", fg= "#3339E1",activeforeground= "#0E7283",activebackground="#FFC9F9")
        
        def backPage():
            print("aaa")
            parent.show_frame(parent.HomePage)
        l5 = Button(self,text="Back Page", command=backPage,bg="#E2FF93", fg= "#3339E1",activeforeground= "#0E7283",activebackground="#FFC9F9")
        
        
        # grid method to arrange labels in respective
        # rows and columns as specified
        
        l1.grid(row = 0, column = 0, sticky = W, pady = 2)
        l2.grid(row = 1, column = 0, sticky = W, pady = 2)
        l3.grid(row = 0, column = 1, sticky = W, pady = 2)
        l4.grid(row = 2, column = 1, sticky = W, pady = 2)
        l5.grid(row = 2, column = 0, sticky = W, pady = 2)


    
    



