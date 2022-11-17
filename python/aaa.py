from tkinter import *
from tkinter import ttk

root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.base()
        self.frames_da_tela()
        root.mainloop()

    def base(self):
        self.root.title("INTERFACE BASE")
        self.root.configure(background='lightgreen')
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=1000, height=1000)
        self.root.minsize(width=100, height=100)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.5)


Tk(Application())
