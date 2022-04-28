from src.package.gui.app import App
import tkinter as tk


def main():
    app = App()
    app.eval('tk::PlaceWindow . center')
    app.mainloop()


main()