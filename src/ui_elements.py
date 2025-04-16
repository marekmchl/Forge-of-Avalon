from tkinter import BOTH, X, Button, Tk, Frame, Label
from tkinter.constants import LEFT, RIGHT
from tkinter.ttk import Combobox
from settings import settings
from state import state_dict
from attribute_modification import inc_str, dec_str, inc_end, dec_end, inc_dex, dec_dex, inc_spi, dec_spi, inc_per, dec_per, inc_pra, dec_pra
from equipment import equipment_dict

class Window(Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry(f"{settings["sizes"]["window_width"]}x{settings["sizes"]["window_height"]}")
        self.configure(bg=settings["colors"]["window_bg"])
        self.resizable(width=False, height=False)

class Line(Frame):
    def __init__(self, master, name, value_var, percentage = False):
        super().__init__(master)
        self.configure(bg = settings["colors"]["section_bg"])
        self.name_label = Label(self, text = name, justify = LEFT,bg = settings["colors"]["section_bg"], fg = settings["colors"]["line_fg"])
        self.name_label.pack(side = LEFT, fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
        if value_var != None:
            if percentage:
                self.value_label = Frame(self, bg = settings["colors"]["section_bg"])
                Label(self.value_label, textvariable = value_var, justify = RIGHT,bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"]).pack(side = LEFT)
                Label(self.value_label, text = "%", justify = RIGHT,bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"]).pack(side = RIGHT)
            else:
                self.value_label = Label(self, textvariable = value_var, justify = RIGHT,bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"])
            self.value_label.pack(side = RIGHT, fill = "none", expand = False, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

class Attribute(Frame):
    def __init__(self, master, name, value_var, inc_func, dec_func):
        super().__init__(master)
        self.configure(bg = settings["colors"]["section_bg"])

        self.name_label = Label(self, text = name, anchor = "w", bg = settings["colors"]["section_bg"], fg = settings["colors"]["line_fg"])
        self.name_label.grid(row = 0, column = 0, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

        self.value_label = Label(self, textvariable = value_var, anchor = "e", bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"])
        self.value_label.grid(row = 0, column = 1, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

        self.add_button = Button(self, text = "+", bg = settings["colors"]["line_bg"], activebackground = settings["colors"]["line_fg"], fg = settings["colors"]["line_fg"], activeforeground = settings["colors"]["line_bg"], command = inc_func)
        self.add_button.grid(row = 0, column = 2, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

        self.sub_button = Button(self, text = "-", bg = settings["colors"]["line_bg"], activebackground = settings["colors"]["line_fg"], fg = settings["colors"]["line_fg"], activeforeground = settings["colors"]["line_bg"], command = dec_func)
        self.sub_button.grid(row = 0, column = 3, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

class EquipmentPiece(Frame):
    def __init__(self, master, name, bound_var, input_list):
        super().__init__(master)
        self.configure(bg = settings["colors"]["section_bg"])
        self.name_label = Label(self, text = name, justify = LEFT,bg = settings["colors"]["section_bg"], fg = settings["colors"]["line_fg"])
        self.name_label.pack(side = LEFT, fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
        self.value_box = Combobox(self, textvariable = bound_var, justify = RIGHT)
        self.value_box["values"] = input_list
        self.value_box.pack(side = RIGHT, fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

def get_equipment(master):
    equipment = Frame(master, bg = settings["colors"]["section_bg"])
    EquipmentPiece(equipment, "Helmet", state_dict["Equipment"]["Helmet"], equipment_dict["Helmet"]["Piece"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Amulet", state_dict["Equipment"]["Amulet"], equipment_dict["Helmet"]["Piece"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Cuirass", state_dict["Equipment"]["Cuirass"], equipment_dict["Helmet"]["Piece"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Back", state_dict["Equipment"]["Back"], equipment_dict["Helmet"]["Piece"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Gauntlets", state_dict["Equipment"]["Gauntlets"], equipment_dict["Helmet"]["Piece"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Ring", state_dict["Equipment"]["Ring 1"], equipment_dict["Helmet"]["Piece"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Ring", state_dict["Equipment"]["Ring 2"], equipment_dict["Helmet"]["Piece"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Greaves", state_dict["Equipment"]["Greaves"], equipment_dict["Helmet"]["Piece"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Boots", state_dict["Equipment"]["Boots"], equipment_dict["Helmet"]["Piece"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    return equipment

def get_attributes(master):
    attributes = Frame(master, bg = settings["colors"]["section_bg"])
    atr = Attribute(attributes, "Strength", state_dict["Attributes"]["Strength"],inc_str, dec_str)
    atr.pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    atr = Attribute(attributes, "Endurance", state_dict["Attributes"]["Endurance"],inc_end, dec_end)
    atr.pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    atr = Attribute(attributes, "Dexterity", state_dict["Attributes"]["Dexterity"],inc_dex, dec_dex)
    atr.pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    atr = Attribute(attributes, "Spirituality", state_dict["Attributes"]["Spirituality"],inc_spi, dec_spi)
    atr.pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    atr = Attribute(attributes, "Perception", state_dict["Attributes"]["Perception"],inc_per, dec_per)
    atr.pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    atr = Attribute(attributes, "Practicality", state_dict["Attributes"]["Practicality"],inc_pra, dec_pra)
    atr.pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    return attributes

def get_statistics(master):
    statistics = Frame(master, bg = settings["colors"]["section_bg"])

    left_half = Frame(statistics, bg = settings["colors"]["section_bg"])
    left_half.pack(side = LEFT)

    left_1 = Frame(left_half, bg = settings["colors"]["section_bg"])
    left_1.pack(padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(left_1, "Health", state_dict["Statistics"]["Health"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_1, "Mana", state_dict["Statistics"]["Mana"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_1, "Stamina", state_dict["Statistics"]["Stamina"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_1, "Encumbrance Limit", state_dict["Statistics"]["Encumbrance Limit"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    left_2 = Frame(left_half, bg = settings["colors"]["section_bg"])
    left_2.pack(padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(left_2, "Armor", state_dict["Statistics"]["Armor"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_2, "Armor Weight Multiplier", state_dict["Statistics"]["Armor Weight Multiplier"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    left_3 = Frame(left_half, bg = settings["colors"]["section_bg"])
    left_3.pack(padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(left_3, "Mana Regeneration/s", state_dict["Statistics"]["Mana Regeneration/s"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_3, "Stamina Regeneration/s", state_dict["Statistics"]["Stamina Regeneration/s"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_3, "Stamina & Mana Cost", state_dict["Statistics"]["Stamina and Mana Cost"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    left_4 = Frame(left_half, bg = settings["colors"]["section_bg"])
    left_4.pack(padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(left_4, "Critical Chance", state_dict["Statistics"]["Critical Chance"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_4, "Magic Critical Chance", state_dict["Statistics"]["Magic Critical Chance"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_4, "Ranged Critical Chance", state_dict["Statistics"]["Ranged Critical Chance"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    left_5 = Frame(left_half, bg = settings["colors"]["section_bg"])
    left_5.pack(padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(left_5, "Critical Damage", state_dict["Statistics"]["Critical Damage"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_5, "Weak Spot Damage", state_dict["Statistics"]["Weak Spot Damage"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    right_half = Frame(statistics, bg = settings["colors"]["section_bg"])
    right_half.pack(side = RIGHT)

    right_1 = Frame(right_half, bg = settings["colors"]["section_bg"])
    right_1.pack(padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(right_1, "Melee Damage", state_dict["Statistics"]["Melee Damage"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_1, "Ranged Damage", state_dict["Statistics"]["Ranged Damage"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_1, "Spell Damage", state_dict["Statistics"]["Spell Damage"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_1, "Attack Speed", state_dict["Statistics"]["Attack Speed"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    right_2 = Frame(right_half, bg = settings["colors"]["section_bg"])
    right_2.pack(padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(right_2, "Sneak Damage", state_dict["Statistics"]["Sneak Damage"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_2, "Noise & Visibility", state_dict["Statistics"]["Noise"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    right_3 = Frame(right_half, bg = settings["colors"]["section_bg"])
    right_3.pack(padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(right_3, "Price of bought goods", state_dict["Statistics"]["Price of bought goods"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_3, "Price of sold goods", state_dict["Statistics"]["Price of sold goods"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_3, "", None).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    right_4 = Frame(right_half, bg = settings["colors"]["section_bg"])
    right_4.pack(padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(right_4, "Alchemy Bonus", state_dict["Statistics"]["Alchemy Bonus"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_4, "Cooking Bonus", state_dict["Statistics"]["Cooking Bonus"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_4, "Handcrafting Bonus", state_dict["Statistics"]["Handcrafting Bonus"]).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    right_5 = Frame(right_half, bg = settings["colors"]["section_bg"])
    right_5.pack(padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(right_5, "Lifesteal", state_dict["Statistics"]["Lifesteal"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_5, "Movement Speed Multiplier", state_dict["Statistics"]["Movement Speed Multiplier"], True).pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    return statistics
