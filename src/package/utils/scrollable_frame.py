import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas_frame = self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # This one does the trick for keeping canvas_frame width height expanding
        self.canvas.bind( "<Configure>", self.adjust_size)
    
    # This one does the trick for keeping canvas_frame width height expanding   
    def adjust_size(self,event):
        # if event.width > self.scrollable_frame.winfo_width():
        #     self.canvas.itemconfig(self.canvas_frame, width=event.width)
        
        self.canvas.itemconfig(self.canvas_frame, width=event.width)
        if event.height > self.scrollable_frame.winfo_height():
            self.canvas.itemconfig(self.canvas_frame, height=event.height)
