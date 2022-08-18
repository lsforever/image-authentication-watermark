from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


def about():
    messagebox.showinfo('About', "This is a sample Application")


def get_resize_shape_with_aspect_ratio(size, max_size):
    w, h = size
    r = w/h
    width = max_size
    height = int(r * width)
    return (width, height)


def get_dpi():
    screen = Tk()
    current_dpi = screen.winfo_fpixels('1i')
    screen.destroy()
    return current_dpi


def show_gray_img_histogram_dialog(win, gray_image_array, tittle):
    pop = Toplevel(win)
    pop.geometry("550x550")
    pop.title("Histogram View")

    fig = Figure(figsize=(5, 5), dpi=get_dpi())
    plot1 = fig.add_subplot(111)
    plot1.set_title(tittle)
    plot1.hist(gray_image_array.ravel(), 256, (0, 256))
    canvas = FigureCanvasTkAgg(fig,
                               master=pop)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, pop, pack_toolbar=False)
    toolbar.update()
    canvas.get_tk_widget().pack(expand=True)
    toolbar.pack(expand=True)
    win.focus_set()
