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
        
        image_cv2 = cv2.imread("src/package/resources/img/test_images/image.png")
        mark_cv2 = cv2.imread("src/package/resources/img/test_images/mark.png")
        
        img_x = cv2.imread("src/package/resources/img/test_images/image.png")
        b, g, r = cv2.split(img_x)
        
        items = embedWatermarkGrayScale(image,mark)
        
        imagekkk = addWaterMark(image_cv2,mark_cv2)
        img_kkkk = Image.fromarray(np.uint8(imagekkk))
        
        water_mark_done = extractWatermark(image_cv2,imagekkk)
        water_mark_done_kkkk = Image.fromarray(np.uint8(water_mark_done))
        
   
        
        img1 = ImageTk.PhotoImage(items[0].resize((200,200), Image.ANTIALIAS))
        img2 = ImageTk.PhotoImage(items[1].resize((200,200), Image.ANTIALIAS))
        img3 = ImageTk.PhotoImage(items[2].resize((200,200), Image.ANTIALIAS))
        
        
        img_y = cv2.merge((r,g,b))
        # img_b = np.stack([b, np.zeros_like(b), np.zeros_like(b)], axis=-1)
        img_b = np.stack([np.zeros_like(b), b, np.zeros_like(b)], axis=-1)
        # img_b = np.stack([np.zeros_like(b), np.zeros_like(b), b], axis=-1)
        
       
        
        img_z = Image.fromarray(img_y)
        img_z_tk = ImageTk.PhotoImage(image=img_kkkk.resize((200,200), Image.ANTIALIAS))
        img_zzz_tk = ImageTk.PhotoImage(image=water_mark_done_kkkk.resize((200,200), Image.ANTIALIAS))
        
        img_label_1 = Label(self, image=img1)
        img_label_1.image = img1
        img_label_2 = Label(self, image=img2)
        img_label_2.image = img2
        img_label_3 = Label(self, image=img3)
        img_label_3.image = img3
        
        img_label_4 = Label(self, image=img_z_tk)
        img_label_4.image = img_z_tk
        
        img_label_5 = Label(self, image=img_zzz_tk)
        img_label_5.image = img_zzz_tk
        
        img_label_1.grid(row = 0, column = 0, sticky = W, pady = 2)
        img_label_2.grid(row = 0, column = 1, sticky = W, pady = 2)
        img_label_3.grid(row = 0, column = 2, sticky = W, pady = 2)
        
        img_label_4.grid(row = 1, column = 1, sticky = W, pady = 2)
        img_label_5.grid(row = 1, column = 2, sticky = W, pady = 2)
        
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
    
    
    




# class HomePage(tk.Frame):
#     def __init__(self, parent, container):
#         super().__init__(container)

#         #label = tk.Label(self, text="Home Page", font=('Times', '20'))
#         #label.pack(pady=0, padx=0)

#         # CODE FOR THIS PAGE
        
#         # this will create a label widget
#         l1 = Label(self, text = "Height")
#         l2 = Label(self, text = "Width")
#         l3 = Label(self, text = "third")
        
#         image = Image.open("src/package/resources/img/test_images/image.png")
#         mark = Image.open("src/package/resources/img/test_images/mark.png")
        
#         image_cv2 = cv2.imread("src/package/resources/img/test_images/image.png")
#         mark_cv2 = cv2.imread("src/package/resources/img/test_images/mark.png")
        
#         items = embedWatermarkGrayScale(image,mark)
        
        
        
#         img1 = ImageTk.PhotoImage(items[0].resize((200,200), Image.ANTIALIAS))
#         img2 = ImageTk.PhotoImage(items[1].resize((200,200), Image.ANTIALIAS))
#         img3 = ImageTk.PhotoImage(items[2].resize((200,200), Image.ANTIALIAS))
        
#         img_x = cv2.imread("src/package/resources/img/test_images/image.png")
#         b, g, r = cv2.split(img_x)
#         img_y = cv2.merge((r,g,b))
#         # img_b = np.stack([b, np.zeros_like(b), np.zeros_like(b)], axis=-1)
#         img_b = np.stack([np.zeros_like(b), b, np.zeros_like(b)], axis=-1)
#         # img_b = np.stack([np.zeros_like(b), np.zeros_like(b), b], axis=-1)
        
#         img_z = Image.fromarray(img_b)
#         img_z_tk = ImageTk.PhotoImage(image=img_z)
        
#         img_label_1 = Label(self, image=img1)
#         img_label_1.image = img1
#         img_label_2 = Label(self, image=img2)
#         img_label_2.image = img2
#         img_label_3 = Label(self, image=img3)
#         img_label_3.image = img3
        
#         img_label_4 = Label(self, image=img_z_tk)
#         img_label_4.image = img_z_tk
        
#         img_label_1.grid(row = 0, column = 0, sticky = W, pady = 2)
#         img_label_2.grid(row = 0, column = 1, sticky = W, pady = 2)
#         img_label_3.grid(row = 0, column = 2, sticky = W, pady = 2)
        
#         img_label_4.grid(row = 1, column = 2, sticky = W, pady = 2)
        
#         # img_label_1.pack()
#         # img_label_2.pack()
#         # img_label_3.pack()
        
        
#         extracted_mark = extractWatermarkGrayScale(image,items[2])
#         img_extrac = ImageTk.PhotoImage(extracted_mark.resize((200,200), Image.ANTIALIAS))
#         img_extrac_label = Label(self, image=img_extrac)
#         img_extrac_label.image = img_extrac
#         img_extrac_label.grid(row = 1, column = 0, sticky = W, pady = 2)
        
#         # grid method to arrange labels in respective
#         # rows and columns as specified
        
#         # l1.grid(row = 0, column = 0, sticky = W, pady = 2)
#         # l2.grid(row = 1, column = 0, sticky = W, pady = 2)
#         # l3.grid(row = 0, column = 1, sticky = W, pady = 2)
        
        
        



#     def create_menubar(self, parent):
#         menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

#         # Filemenu
#         filemenu = Menu(menubar, tearoff=0, relief=RAISED,
#                         activebackground="#026AA9")
#         menubar.add_cascade(label="File", menu=filemenu)
#         filemenu.add_command(
#             label="New Project", command=lambda: parent.show_frame(parent.Validation))
#         filemenu.add_command(
#             label="Close", command=lambda: parent.show_frame(parent.HomePage))
#         filemenu.add_separator()
#         filemenu.add_command(label="Exit", command=parent.quit)

#         # proccessing menu
#         processing_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Validation", menu=processing_menu)
#         processing_menu.add_command(label="validate")
#         processing_menu.add_separator()

#         # help menu
#         help_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Help", menu=help_menu)
#         help_menu.add_command(label="About", command=U.about)
#         help_menu.add_separator()

#         return menubar
