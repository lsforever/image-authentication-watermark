import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from src.package.domain.img_func import get_watermarked_img_with_info

from src.package.utils.scrollable_frame import ScrollableFrame

from src.package.utils.constants import *
from src.package.utils.extentions import get_dpi, get_resize_shape_with_aspect_ratio

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

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

        max_image_show_size = 200

        ########### part details
        part_details = ttk.LabelFrame(view, text='Details')
        l1 = ttk.Label(part_details, text="The gray scale watermark will be embeded to LL band of DWT coefficient of original image using alpha blend.").grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W)
        part_details.bind("<Configure>", lambda e:
                          l1.configure(wraplength=e.width - 60)
                          )
        ttk.Label(
            part_details, text="Following alpha blending constants will be used").grid(
            row=1, column=0, columnspan=2, padx=10, pady=2, sticky=W)
        ttk.Label(part_details, text="k : {k}".format(k = self.data[ALPHA_BLEND_K])).grid(
            row=2, column=0, padx=10, pady=2, sticky=W)
        ttk.Label(part_details, text="q : {q}".format(q = self.data[ALPHA_BLEND_Q])).grid(
            row=2, column=1, padx=10, pady=2, sticky=W)
        part_details.columnconfigure(0, weight=1)
        part_details.columnconfigure(1, weight=1)


        # z1 , part gray
        part_gray = ttk.LabelFrame(view, text='Input Images')

        pg_1 = ttk.LabelFrame(part_gray, text="Original Grayscale Image")
        pg_2 = ttk.LabelFrame(part_gray, text="Watermark Grayscale Image")
        # self.gray_img_original_a = ImageTk.PhotoImage(Image.fromarray(
        #     self.data[ORIGINAL_IMAGE_GRAY_ARRAY]).resize((300, 205), Image.ANTIALIAS))
        # self.gray_img_watermark_a = ImageTk.PhotoImage(Image.fromarray(
        #     self.data[WATERMARK_IMAGE_GRAY_ARRAY]).resize((300, 205), Image.ANTIALIAS))

        b_w_original = Image.fromarray(self.data[ORIGINAL_IMAGE_GRAY_ARRAY])
        b_w_mark = Image.fromarray(self.data[WATERMARK_IMAGE_GRAY_ARRAY])
        b_w_original = b_w_original.resize(get_resize_shape_with_aspect_ratio(
            b_w_original.size, max_image_show_size), Image.ANTIALIAS)
        b_w_mark = b_w_mark.resize(get_resize_shape_with_aspect_ratio(
            b_w_mark.size, max_image_show_size), Image.ANTIALIAS)

        #b_w_original = b_w_original.thumbnail((max_image_show_size, max_image_show_size), Image.ANTIALIAS)
        #b_w_mark = b_w_mark.thumbnail((max_image_show_size, max_image_show_size), Image.ANTIALIAS)
        # b_w_original = b_w_original.resize((200, 200), Image.ANTIALIAS)
        # b_w_mark = b_w_mark.resize((200, 200), Image.ANTIALIAS)

        self.gray_img_original_a = ImageTk.PhotoImage(b_w_original)
        self.gray_img_watermark_a = ImageTk.PhotoImage(b_w_mark)

        gray_img_original = ttk.Label(pg_1, image=self.gray_img_original_a)
        gray_img_watermark = ttk.Label(pg_2, image=self.gray_img_watermark_a)

        z1_l1 = ttk.Label(pg_1, text="Image View")
        z1_l2 = ttk.Label(pg_2, text="Image View")
        z1_l3 = ttk.Label(pg_1, text="Image Histogram View")
        z1_l4 = ttk.Label(pg_2, text="Image Histogram View")

        z1_l1.grid(row=0, column=0, padx=10, pady=(10, 2), sticky=W)
        z1_l2.grid(row=0, column=0, padx=10, pady=(10, 2), sticky=W)
        z1_l3.grid(row=2, column=0, padx=10, pady=(10, 2), sticky=W)
        z1_l4.grid(row=2, column=0, padx=10, pady=(10, 2), sticky=W)
        gray_img_original.grid(row=1, column=0, padx=10, pady=2, sticky=W)
        gray_img_watermark.grid(row=1, column=0, padx=10, pady=2, sticky=W)

        pg_1.grid(row=0, column=0, padx=10, pady=10, sticky=W+E)
        pg_2.grid(row=0, column=1, padx=10, pady=10, sticky=W+E)

        part_gray.columnconfigure(0, weight=1)
        part_gray.columnconfigure(1, weight=1)
        
        
        
        # the figure that will contain the plot
        # fig = Figure(figsize = (5, 5), dpi = 100)
        # fig = Figure(figsize = (3.5,3), dpi = get_dpi())#TODO check dpi
        fig = Figure(figsize = (3,3), dpi = get_dpi())#TODO check dpi
    
        # adding the subplot
        plot1 = fig.add_subplot(111)
    
        # plotting the graph
        plot1.set_title("histogram xxx")
        plot1.hist(self.data[ORIGINAL_IMAGE_GRAY_ARRAY].ravel(), 256, (0, 256))
    
        # kinter canvas below
        canvas = FigureCanvasTkAgg(fig,
                                master = pg_1)  
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, pg_1, pack_toolbar=False)
        toolbar.update()
        canvas.get_tk_widget().grid(row=3, column=0, padx=10, pady=10, sticky=W+E)
        toolbar.grid(row=4, column=0, padx=10, pady=10, sticky=W+E)
        
        
        

        ########### part dwt
        part_dwt = ttk.LabelFrame(view, text='Level 1 DWT')
        dwt_o = ttk.LabelFrame(
            part_gray, text="Original Image DWT coefficients")
        dwt_m = ttk.LabelFrame(
            part_gray, text="Watermark Image DWT coefficients")

        #dwt_info = get_watermarked_img_with_info(self.data[ORIGINAL_IMAGE_GRAY_ARRAY],self.data[WATERMARK_IMAGE_GRAY_ARRAY],kkk,qqqq)

        dwt_original_img = ttk.Label(dwt_o, image=self.gray_img_original_a)
        dwt_mark_img = ttk.Label(dwt_m, image=self.gray_img_original_a)

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
        b3 = ttk.Button(part_nav, text="Next",
                        command=next)
        b1.grid(row=0, column=0, pady=5, padx=10)
        b2.grid(row=0, column=1, pady=5, padx=10)
        b3.grid(row=0, column=2, sticky=E, pady=5, padx=10)
        part_nav.columnconfigure(2, weight=1)

        #################################
        part_details.grid(row=0, column=0, padx=10, pady=10, sticky=E+W)
        part_gray.grid(row=1, column=0, padx=10, pady=10, sticky=E+W)
        part_dwt.grid(row=2, column=0, padx=10, pady=10, sticky=E+W)
        part_blend.grid(row=3, column=0, padx=10, pady=10, sticky=E+W)
        part_nav.grid(row=4, column=0, padx=10, pady=10, sticky=E+W+S)

        view.columnconfigure(0, weight=1)
        view.rowconfigure(4, weight=1)

    # ------------------------------------------------------------------------------------------
