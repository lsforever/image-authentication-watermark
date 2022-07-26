from email.mime import image
from tkinter import *
from tkinter import ttk
from src.package.utils.constants import COPYRIGHT_TEXT
from src.package.gui.pages.methods.methods_list import methods_list
from PIL import Image, ImageTk
import copy

# ---------------------------------------- HOME PAGE FRAME / CONTAINER ------------------------------------------------------------------------


class HomePage(ttk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        # CODE FOR THIS PAGE

        style = ttk.Style()
        style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'),
                        foreground='black',)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # label frame
        lf = ttk.LabelFrame(self, text='Home')
        lf.grid(column=0, row=0, padx=20, pady=20, sticky=E+W+N+S)

        l1 = ttk.Label(lf, text="Image Authentication Using Watermarks")
        l2 = ttk.Label(lf, text="Select method :")
        l3 = ttk.Label(lf, text=COPYRIGHT_TEXT)

        self.current_str = StringVar()
        combo_box = ttk.Combobox(lf, textvariable=self.current_str,
                                 state='readonly', values=list(methods_list.values()))
        combo_box.current(0)
        combo_box.bind("<<ComboboxSelected>>", lambda e: self.focus())

        def start():
            id = list(methods_list)[combo_box.current()]
            if id == 'm_1':
                parent.show_m1_frame(parent.M1_Page_1)
            elif id == 'm_2':
                parent.show_m1_frame(parent.M1_Page_1)
            else:
                pass

        b1 = ttk.Button(lf, text="Start", command=start, style='W.TButton')

        lf.columnconfigure(1, weight=1)
        lf.rowconfigure(3, weight=1)

        l1.grid(row=0, column=0, columnspan=2, sticky=W, pady=10, padx=10)
        l2.grid(row=1, column=0, sticky=W, pady=10, padx=10)
        combo_box.grid(row=1, column=1, sticky=E+W, pady=10, padx=10)

        b1.grid(row=2, column=0, columnspan=2,  pady=10, padx=10)
        l3.grid(row=4, column=0, columnspan=2, sticky=E+S, pady=2, padx=10)

        # self.a1 = Image.open('src/package/resources/img/bg_images/luffy.jpeg')
        # self.a1.thumbnail((470, 470), Image.ANTIALIAS)
        # self.img = ImageTk.PhotoImage(self.a1)
        # self.l4 = ttk.Label(lf, image=self.img)
        # self.l4.grid(row=3, column=0, columnspan=2, pady=10, padx=10)



        # lf.bind("<Configure>", self.resize_image)

    # def resize_image(self, event):
    #     w =event.width
    #     self.a2 = copy.deepcopy(self.a1)
    #     self.a2.thumbnail((w, w), Image.ANTIALIAS)
    #     self.img = ImageTk.PhotoImage(self.a2)
    #     self.l4.configure(image=self.img)
