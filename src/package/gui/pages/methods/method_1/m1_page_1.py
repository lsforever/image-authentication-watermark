import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
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
        scroll.pack(fill='both', expand=1)
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
            max_image_show_size = 300
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

        img1 = ttk.Label(view, image=None)
        img2 = ttk.Label(view, image=None)

        l1 = ttk.Label(
            view, text="Image Authention Using watermark", font=('Times', '15'))
        l2 = ttk.Label(
            view, text="Level 1 DWT(Discrete Wawelet Transformation with 'haar' algorithm", font=('Times', '10'))
        l3 = ttk.Label(
            view, text="Alpha bleding embeding algorithm", font=('Times', '10'))
        l4 = ttk.Label(view, text="Gray Scale (Better for psnr)",
                       font=('Times', '10'))
        l5 = ttk.Label(view, text="Uses Encryption", font=('Times', '10'))

        l6 = ttk.Label(
            view, text="Choose your image and watermark image below\n(Select same size images for testing psnr ratios. Or else images will be cropped)")
        l7 = ttk.Label(
            view, text="Not selected")
        l8 = ttk.Label(
            view, text="Not selected")
        l9 = ttk.Label(view, text="Enter your encryption key")
        l10 = ttk.Label(view, text="Generate a new encryption key")

        b1 = ttk.Button(view, text="Use Defualt Images",
                        command=default_img)
        b2 = ttk.Button(view, text="Choose Original Image",
                        command=choose_original)
        b3 = ttk.Button(view, text="Choose Watermark Image",
                        command=choose_watermark)
        b4 = ttk.Button(view, text="Generate New Encryption Key",
                        command=generate_enc)
        b5 = ttk.Button(view, text="Back",
                        command=back)
        b6 = ttk.Button(view, text="Next",
                        command=next)

        view.columnconfigure(0, weight=1)
        view.rowconfigure(0, weight=0)

        l1.grid(row=0, column=0, sticky=W, pady=(2, 10), padx=5)
        l2.grid(row=1, column=0, sticky=W, pady=0, padx=5)
        l3.grid(row=2, column=0, sticky=W, pady=0, padx=5)
        l4.grid(row=3, column=0, sticky=W, pady=0, padx=5)
        l5.grid(row=4, column=0, sticky=W, pady=0, padx=5)

        l6.grid(row=5, column=0, sticky=W, pady=(20, 2), padx=5)
        l7.grid(row=6, column=0, sticky=W, pady=2, padx=5)
        l8.grid(row=7, column=0, sticky=W, pady=2, padx=5)
        l9.grid(row=8, column=0, sticky=W, pady=2, padx=5)
        l10.grid(row=9, column=0, sticky=W, pady=2, padx=5)

        b1.grid(row=10, column=0, sticky=W, pady=2, padx=5)
        b2.grid(row=11, column=0, sticky=W, pady=2, padx=5)
        b3.grid(row=12, column=0, sticky=W, pady=2, padx=5)
        b4.grid(row=13, column=0, sticky=W, pady=2, padx=5)
        b5.grid(row=14, column=0, sticky=W, pady=2, padx=5)
        b6.grid(row=15, column=0, sticky=W, pady=2, padx=5)

        img1.grid(row=16, column=0, sticky=W, pady=2, padx=5)
        img2.grid(row=17, column=0, sticky=W, pady=2, padx=5)
