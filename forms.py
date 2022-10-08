from tkinter import *
from tkinter.filedialog import askopenfilename
from imageoperator import ImageProcessor


class Window:
    def __init__(self, master):
        self.filename = "no file selected"
        self.image_processor = ImageProcessor()
        self.horizontal_options = {"Left": 0, "Center": 0.5, "Right": 1}
        self.vertical_options = {"Top": 0, "Middle": 0.5, "Bottom": 1}
        self.horizontal_var = StringVar()
        self.vertical_var = StringVar()

        # Label for file
        self.csvfile = Label(master, text="File:")
        self.csvfile.grid(row=1, column=0, pady=10, padx=10, sticky=E)

        # Dynamic label for filename
        self.bar = Label(master, text=self.filename)
        self.bar.grid(row=1, column=1, pady=10, padx=10, sticky=W)

        # Watermark text entry
        Label(master, text="Watermark text:").grid(row=5, column=0, pady=10, padx=10, sticky=E)
        self.watermark = Entry(master)
        self.watermark.grid(row=5, column=1, pady=10, padx=10, sticky=W)

        # Position selectors
        Label(master, text="Horizontal position:").grid(row=6, column=0, pady=10, padx=10, sticky=E)
        self.horizontal_var.set("Left")
        option_horizontal = OptionMenu(
            master,
            self.horizontal_var,
            *self.horizontal_options.keys()
        )
        option_horizontal.grid(column=1, row=6, columnspan=2, pady=10, padx=10,  sticky=W)

        Label(master, text="Vertical position:").grid(row=12, column=0, pady=10, padx=10, sticky=E)
        self.vertical_var.set("Top")
        option_vertical = OptionMenu(
            master,
            self.vertical_var,
            *self.vertical_options.keys()
        )
        option_vertical.grid(column=1, row=12,  columnspan=2, pady=10, padx=10,  sticky=W)

        # Buttons
        self.process_button = Button(
            master,
            text="Process and save",
            command=self.place_watermark,
            padx=5,
            pady=5
        )
        self.process_button.grid(row=15, column=1, columnspan=2, pady=10, padx=10)
        self.browse_button = Button(
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
        self.filename = askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
        if self.filename:
            self.bar["text"] = self.filename

    def place_watermark(self) -> None:
        """
        Get information for form and places watermark in picture using class ImageProcessor
        """
        text = self.watermark.get()
        if text != "":
            horizontal_align = self.horizontal_options[self.horizontal_var.get()]
            vertical_align = self.vertical_options[self.vertical_var.get()]
            self.image_processor.add_watermark(
                text,
                filename=self.filename,
                pos_x=horizontal_align,
                pos_y=vertical_align
            )
        else:
            self.image_processor.add_watermark(
                "Teste",
                filename=self.filename
            )
