import tkinter as tk
from tkinter import *
import src.package.gui.extentions as U
from src.package.domain.embed import *
from PIL import Image, ImageTk

# ---------------------------------------- HOME PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class HomePage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        #label = tk.Label(self, text="Home Page", font=('Times', '20'))
        #label.pack(pady=0, padx=0)

        # CODE FOR THIS PAGE
        
        # this will create a label widget
        l1 = Label(self, text = "Height")
        l2 = Label(self, text = "Width")
        l3 = Label(self, text = "third")
        
        image = Image.open("src/package/resources/img/test_images/image.png")
        mark = Image.open("src/package/resources/img/test_images/mark.png")
        
        items = embedWatermarkGrayScale(image,mark)
        
        img1 = ImageTk.PhotoImage(items[0].resize((200,200), Image.ANTIALIAS))
        img2 = ImageTk.PhotoImage(items[1].resize((200,200), Image.ANTIALIAS))
        img3 = ImageTk.PhotoImage(items[2].resize((200,200), Image.ANTIALIAS))
        
        img_label_1 = Label(self, image=img1)
        img_label_1.image = img1
        img_label_2 = Label(self, image=img2)
        img_label_2.image = img2
        img_label_3 = Label(self, image=img3)
        img_label_3.image = img3
        
        img_label_1.grid(row = 0, column = 0, sticky = W, pady = 2)
        img_label_2.grid(row = 0, column = 1, sticky = W, pady = 2)
        img_label_3.grid(row = 0, column = 2, sticky = W, pady = 2)
        # img_label_1.pack()
        # img_label_2.pack()
        # img_label_3.pack()
        
        
        extracted_mark = extractWatermarkGrayScale(image,items[2])
        img_extrac = ImageTk.PhotoImage(extracted_mark.resize((200,200), Image.ANTIALIAS))
        img_extrac_label = Label(self, image=img_extrac)
        img_extrac_label.image = img_extrac
        img_extrac_label.grid(row = 1, column = 0, sticky = W, pady = 2)
        
        # grid method to arrange labels in respective
        # rows and columns as specified
        
        # l1.grid(row = 0, column = 0, sticky = W, pady = 2)
        # l2.grid(row = 1, column = 0, sticky = W, pady = 2)
        # l3.grid(row = 0, column = 1, sticky = W, pady = 2)
        
        
        



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
