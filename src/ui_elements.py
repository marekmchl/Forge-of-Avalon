from tkinter import BOTH, Button, Tk, Frame, Label
from tkinter.constants import LEFT, RIGHT
from settings import settings

class Window(Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry(f"{settings["sizes"]["window_width"]}x{settings["sizes"]["window_height"]}")
        self.configure(bg=settings["colors"]["window_bg"])
        self.resizable(width=False, height=False)

class Line(Frame):
    def __init__(self, master, name, value_var):
        super().__init__(master)
        self.configure(bg = settings["colors"]["section_bg"])
        self.name_label = Label(self, text = name, justify = LEFT,bg = settings["colors"]["section_bg"], fg = settings["colors"]["line_fg"])
        self.name_label.pack(side = LEFT, fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
        self.value_label = Label(self, textvariable = value_var, justify = RIGHT,bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"])
        self.value_label.pack(side = RIGHT, fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

class Attribute(Frame):
    def __init__(self, master, name, value_var, inc_func, dec_func):
        super().__init__(master)
        self.configure(bg = settings["colors"]["section_bg"])

        self.name_label = Label(self, text = name, justify = LEFT,bg = settings["colors"]["section_bg"], fg = settings["colors"]["line_fg"])
        # self.name_label.pack(side = LEFT, fill = BOTH, expand = True)
        self.name_label.grid(row = 0, column = 0, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

        self.value_label = Label(self, textvariable = value_var, justify = RIGHT,bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"])
        # self.value_label.pack(side = RIGHT, fill = BOTH)
        self.value_label.grid(row = 0, column = 1, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

        self.add_button = Button(self, text = "+", bg = settings["colors"]["line_bg"], activebackground = settings["colors"]["line_fg"], fg = settings["colors"]["line_fg"], activeforeground = settings["colors"]["line_bg"], command = inc_func)
        # self.add_button.pack(side = RIGHT, fill = BOTH)
        self.add_button.grid(row = 0, column = 2, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

        self.sub_button = Button(self, text = "-", bg = settings["colors"]["line_bg"], activebackground = settings["colors"]["line_fg"], fg = settings["colors"]["line_fg"], activeforeground = settings["colors"]["line_bg"], command = dec_func)
        # self.sub_button.pack(side = RIGHT, fill = BOTH)
        self.sub_button.grid(row = 0, column = 3, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
