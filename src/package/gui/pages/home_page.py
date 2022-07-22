from tkinter import *
from tkinter import ttk
from src.package.domain.embed import *
from PIL import Image, ImageTk
from src.package.gui.pages.methods.methods_list import methods_list



# ---------------------------------------- HOME PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class HomePage(ttk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        #label = tk.Label(self, text="Home Page", font=('Times', '20'))
        #label.pack(pady=0, padx=0)

        # CODE FOR THIS PAGE
        
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)
        
        style = ttk.Style()
        style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'black',)
        
        # this will create a label widget
        l1 = ttk.Label(self, text = "Image Authentication Using Watermarks")
        l2 = ttk.Label(self, text = "Select method :")
        l3 = ttk.Label(self, text = "2022 @c")
        
        self.current_str = StringVar()
        combo_box = ttk.Combobox(self, textvariable=self.current_str, state='readonly', values= list(methods_list.values()))
        combo_box.current(0)
        combo_box.bind("<<ComboboxSelected>>",lambda e: self.focus())
        
        # combo_box.current()
        # first_key = list(colors)[0]
        # first_val = list(colors.values())[0]
        
        def start():
            id = list(methods_list)[combo_box.current()]
            if id == 'm_1':
                parent.show_frame(parent.StartPage_1)
            else:
                parent.show_frame(parent.StartPage_1)
            
            
        b1 = ttk.Button(self,text="Start", command=start, style='W.TButton')
        
        
        # grid method to arrange labels in respective
        # rows and columns as specified
        
        l1.grid(row = 0, column = 0,columnspan=2, sticky = W, pady = 10)
        l2.grid(row = 1, column = 0, sticky = W, pady = 10)
        combo_box.grid(row = 1, column = 1, sticky = E+W, pady = 10, padx= 10 )
      
       
        b1.grid(row = 2, column = 0,columnspan=2,  pady = 10)
        l3.grid(row = 3, column = 0,columnspan=2, sticky = E+S, pady = 2, padx= 10)


    
    





# class HomePage(tk.Frame):
#     def __init__(self, parent, container):
#         super().__init__(container)

#         #label = tk.Label(self, text="Home Page", font=('Times', '20'))
#         #label.pack(pady=0, padx=0)

#         # CODE FOR THIS PAGE
        
#         self.columnconfigure(0, weight=2)
#         self.rowconfigure(1, weight=3)
        
#         # this will create a label widget
#         l1 = Label(self, text = "Height")
#         l2 = Label(self, text = "Width")
#         l3 = Label(self, text = "kkkkkkkkkkkkkkkkkkkkk")
        
        
#         def nextPage():
#             print("aaa")
#             parent.show_frame(parent.StartPage_01)
#         l4 = Button(self,text="Next Page", command=nextPage,bg="#E2FF93", fg= "#3339E1",activeforeground= "#0E7283",activebackground="#FFC9F9")
        
#         def backPage():
#             print("aaa")
#             parent.show_frame(parent.HomePage)
#         l5 = Button(self,text="Back Page", command=backPage,bg="#E2FF93", fg= "#3339E1",activeforeground= "#0E7283",activebackground="#FFC9F9")
        
        
#         # grid method to arrange labels in respective
#         # rows and columns as specified
        
#         l1.grid(row = 0, column = 0, sticky = W, pady = 2)
#         l2.grid(row = 1, column = 0, sticky = W, pady = 2)
#         l3.grid(row = 0, column = 1, sticky = W, pady = 2)
#         l4.grid(row = 2, column = 1, sticky = W, pady = 2)
#         l5.grid(row = 2, column = 0, sticky = W, pady = 2)