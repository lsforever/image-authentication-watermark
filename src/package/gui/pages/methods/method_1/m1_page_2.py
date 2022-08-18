import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import copy
from src.package.domain.img_func import get_watermarked_img_with_info

from src.package.utils.scrollable_frame import ScrollableFrame

from src.package.utils.constants import *
from src.package.utils.extentions import get_dpi, get_resize_shape_with_aspect_ratio, show_gray_img_histogram_dialog


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

        # part details
        part_details = ttk.LabelFrame(view, text='Details')
        l1 = ttk.Label(part_details, text="The gray scale watermark will be embeded to LL band of DWT coefficient of original image using alpha blend.").grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W)
        part_details.bind("<Configure>", lambda e:
                          l1.configure(wraplength=e.width - 60)
                          )
        ttk.Label(
            part_details, text="Following alpha blending constants will be used").grid(
            row=1, column=0, columnspan=2, padx=10, pady=2, sticky=W)
        k = self.data[ALPHA_BLEND_K].get()
        q = self.data[ALPHA_BLEND_Q].get()
        ttk.Label(part_details, text="k : {k}".format(k=k)).grid(
            row=2, column=0, padx=10, pady=2, sticky=W)
        ttk.Label(part_details, text="q : {q}".format(q=q)).grid(
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
        z1_b1 = ttk.Button(pg_1, text="View Img histogram",
                           command=lambda: show_gray_img_histogram_dialog(self, self.data[ORIGINAL_IMAGE_GRAY_ARRAY], 'Original Gray Image Histogram'))
        z1_b2 = ttk.Button(pg_2, text="View Img histogram",
                           command=lambda: show_gray_img_histogram_dialog(self, self.data[WATERMARK_IMAGE_GRAY_ARRAY], 'Watermark Gray Image Histogram'))

        z1_l1.grid(row=0, column=0, padx=10, pady=(10, 2), sticky=W)
        z1_l2.grid(row=0, column=0, padx=10, pady=(10, 2), sticky=W)
        z1_b1.grid(row=2, column=0, padx=10, pady=(10, 2), sticky=W)
        z1_b2.grid(row=2, column=0, padx=10, pady=(10, 2), sticky=W)
        gray_img_original.grid(row=1, column=0, padx=10, pady=2, sticky=W)
        gray_img_watermark.grid(row=1, column=0, padx=10, pady=2, sticky=W)

        pg_1.grid(row=0, column=0, padx=10, pady=10, sticky=W+E)
        pg_2.grid(row=0, column=1, padx=10, pady=10, sticky=W+E)

        part_gray.columnconfigure(0, weight=1)
        part_gray.columnconfigure(1, weight=1)

        # part dwt
        part_dwt = ttk.LabelFrame(view, text='Level 1 DWT')

        dwt_o = ttk.LabelFrame(
            part_dwt, text="Original Image DWT coefficients")
        dwt_m = ttk.LabelFrame(
            part_dwt, text="Watermark Image DWT coefficients")

        dwt_o.grid(row=0, column=0, padx=10, pady=10, sticky=W+E)
        dwt_m.grid(row=0, column=1, padx=10, pady=10, sticky=W+E)

        part_dwt.columnconfigure(0, weight=1)
        part_dwt.columnconfigure(1, weight=1)

        dwt_info = get_watermarked_img_with_info(
            self.data[ORIGINAL_IMAGE_GRAY_ARRAY], self.data[WATERMARK_IMAGE_GRAY_ARRAY], k, q)

        LL, (LH, HL, HH) = dwt_info['main_image_dwt']
        mLL, (mLH, mHL, mHH) = dwt_info['mark_image_dwt']
        
        main_coef_array = np.concatenate(
            (
                np.concatenate((np.uint8(LL), np.uint8(LH)), axis=1),
                np.concatenate((np.uint8(HL), np.uint8(HH)), axis=1),
            ),
            axis=0
        )
        mark_coef_array = np.concatenate(
            (
                np.concatenate((np.uint8(mLL), np.uint8(mLH)), axis=1),
                np.concatenate((np.uint8(mHL), np.uint8(mHH)), axis=1),
            ),
            axis=0
        )

        # main_coef_array = np.concatenate(
        #     (
        #         np.concatenate((LL, LH), axis=1),
        #         np.concatenate((HL, HH), axis=1),
        #     ),
        #     axis=0
        # )
        # mark_coef_array = np.concatenate(
        #     (
        #         np.concatenate((mLL, mLH), axis=1),
        #         np.concatenate((mHL, mHH), axis=1),
        #     ),
        #     axis=0
        # )

        img_arr_x_0 = Image.fromarray(main_coef_array)
        img_arr_x_m = Image.fromarray(mark_coef_array)

        # TODO change size if needed here
        img_arr_x_0.thumbnail((300, 300), Image.ANTIALIAS)
        img_arr_x_m.thumbnail((300, 300), Image.ANTIALIAS)

        self.dwt_original_array_photo = ImageTk.PhotoImage(img_arr_x_0)
        self.dwt_mark_array_photo = ImageTk.PhotoImage(img_arr_x_m)

        ttk.Label(dwt_o, image=self.dwt_original_array_photo).grid(
            row=0, column=0, columnspan=2, padx=10, pady=2, sticky=W)
        ttk.Label(dwt_m, image=self.dwt_mark_array_photo).grid(
            row=0, column=0, columnspan=2, padx=10, pady=2, sticky=W)

        z2_l1 = ttk.Label(dwt_o, text="View Histograms...")
        z2_b1 = ttk.Button(dwt_o, text="LL",
                           command=lambda: show_gray_img_histogram_dialog(self, LL, 'Histogram of Original Image LL Band'))
        z2_b2 = ttk.Button(dwt_o, text="LH",
                           command=lambda: show_gray_img_histogram_dialog(self, LH, 'Histogram of Original Image LH Band'))
        z2_b3 = ttk.Button(dwt_o, text="HL",
                           command=lambda: show_gray_img_histogram_dialog(self, HL, 'Histogram of Original Image HL Band'))
        z2_b4 = ttk.Button(dwt_o, text="HH",
                           command=lambda: show_gray_img_histogram_dialog(self, HH, 'Histogram of Original Image HH Band'))

        z2_l1.grid(row=1, column=0, columnspan=2, padx=2, pady=4, sticky=W)
        z2_b1.grid(row=2, column=0, padx=2, pady=2, sticky=W+E)
        z2_b2.grid(row=2, column=1, padx=(2, 12), pady=2, sticky=W+E)
        z2_b3.grid(row=3, column=0, padx=2, pady=2, sticky=W+E)
        z2_b4.grid(row=3, column=1, padx=(2, 12), pady=2, sticky=W+E)

        z3_l1 = ttk.Label(dwt_m, text="View Histograms...")
        z3_b1 = ttk.Button(dwt_m, text="LL",
                           command=lambda: show_gray_img_histogram_dialog(self, mLL, 'Histogram of Watermark Image LL Band'))
        z3_b2 = ttk.Button(dwt_m, text="LH",
                           command=lambda: show_gray_img_histogram_dialog(self, mLH, 'Histogram of Watermark Image LH Band'))
        z3_b3 = ttk.Button(dwt_m, text="HL",
                           command=lambda: show_gray_img_histogram_dialog(self, mHL, 'Histogram of Watermark Image HL Band'))
        z3_b4 = ttk.Button(dwt_m, text="HH",
                           command=lambda: show_gray_img_histogram_dialog(self, mHH, 'Histogram of Watermark Image HH Band'))

        z3_l1.grid(row=1, column=0, columnspan=2, padx=2, pady=4, sticky=W)
        z3_b1.grid(row=2, column=0, padx=2, pady=2, sticky=W+E)
        z3_b2.grid(row=2, column=1, padx=(2, 12), pady=2, sticky=W+E)
        z3_b3.grid(row=3, column=0, padx=2, pady=2, sticky=W+E)
        z3_b4.grid(row=3, column=1, padx=(2, 12), pady=2, sticky=W+E)

        # blend
        part_blend = ttk.LabelFrame(view, text='Embeding (Alpha Blend)')

        ttk.Label(part_blend, text="The watermark LL band will be embeded into original image LL band with k and q ratios and then the watermarked image will be created.").grid(
            row=0, column=0, padx=10, pady=2, sticky=W)
        ttk.Label(part_blend, text="Alpha blended LL band").grid(
            row=1, column=0, padx=10, pady=2, sticky=W)

        marked_LL_img_a = Image.fromarray(dwt_info['marked_LL'])
        water_marked_img_a = Image.fromarray(
            dwt_info['water_marked_img_array'])

        # TODO change size if needed here
        marked_LL_img_a.thumbnail((200, 200), Image.ANTIALIAS)
        water_marked_img_a.thumbnail((200, 200), Image.ANTIALIAS)

        self.marked_LL_img_a_photo = ImageTk.PhotoImage(marked_LL_img_a)
        self.water_marked_img_a_photo = ImageTk.PhotoImage(water_marked_img_a)

        ttk.Label(part_blend, image=self.marked_LL_img_a_photo).grid(
            row=2, column=0, columnspan=2, padx=10, pady=2, sticky=W)
        ttk.Label(part_blend, text="Water Marked Image").grid(
            row=3, column=0, padx=10, pady=2, sticky=W)
        ttk.Label(part_blend, image=self.water_marked_img_a_photo).grid(
            row=4, column=0, columnspan=2, padx=10, pady=2, sticky=W)

        # nav
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
