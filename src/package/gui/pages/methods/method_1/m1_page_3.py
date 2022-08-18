import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2
from tkinter import filedialog
from src.package.domain.img_func import get_extracted_mark_with_info

from src.package.utils.scrollable_frame import ScrollableFrame

from src.package.utils.constants import *
from src.package.utils.extentions import get_resize_shape_with_aspect_ratio, show_gray_img_histogram_dialog

# ---------------------------------------- M1_Page_3 FRAME / CONTAINER ------------------------------------------------------------------------


class M1_Page_3(tk.Frame):

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

        # part details (p1)
        part_details = ttk.LabelFrame(view, text='Watermark Extraction')
        l1 = ttk.Label(
            part_details, text="The original image and watermarked image will be transformed by DWT. Their LL band coefficients will be used to extract watermark. k and q will be used for reverse alpha blending")
        l1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        part_details.bind("<Configure>", lambda e:
                          l1.configure(wraplength=e.width - 60)
                          )

        # part inputs (p2)
        part_inputs = ttk.LabelFrame(view, text='Input Items')
        p2_pg_1 = ttk.LabelFrame(part_inputs, text="Original Grayscale Image")
        p2_pg_2 = ttk.LabelFrame(
            part_inputs, text="Watermarked Grayscale Image")

        original_img_g_arr = Image.fromarray(
            self.data[ORIGINAL_IMAGE_GRAY_ARRAY])
        watermarked_img_g_arr = Image.fromarray(
            self.data[WATERMARKED_IMAGE_GRAY_ARRAY])
        original_img_g_arr = original_img_g_arr.resize(get_resize_shape_with_aspect_ratio(
            original_img_g_arr.size, max_image_show_size), Image.ANTIALIAS)
        watermarked_img_g_arr = watermarked_img_g_arr.resize(get_resize_shape_with_aspect_ratio(
            watermarked_img_g_arr.size, max_image_show_size), Image.ANTIALIAS)

        self.original_img_g_arr_photo = ImageTk.PhotoImage(original_img_g_arr)
        self.watermarked_img_g_arr_photo = ImageTk.PhotoImage(
            watermarked_img_g_arr)
        original_img_g_arr_p_lbl = ttk.Label(
            p2_pg_1, image=self.original_img_g_arr_photo)
        watermarked_img_g_arr_p_lbl = ttk.Label(
            p2_pg_2, image=self.watermarked_img_g_arr_photo)
        p1_b1 = ttk.Button(p2_pg_1, text="View histogram",
                           command=lambda: show_gray_img_histogram_dialog(self, self.data[ORIGINAL_IMAGE_GRAY_ARRAY], 'Original Gray Image Histogram'))
        p1_b2 = ttk.Button(p2_pg_2, text="View histogram",
                           command=lambda: show_gray_img_histogram_dialog(self, self.data[WATERMARKED_IMAGE_GRAY_ARRAY], 'Watermarked Gray Image Histogram'))

        p2_pg_1.grid(row=0, column=0, padx=10, pady=10, sticky=W+E)
        p2_pg_2.grid(row=0, column=1, padx=10, pady=10, sticky=W+E)
        part_inputs.columnconfigure(0, weight=1)
        part_inputs.columnconfigure(1, weight=1)
        original_img_g_arr_p_lbl.grid(
            row=0, column=0, padx=10, pady=(10, 2), sticky=W)
        p1_b1.grid(row=1, column=0, padx=10, pady=2, sticky=W)
        watermarked_img_g_arr_p_lbl.grid(
            row=0, column=0, padx=10, pady=(10, 2), sticky=W)
        p1_b2.grid(row=1, column=0, padx=10, pady=2, sticky=W)

        # part dwts (p3)
        part_dwts = ttk.LabelFrame(view, text='DWT transform')
        p3_pg_1 = ttk.LabelFrame(
            part_dwts, text="Original Image DWT coefficients")
        p3_pg_2 = ttk.LabelFrame(
            part_dwts, text="Watermarked Image DWT coefficients")

        k = self.data[ALPHA_BLEND_K].get()
        q = self.data[ALPHA_BLEND_Q].get()
        extracted_info = get_extracted_mark_with_info(
            self.data[ORIGINAL_IMAGE_GRAY_ARRAY], self.data[WATERMARKED_IMAGE_GRAY_ARRAY], k, q)

        LL, (LH, HL, HH) = extracted_info['main_img_dwt']
        mLL, (mLH, mHL, mHH) = extracted_info['water_marked_img_dwt']

        main_coef_array = np.concatenate(
            (
                np.concatenate((LL, np.uint8(LH)), axis=1),
                np.concatenate((np.uint8(HL), np.uint8(HH)), axis=1),
            ),
            axis=0
        )
        mark_coef_array = np.concatenate(
            (
                np.concatenate((mLL, np.uint8(mLH)), axis=1),
                np.concatenate((np.uint8(mHL), np.uint8(mHH)), axis=1),
            ),
            axis=0
        )

        img_arr_x_0 = Image.fromarray(main_coef_array)
        img_arr_x_m = Image.fromarray(mark_coef_array)

        # TODO change size if needed here
        img_arr_x_0.thumbnail((300, 300), Image.ANTIALIAS)
        img_arr_x_m.thumbnail((300, 300), Image.ANTIALIAS)

        self.dwt_original_array_photo = ImageTk.PhotoImage(img_arr_x_0)
        self.dwt_mark_array_photo = ImageTk.PhotoImage(img_arr_x_m)

        ttk.Label(p3_pg_1, image=self.dwt_original_array_photo).grid(
            row=0, column=0, columnspan=2, padx=10, pady=2, sticky=W)
        ttk.Label(p3_pg_2, image=self.dwt_mark_array_photo).grid(
            row=0, column=0, columnspan=2, padx=10, pady=2, sticky=W)

        p3_l1 = ttk.Label(p3_pg_1, text="View Histograms...")
        p3_b1 = ttk.Button(p3_pg_1, text="LL",
                           command=lambda: show_gray_img_histogram_dialog(self, LL, 'Histogram of Original Image LL Band'))
        p3_b2 = ttk.Button(p3_pg_1, text="LH",
                           command=lambda: show_gray_img_histogram_dialog(self, LH, 'Histogram of Original Image LH Band'))
        p3_b3 = ttk.Button(p3_pg_1, text="HL",
                           command=lambda: show_gray_img_histogram_dialog(self, HL, 'Histogram of Original Image HL Band'))
        p3_b4 = ttk.Button(p3_pg_1, text="HH",
                           command=lambda: show_gray_img_histogram_dialog(self, HH, 'Histogram of Original Image HH Band'))

        p3_l1.grid(row=1, column=0, columnspan=2, padx=2, pady=4, sticky=W)
        p3_b1.grid(row=2, column=0, padx=2, pady=2, sticky=W+E)
        p3_b2.grid(row=2, column=1, padx=(2, 12), pady=2, sticky=W+E)
        p3_b3.grid(row=3, column=0, padx=2, pady=2, sticky=W+E)
        p3_b4.grid(row=3, column=1, padx=(2, 12), pady=2, sticky=W+E)

        p3_l1 = ttk.Label(p3_pg_2, text="View Histograms...")
        p3_b1 = ttk.Button(p3_pg_2, text="LL",
                           command=lambda: show_gray_img_histogram_dialog(self, mLL, 'Histogram of Watermarked Image LL Band'))
        p3_b2 = ttk.Button(p3_pg_2, text="LH",
                           command=lambda: show_gray_img_histogram_dialog(self, mLH, 'Histogram of Watermarked Image LH Band'))
        p3_b3 = ttk.Button(p3_pg_2, text="HL",
                           command=lambda: show_gray_img_histogram_dialog(self, mHL, 'Histogram of Watermarked Image HL Band'))
        p3_b4 = ttk.Button(p3_pg_2, text="HH",
                           command=lambda: show_gray_img_histogram_dialog(self, mHH, 'Histogram of Watermarked Image HH Band'))

        p3_l1.grid(row=1, column=0, columnspan=2, padx=2, pady=4, sticky=W)
        p3_b1.grid(row=2, column=0, padx=2, pady=2, sticky=W+E)
        p3_b2.grid(row=2, column=1, padx=(2, 12), pady=2, sticky=W+E)
        p3_b3.grid(row=3, column=0, padx=2, pady=2, sticky=W+E)
        p3_b4.grid(row=3, column=1, padx=(2, 12), pady=2, sticky=W+E)

        ###
        p3_pg_1.grid(row=0, column=0, padx=10, pady=10, sticky=W+E)
        p3_pg_2.grid(row=0, column=1, padx=10, pady=10, sticky=W+E)
        part_dwts.columnconfigure(0, weight=1)
        part_dwts.columnconfigure(1, weight=1)

        # part output (p4)
        part_outputs = ttk.LabelFrame(view, text='Extracted Items')
        p4_pg_1 = ttk.LabelFrame(
            part_outputs, text="Extracted LL Band of watermark")
        p4_pg_2 = ttk.LabelFrame(part_outputs, text="Extracted watermark")

        extracted_LL_arr = Image.fromarray(
            extracted_info['water_mark_coeficient_LL'])
        extracted_watermark_arr = Image.fromarray(
            extracted_info['extracted_watermark_array'])
        # TODO change size if needed here
        extracted_LL_arr.thumbnail((200, 200), Image.ANTIALIAS)
        extracted_watermark_arr.thumbnail((200, 200), Image.ANTIALIAS)

        self.extracted_LL_arr_photo = ImageTk.PhotoImage(extracted_LL_arr)
        self.extracted_watermark_arr_photo = ImageTk.PhotoImage(
            extracted_watermark_arr)
        p4_l1 = ttk.Label(p4_pg_1, image=self.extracted_LL_arr_photo)
        p4_l2 = ttk.Label(p4_pg_2, image=self.extracted_watermark_arr_photo)
        p4_b1 = ttk.Button(p4_pg_1, text="View histogram",
                           command=lambda: show_gray_img_histogram_dialog(self, extracted_info['water_mark_coeficient_LL'], 'Extracted LL band (watermark) Histogram'))
        p4_b2 = ttk.Button(p4_pg_2, text="View histogram",
                           command=lambda: show_gray_img_histogram_dialog(self, extracted_info['extracted_watermark_array'], 'Extracted Watermark Histogram'))

        def save_extracted_image():
            filename = filedialog.asksaveasfilename(
                initialdir="/", title="Select Path", filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg")))
            # TODO extentions auto hedenna hadanna, if: time
            cv2.imwrite(filename, extracted_info['extracted_watermark_array'])

        p4_b3 = ttk.Button(
            p4_pg_2, text="Save Extracted Watermark", command=save_extracted_image)

        p4_pg_1.grid(row=0, column=0, padx=10, pady=10, sticky=W+E+N)
        p4_pg_2.grid(row=0, column=1, padx=10, pady=10, sticky=W+E+N)
        part_outputs.columnconfigure(0, weight=1)
        part_outputs.columnconfigure(1, weight=1)

        p4_l1.grid(row=0, column=0, padx=10, pady=(10, 2), sticky=W)
        p4_b1.grid(row=1, column=0, padx=10, pady=2, sticky=W)
        p4_l2.grid(row=0, column=0, padx=10, pady=(10, 2), sticky=W)
        p4_b2.grid(row=1, column=0, padx=10, pady=2, sticky=W)
        p4_b3.grid(row=2, column=0, padx=10, pady=2, sticky=W)

        # part nav (p5)
        part_nav = ttk.LabelFrame(view, text='Navigate')

        def home():
            parent.show_frame(parent.HomePage)

        def back():
            parent.show_m1_frame(parent.M1_Page_2)

        def next():
            # TODO implement comparision, if: time
            pass

        b1 = ttk.Button(part_nav, text="Home",
                        command=home)
        b2 = ttk.Button(part_nav, text="Back",
                        command=back)
        b3 = ttk.Button(part_nav, text="Comparision",
                        command=next)
        b1.grid(row=0, column=0, pady=5, padx=10)
        b2.grid(row=0, column=1, pady=5, padx=10)
        b3.grid(row=0, column=2, sticky=E, pady=5, padx=10)
        part_nav.columnconfigure(2, weight=1)

        ######################################
        ######################################

        part_details.grid(row=0, column=0, padx=10, pady=10, sticky=E+W)
        part_inputs.grid(row=1, column=0, padx=10, pady=10, sticky=E+W)
        part_dwts.grid(row=2, column=0, padx=10, pady=10, sticky=E+W)
        part_outputs.grid(row=3, column=0, padx=10, pady=10, sticky=E+W)
        part_nav.grid(row=4, column=0, padx=10, pady=10, sticky=E+W+S)
        view.columnconfigure(0, weight=1)
        view.rowconfigure(4, weight=1)

        ######################################
        ######################################
