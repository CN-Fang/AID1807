import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle


def zhujiemian():
    window = tk.Tk()
    window.title('主界面')
    window.geometry('1600x800')

    canvas = tk.Canvas(window, height = 1000, width = 1200)
    image_file = tk.PhotoImage(file = 'beijing.gif')
    image = canvas.create_image(0, 0, anchor = 'nw', image = image_file)
    canvas.pack()

    window.mainloop()