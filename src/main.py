from tkinter import Frame
from tkinter.constants import BOTH, BOTTOM, TOP
from ui_elements import Window, Line, get_attributes, get_statistics, get_equipment, get_skills
from state import make_updatable, state_dict
from settings import settings


def main():
    win = Window("Forge of Avalon")
    make_updatable(win, state_dict)

    left = Frame(win, bg = settings["colors"]["window_bg"])
    left.grid(row = 0, column = 0, padx = settings["sizes"]["window_padding"], pady = settings["sizes"]["window_padding"])

    lvl = Line(left, "Level", state_dict["Level"], settings["sizes"]["level_name_width"])
    lvl.pack(expand = True, fill = BOTH, side = TOP, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])

    attributes = get_attributes(left)
    attributes.pack(expand = True, fill = BOTH, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])

    equipment = get_equipment(left)
    equipment.pack(expand = True, fill = BOTH, side = BOTTOM, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])

    middle = get_statistics(win)
    middle.grid(row = 0, column = 1, pady = settings["sizes"]["window_padding"])

    right = get_skills(win)
    right.grid(row = 0, column = 2, padx = settings["sizes"]["window_padding"], pady = settings["sizes"]["window_padding"])

    win.mainloop()

if __name__ == "__main__":
    main()
