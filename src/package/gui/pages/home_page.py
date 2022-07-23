from tkinter import *
from tkinter import ttk
from src.package.gui.pages.methods.methods_list import methods_list


# ---------------------------------------- HOME PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class HomePage(ttk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        # CODE FOR THIS PAGE
        
        style = ttk.Style()
        style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'black',)
        
        l1 = ttk.Label(self, text = "Image Authentication Using Watermarks")
        l2 = ttk.Label(self, text = "Select method :")
        l3 = ttk.Label(self, text = "2022 @c")
        
        self.current_str = StringVar()
        combo_box = ttk.Combobox(self, textvariable=self.current_str, state='readonly', values= list(methods_list.values()))
        combo_box.current(0)
        combo_box.bind("<<ComboboxSelected>>",lambda e: self.focus())
        
        
        def start():
            id = list(methods_list)[combo_box.current()]
            if id == 'm_1':
                parent.show_frame(parent.M1_Page_1)
            elif id == 'm_2':
                parent.show_frame(parent.M1_Page_1)
            else:
                parent.show_frame(parent.M1_Page_1)
            
        
        b1 = ttk.Button(self,text="Start", command=start, style='W.TButton')
        
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)
        
        l1.grid(row = 0, column = 0,columnspan=2, sticky = W, pady = 10)
        l2.grid(row = 1, column = 0, sticky = W, pady = 10)
        combo_box.grid(row = 1, column = 1, sticky = E+W, pady = 10, padx= 10 )
      
       
        b1.grid(row = 2, column = 0,columnspan=2,  pady = 10)
        l3.grid(row = 3, column = 0,columnspan=2, sticky = E+S, pady = 2, padx= 10)
        
        