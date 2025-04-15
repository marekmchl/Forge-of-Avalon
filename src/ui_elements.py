from tkinter import BOTH, Tk, Frame, Label
from tkinter.constants import LEFT, RIGHT
from settings import settings

class Window(Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry(f"{settings["sizes"]["window_width"]}x{settings["sizes"]["window_height"]}")
        self.configure(bg=settings["colors"]["window_bg"])

class Line(Frame):
    def __init__(self, master, name, value_var):
        super().__init__(master)
        self.configure(bg = settings["colors"]["section_bg"])
        self.name_label = Label(self, text = name, justify = LEFT,bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"])
        self.name_label.pack(side = LEFT, fill = BOTH, expand = True)
        self.value_label = Label(self, textvariable = value_var, justify = RIGHT,bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"])
        self.value_label.pack(side = RIGHT, fill = BOTH, expand = True)
