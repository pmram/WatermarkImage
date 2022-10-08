from tkinter import *
from tkinter import ttk

from forms import Window

# Basic GUI configuration
root = Tk()
root.title("Watermarking tool")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Set window layout and behaviour
window = Window(mainframe)
root.mainloop()
