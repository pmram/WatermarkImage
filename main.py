from tkinter import *
import customtkinter
from forms import Window

# Basic GUI configuration
root = customtkinter.CTk()
root.set_appearance_mode("light")
root.title("Watermarking tool")
window_width = 550
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

mainframe = customtkinter.CTkFrame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Set window layout and behaviour
window = Window(mainframe)
root.mainloop()
