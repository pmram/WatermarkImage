from tkinter import *
import customtkinter
from tkinter.filedialog import askopenfilename
from imageoperator import ImageProcessor
import os


class Window:
    def __init__(self, master):
        self.filename = "no file selected"
        self.filepath = ""
        self.font_size = IntVar()
        self.image_processor = ImageProcessor()
        self.horizontal_options = {"Left": 0, "Center": 0.5, "Right": 1}
        self.vertical_options = {"Top": 0, "Middle": 0.5, "Bottom": 1}
        self.horizontal_var = StringVar()
        self.vertical_var = StringVar()

        # Label for file
        self.csvfile = customtkinter.CTkLabel(master, text="File:")
        self.csvfile.grid(row=1, column=0, pady=10, padx=10, sticky=E)

        # Dynamic label for filename
        self.bar = customtkinter.CTkLabel(master, text=self.filename)
        self.bar.grid(row=1, column=1, pady=10, padx=10, sticky=W)

        # Watermark text entry
        customtkinter.CTkLabel(master, text="Watermark text:").grid(row=5, column=0, pady=10, padx=10, sticky=E)
        self.watermark = Entry(master)
        self.watermark.grid(row=5, column=1, pady=10, padx=10, sticky=W)

        # Position selectors
        customtkinter.CTkLabel(master, text="Horizontal position:").grid(row=6, column=0, pady=10, padx=10, sticky=E)
        self.horizontal_var.set("Left")
        option_horizontal = customtkinter.CTkOptionMenu(
            master=master,
            variable=self.horizontal_var,
            values=list(self.horizontal_options.keys())
        )
        option_horizontal.grid(column=1, row=6, columnspan=2, pady=10, padx=10,  sticky=W)

        customtkinter.CTkLabel(master, text="Vertical position:").grid(row=12, column=0, pady=10, padx=10, sticky=E)
        self.vertical_var.set("Top")
        option_vertical = customtkinter.CTkOptionMenu(
            master=master,
            variable=self.vertical_var,
            values=list(self.vertical_options.keys())
        )
        option_vertical.grid(column=1, row=12,  columnspan=2, pady=10, padx=10,  sticky=W)

        # Font size selector
        customtkinter.CTkLabel(master, text="Font size:").grid(row=13, column=0, pady=10, padx=10, sticky=E)
        slider = customtkinter.CTkSlider(master=master, from_=0, to=100, variable=self.font_size)
        slider.grid(column=1, row=13,  columnspan=2, pady=10, padx=10,  sticky=W)

        # Buttons
        self.process_button = customtkinter.CTkButton(
            master=master,
            text="Process and save",
            command=self.place_watermark,
            padx=5,
            pady=5
        )
        self.process_button.grid(row=15, column=0, columnspan=4, pady=10, padx=10)
        self.browse_button = customtkinter.CTkButton(
            master,
            text="Browse",
            command=self.browse_image,
            padx=5,
            pady=5
        )
        self.browse_button.grid(row=1, column=3, pady=10, padx=10)

    def browse_image(self) -> None:
        """
        Configures and opens file manager to search for images
        """
        Tk().withdraw()
        filetypes = (
            ('Image files', '*.jpg *.jpeg *.png *.bmp'),
            ('All files', '*.*')
        )
        self.filepath = askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
        if self.filepath:
            self.filename = os.path.basename(self.filepath)
            self.bar.configure(text=self.filename)

    def place_watermark(self) -> None:
        """
        Get information for form and places watermark in picture using class ImageProcessor
        """
        text = self.watermark.get()
        if text != "":
            horizontal_align = self.horizontal_options[self.horizontal_var.get()]
            vertical_align = self.vertical_options[self.vertical_var.get()]
            font_size_percentage = self.font_size.get()
            self.image_processor.add_watermark(
                text,
                filepath=self.filepath,
                pos_x=horizontal_align,
                pos_y=vertical_align,
                size=0.1 * (font_size_percentage / 100)
            )
        else:
            self.image_processor.add_watermark(
                "Teste",
                filepath=self.filepath
            )
