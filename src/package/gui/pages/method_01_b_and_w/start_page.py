import tkinter as tk
from tkinter import *

# ---------------------------------------- Validation PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class StartPage_01(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        # CODE FOR THIS PAGE
        
        self.columnconfigure(0, weight=1)
        
        #self.rowconfigure(0, weight=1)
        #self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        
        # this will create a label widget
        l1 = Label(self, text = "DWT black and white")
        l2 = Label(self, text = "Select Original Image and the Warter Mark Image below")
        l3 = LabelFrame(self, text = "Select Encryption keys",height=200, width=200)
        
        
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
        l3.grid(row = 2, column = 0, sticky = E+W, pady = 2)
        
        l4.grid(row = 3, column = 0, sticky = W, pady = 2)
        l5.grid(row = 4, column = 0, sticky = E+W, pady = 2)
        