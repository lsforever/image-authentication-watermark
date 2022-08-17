from tkinter import *
from tkinter import messagebox


def about():
    messagebox.showinfo('About', "This is a sample Application")
    

def get_resize_shape_with_aspect_ratio(size, max_size):
    w, h = size
    r = w/h
    width = max_size
    height = int(r * width)
    return (width,height)

def get_dpi():
    screen = Tk()
    current_dpi = screen.winfo_fpixels('1i')
    screen.destroy()
    return current_dpi

def show_imag_histogram_dialog():
    pass #TODO