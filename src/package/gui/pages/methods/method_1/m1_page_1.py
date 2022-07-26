import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from turtle import width
from src.package.utils.constants import *
from src.package.utils.scrollable_frame import ScrollableFrame

from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import cv2

# ---------------------------------------- M1_page_1 FRAME / CONTAINER ------------------------------------------------------------------------


class M1_Page_1(tk.Frame):

    def __init__(self, parent, container):
        super().__init__(container)

        # CODE FOR THIS PAGE

        self.data = {}
        self.height = 0
        self.width = 0

        # Scrolling code start
        scroll = ScrollableFrame(self)
        scroll.pack(fill='both', expand=True)
        #scroll.pack(fill='both', expand=1)
        view = scroll.scrollable_frame
        # Scrolling code end

        filetypes = (
            ('PNG, JPEG files', '*.PNG *.JPEG'),
        )

        # PILL Uses RGB while Opencv(cv2) uses BGR
        def default_img():
            self.data[ORIGINAL_IMAGE_PATH] = DEFAULT_ORIGINAL_IMAGE_PATH
            self.data[WATERMARK_IMAGE_PATH] = DEFAULT_WATERMARK_IMAGE_PATH
            l7.config(text="Default image selected")
            l8.config(text="Default watermark selected")
            set_images()

        def choose_original():
            self.data[ORIGINAL_IMAGE_PATH] = filedialog.askopenfilename(
                title='Select Original Image ...',
                filetypes=filetypes,
            )
            set_images()

        def choose_watermark():
            self.data[WATERMARK_IMAGE_PATH] = filedialog.askopenfilename(
                title='Select Watermark Image ...',
                filetypes=filetypes,
            )
            set_images()

        def resizeImage(img):
            max_image_show_size = 200
            w, h = img.size
            if h > max_image_show_size:
                img.thumbnail(
                    (max_image_show_size, max_image_show_size), Image.ANTIALIAS)

        def set_images():

            a1 = None
            a2 = None
            if ORIGINAL_IMAGE_PATH in self.data:
                l7.config(text=self.data[ORIGINAL_IMAGE_PATH])
                a1 = Image.open(self.data[ORIGINAL_IMAGE_PATH])
            if WATERMARK_IMAGE_PATH in self.data:
                l8.config(text=self.data[WATERMARK_IMAGE_PATH])
                a2 = Image.open(self.data[WATERMARK_IMAGE_PATH])

            if a1 and a2:
                a1w, a1h = a1.size
                a2w, a2h = a2.size
                if a1h <= a2h:
                    self.height = a1h
                else:
                    self.height = a2h
                if a1w <= a2w:
                    self.width = a1w
                else:
                    self.width = a2w

                a1 = a1.crop((0, 0, self.width, self.height))
                a2 = a2.crop((0, 0, self.width, self.height))

                resizeImage(a1)
                resizeImage(a2)

                self.data[ORIGINAL_IMAGE] = ImageTk.PhotoImage(a1)
                self.data[WATERMARK_IMAGE] = ImageTk.PhotoImage(a2)

                img1.configure(image=self.data[ORIGINAL_IMAGE])
                img2.configure(image=self.data[WATERMARK_IMAGE])

                a1 = cv2.imread(self.data[ORIGINAL_IMAGE_PATH])
                a2 = cv2.imread(self.data[WATERMARK_IMAGE_PATH])
                a1 = a1[0:self.height, 0:self.width]
                a2 = a2[0:self.height, 0:self.width]
                self.data[ORIGINAL_IMAGE_GRAY_ARRAY] = cv2.cvtColor(
                    a1, cv2.COLOR_BGR2GRAY)
                self.data[WATERMARK_IMAGE_GRAY_ARRAY] = cv2.cvtColor(
                    a2, cv2.COLOR_BGR2RGB)

            elif a1:
                resizeImage(a1)
                self.data[ORIGINAL_IMAGE] = ImageTk.PhotoImage(a1)
                img1.configure(image=self.data[ORIGINAL_IMAGE])
            elif a2:
                resizeImage(a2)
                self.data[WATERMARK_IMAGE] = ImageTk.PhotoImage(a2)
                img2.configure(image=self.data[WATERMARK_IMAGE])

        def generate_enc():
            pass

        def back():
            parent.show_frame(parent.HomePage)

        def next():
            # TODO check rquirements before next ///// encrpt add //// and (ENCRYPTION_KEY in data)
            if (ORIGINAL_IMAGE_PATH in self.data) and (WATERMARK_IMAGE_PATH in self.data) and (ORIGINAL_IMAGE_GRAY_ARRAY in self.data) and (WATERMARK_IMAGE_GRAY_ARRAY in self.data):
                parent.show_m1_frame(parent.M1_Page_2, data=self.data)
            else:
                showinfo(
                    title='Incomplete',
                    message='Select Images and Encryption key before continuing.')

        # UI basic part -------------------------------------------------------------------------------------------------------

        lf1 = ttk.LabelFrame(view, text='DWT level 1')
        lf2 = ttk.LabelFrame(view, text='Image Selection')
        lf3 = ttk.LabelFrame(view, text='Navigate')

        lf6 = ttk.LabelFrame(lf2, text='Original Image')
        lf7 = ttk.LabelFrame(lf2, text='Watermark Image')
        view.columnconfigure(0, weight=1)
        view.rowconfigure(4, weight=1)
        lf1.grid(column=0, row=0, padx=10, pady=10, sticky=E+W)
        lf2.grid(column=0, row=1, padx=10, pady=10, sticky=E+W)
        lf3.grid(column=0, row=3, padx=10, pady=10, sticky=E+W)

        img1 = ttk.Label(lf6, image=None)
        img2 = ttk.Label(lf7, image=None)

        l1 = ttk.Label(
            lf1, text="Image Authention Using watermark")
        l2 = ttk.Label(
            lf1, text="Level 1 DWT(Discrete Wawelet Transformation with 'haar' algorithm")
        l3 = ttk.Label(
            lf1, text="Alpha bleding embeding algorithm")
        l4 = ttk.Label(lf1, text="Gray scale")
        l5 = ttk.Label(lf1, text="Same size")

        l6 = ttk.Label(
            lf2, text="Choose your image and watermark image below\n(Select same size images for testing psnr ratios. Or else images will be cropped)")
        l7 = ttk.Label(
            lf6, text="n/a")
        l8 = ttk.Label(
            lf7, text="n/a")
        l9 = ttk.Label(
            lf6, text="Path :")
        l10 = ttk.Label(
            lf7, text="Path :")

        lf6.bind("<Configure>", lambda e:
                 l7.configure(wraplength=e.width - 60)
                 )
        lf7.bind("<Configure>", lambda e:
                 l8.configure(wraplength=e.width - 60)
                 )

        b1 = ttk.Button(lf2, text="Use Defualt Images",
                        command=default_img)
        b2 = ttk.Button(lf6, text="Choose Original Image",
                        command=choose_original)
        b3 = ttk.Button(lf7, text="Choose Watermark Image",
                        command=choose_watermark)
        b4 = ttk.Button(lf3, text="Back",
                        command=back)
        b5 = ttk.Button(lf3, text="Next",
                        command=next)
        cc = ttk.Label(view, text=COPYRIGHT_TEXT)

        # DWT
        l1.grid(row=0, column=0, sticky=W, pady=(8, 12), padx=10)
        l2.grid(row=1, column=0, sticky=W, pady=0, padx=10)
        l3.grid(row=2, column=0, sticky=W, pady=0, padx=10)
        l4.grid(row=3, column=0, sticky=W, pady=0, padx=10)
        l5.grid(row=4, column=0, sticky=W, pady=(2, 10), padx=10)

        # image
        l6.grid(row=0, column=0, columnspan=2, sticky=W, pady=(20, 2), padx=10)

        l9.grid(row=0, column=0, sticky=W, pady=2, padx=5)
        l7.grid(row=0, column=1, sticky=W, pady=2, padx=5)
        b2.grid(row=1, column=0, columnspan=2, sticky=W, pady=2, padx=5)
        img1.grid(row=2, column=0, columnspan=2, sticky=W, pady=2, padx=5)

        l10.grid(row=0, column=0, sticky=W, pady=2, padx=5)
        l8.grid(row=0, column=1, sticky=W, pady=2, padx=5)
        b3.grid(row=1, column=0, columnspan=2, sticky=W, pady=2, padx=5)
        img2.grid(row=2, column=0, columnspan=2, sticky=W, pady=2, padx=5)

        lf6.grid(column=0, row=1, padx=10, pady=10, sticky=E+W)
        lf7.grid(column=1, row=1, padx=10, pady=10, sticky=E+W)

        b1.grid(row=2, column=0, columnspan=2, sticky=E, pady=(2, 8), padx=10)

        lf2.rowconfigure(3, weight=1)
        lf2.rowconfigure(6, weight=1)

        # Nav
        b4.grid(row=0, column=0, sticky=W, pady=10, padx=10)
        b5.grid(row=0, column=1, sticky=E, pady=10, padx=10)

        cc.grid(row=4, column=0, sticky=E+S, pady=2, padx=10)

        lf1.columnconfigure(1, weight=1)

        lf2.columnconfigure(0, weight=1)
        lf2.columnconfigure(1, weight=1)

        lf3.columnconfigure(1, weight=1)
