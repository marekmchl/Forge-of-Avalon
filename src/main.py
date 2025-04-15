from ui_elements import Attribute, Window, Line
from state import make_updatable, state_dict
from attribute_modification import inc_str, dec_str, inc_end, dec_end, inc_dex, dec_dex, inc_spi, dec_spi, inc_per, dec_per, inc_pra, dec_pra


def main():
    win = Window("Forge of Avalon")
    state = make_updatable(win, state_dict)

    lvl = Line(win, "Level", state["Level"])
    lvl.grid(row = 0, column = 0)

    atr = Attribute(win, "Strength", state["Attributes"]["Strength"],inc_str, dec_str)
    atr.grid(row = 1, column = 0)

    atr = Attribute(win, "Endurance", state["Attributes"]["Endurance"],inc_end, dec_end)
    atr.grid(row = 2, column = 0)

    atr = Attribute(win, "Dexterity", state["Attributes"]["Dexterity"],inc_dex, dec_dex)
    atr.grid(row = 3, column = 0)

    atr = Attribute(win, "Spirituality", state["Attributes"]["Spirituality"],inc_spi, dec_spi)
    atr.grid(row = 4, column = 0)

    atr = Attribute(win, "Perception", state["Attributes"]["Perception"],inc_per, dec_per)
    atr.grid(row = 5, column = 0)

    atr = Attribute(win, "Practicality", state["Attributes"]["Practicality"],inc_pra, dec_pra)
    atr.grid(row = 6, column = 0)

    win.mainloop()

if __name__ == "__main__":
    main()
