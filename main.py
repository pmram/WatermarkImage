from tkinter import *
import customtkinter
from forms import Window

# Basic GUI configuration
root = customtkinter.CTk()
root.set_appearance_mode("light")
root.title("Watermarking tool")
mainframe = customtkinter.CTkFrame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Set window layout and behaviour
window = Window(mainframe)
root.mainloop()
