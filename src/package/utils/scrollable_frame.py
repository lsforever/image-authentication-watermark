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
        self.canvas.bind("<Configure>", self.adjust_size)

        #self.scrollable_frame.bind( "<Configure>", self.adjust_size)
        self.flag = False
        self.flag_size = 0

    # This one does the trick for keeping canvas_frame width height expanding

    def adjust_size(self, event):
        self.canvas.itemconfig(self.canvas_frame, width=event.width)

        # if event.height > self.scrollable_frame.winfo_height():
        #     self.flag = True
        #     self.canvas.itemconfig(self.canvas_frame, height=event.height)
        # else:
        #     if self.flag == True:
        #         self.flag = False
                #self.canvas.itemconfig(self.canvas_frame, height=-1)


# self.scrollframe.bind('<Enter>', self._bound_to_mousewheel)
#     self.scrollframe.bind('<Leave>', self._unbound_to_mousewheel)

#     return None

# def _bound_to_mousewheel(self, event):
#     self.canv.bind_all("<MouseWheel>", self._on_mousewheel)

# def _unbound_to_mousewheel(self, event):
#     self.canv.unbind_all("<MouseWheel>")

# def _on_mousewheel(self, event):
#     self.canv.yview_scroll(int(-1*(event.delta/120)), "units")
