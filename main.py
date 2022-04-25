from src.package.gui.app import App
import tkinter as tk



def main():
    splash_root = tk()
    splash_root.title("Welcome to: Start My Apps!")
    splash_root.geometry("700x700")

    splash_label = tk.Label(
    splash_root, text="Welcome to: Start My Apps!", font='times 20 bold', bg="white")
    splash_label.pack(pady=20)

    splash_root.after(5000,splash_root.destroy) #after(ms,func)
    splash_root.mainloop()
    app = App()
    app.mainloop()


main()