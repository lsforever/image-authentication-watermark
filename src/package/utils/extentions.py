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