import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('300x200')
root.title('Imagem falsa')

# download button


def download_clicked():
    showinfo(
        title='CLICA AQUI VAI!!!',
        message='BOTAO CLICADO'
    )


download_icon = root.iconbitmap(file="J/codes/python/assets/download")
download_button = ttk.Button(
    root,
    image=download_icon,
    command=download_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop(Tk())
