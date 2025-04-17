from tkinter import BOTH, Button, Tk, Frame, Label
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
    def __init__(self, master, name, value_var, name_width, percentage = False):
        super().__init__(master)
        self.configure(bg = settings["colors"]["section_bg"])
        self.name_label = Label(self, text = name, anchor = "w", bg = settings["colors"]["section_bg"], fg = settings["colors"]["line_fg"])
        self.name_label.configure(width = name_width)
        self.name_label.pack(side = LEFT, fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
        if value_var != None:
            if percentage:
                self.value_label = Frame(self, bg = settings["colors"]["section_bg"])
                Label(self.value_label, textvariable = value_var, bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"]).pack(side = LEFT)
                Label(self.value_label, text = "%", bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"]).pack(side = RIGHT)
            else:
                self.value_label = Label(self, textvariable = value_var, bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"])
            self.value_label.pack(side = RIGHT, fill = "none", expand = False, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

class Attribute(Frame):
    def __init__(self, master, name, value_var, inc_func, dec_func):
        super().__init__(master)
        self.configure(bg = settings["colors"]["section_bg"])

        self.name_label = Label(self, text = name, anchor = "w", bg = settings["colors"]["section_bg"], fg = settings["colors"]["line_fg"])
        self.name_label.configure(width = settings["sizes"]["attribute_name_width"])
        self.name_label.pack(side = LEFT, fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

        self.right_side = Frame(self, bg = settings["colors"]["section_bg"])
        self.right_side.pack(side = RIGHT, fill = "none", expand = False, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
        self.value_label = Label(self.right_side, textvariable = value_var, anchor = "e", bg = settings["colors"]["line_bg"], fg = settings["colors"]["line_fg"])
        self.value_label.grid(row = 0, column = 0, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

        self.add_button = Button(self.right_side, text = "+", bg = settings["colors"]["line_bg"], activebackground = settings["colors"]["line_fg"], fg = settings["colors"]["line_fg"], activeforeground = settings["colors"]["line_bg"], command = inc_func)
        self.add_button.grid(row = 0, column = 1, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

        self.sub_button = Button(self.right_side, text = "-", bg = settings["colors"]["line_bg"], activebackground = settings["colors"]["line_fg"], fg = settings["colors"]["line_fg"], activeforeground = settings["colors"]["line_bg"], command = dec_func)
        self.sub_button.grid(row = 0, column = 2, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

class EquipmentPiece(Frame):
    equipment_memory = {
        "Helmet":"Naked",
        "Cuirass":"Naked",
        "Greaves":"Naked",
        "Boots":"Naked",
        "Gauntlets":"Naked",
        "Ring 1":"Naked",
        "Ring 2":"Naked",
        "Amulet":"Naked",
        "Back":"Naked"
    }

    def __init__(self, master, name, slot):
        super().__init__(master)
        self.configure(bg = settings["colors"]["section_bg"])
        self.name_label = Label(self, text = name, anchor = "w", bg = settings["colors"]["section_bg"], fg = settings["colors"]["line_fg"])
        self.name_label.configure(width = settings["sizes"]["equipment_name_width"])
        self.name_label.pack(side = LEFT, fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

        self.slot = slot
        self.old = None
        self.current = state_dict["Equipment"][self.slot]
        self.current.trace("w", self.apply_equipment_change_effects)

        self.value_box = Combobox(self, textvariable = self.current, width = settings["sizes"]["equipment_selector_width"])
        if self.slot == "Ring 1" or self.slot == "Ring 2":
            self.value_box["values"] = equipment_dict["Ring"]["Piece"]
        else:
            self.value_box["values"] = equipment_dict[self.slot]["Piece"]
        self.value_box.pack(side = RIGHT, fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    def apply_equipment_change_effects(self, *args):
        if self.slot == "Ring 1" or self.slot == "Ring 2":
            slot = "Ring"
        else:
            slot = self.slot

        if self.old != None:
            # Remove old active effects
            for (stat_name, stat_change) in equipment_dict[slot]["Effects"][self.old].items():
                state_dict["Statistics"][stat_name].set(round(state_dict["Statistics"][stat_name].get() - stat_change, 2))

        # Update self.old
        self.old = self.current.get()

        # Apply new effects
        for (stat_name, stat_change) in equipment_dict[slot]["Effects"][self.current.get()].items():
            state_dict["Statistics"][stat_name].set(round(state_dict["Statistics"][stat_name].get() + stat_change, 2))


def get_equipment(master):
    equipment = Frame(master, bg = settings["colors"]["section_bg"])
    EquipmentPiece(equipment, "Helmet", "Helmet").pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Amulet", "Amulet").pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Cuirass", "Cuirass").pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Back", "Back").pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Gauntlets", "Gauntlets").pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Ring", "Ring 1").pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Ring", "Ring 2").pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Greaves", "Greaves").pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    EquipmentPiece(equipment, "Boots", "Boots").pack(padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    return equipment

def get_attributes(master):
    attributes = Frame(master, bg = settings["colors"]["section_bg"])
    atr = Attribute(attributes, "Strength", state_dict["Attributes"]["Strength"],inc_str, dec_str)
    atr.pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    atr = Attribute(attributes, "Endurance", state_dict["Attributes"]["Endurance"],inc_end, dec_end)
    atr.pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    atr = Attribute(attributes, "Dexterity", state_dict["Attributes"]["Dexterity"],inc_dex, dec_dex)
    atr.pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    atr = Attribute(attributes, "Spirituality", state_dict["Attributes"]["Spirituality"],inc_spi, dec_spi)
    atr.pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    atr = Attribute(attributes, "Perception", state_dict["Attributes"]["Perception"],inc_per, dec_per)
    atr.pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    atr = Attribute(attributes, "Practicality", state_dict["Attributes"]["Practicality"],inc_pra, dec_pra)
    atr.pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    return attributes

def get_statistics(master):
    statistics = Frame(master, bg = settings["colors"]["section_bg"])

    left_half = Frame(statistics, bg = settings["colors"]["section_bg"])
    left_half.pack(side = LEFT, fill = BOTH, expand = True)

    left_1 = Frame(left_half, bg = settings["colors"]["section_bg"])
    left_1.pack(fill = BOTH, expand = True, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(left_1, "Health", state_dict["Statistics"]["Health"], settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_1, "Mana", state_dict["Statistics"]["Mana"], settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_1, "Stamina", state_dict["Statistics"]["Stamina"], settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_1, "Encumbrance Limit", state_dict["Statistics"]["Encumbrance Limit"], settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    left_2 = Frame(left_half, bg = settings["colors"]["section_bg"])
    left_2.pack(fill = BOTH, expand = True, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(left_2, "Armor", state_dict["Statistics"]["Armor"], settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_2, "Armor Weight Multiplier", state_dict["Statistics"]["Armor Weight Multiplier"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    left_3 = Frame(left_half, bg = settings["colors"]["section_bg"])
    left_3.pack(fill = BOTH, expand = True, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(left_3, "Mana Regeneration/s", state_dict["Statistics"]["Mana Regeneration/s"], settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_3, "Stamina Regeneration/s", state_dict["Statistics"]["Stamina Regeneration/s"], settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_3, "Stamina Cost", state_dict["Statistics"]["Stamina Cost"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_3, "Mana Cost", state_dict["Statistics"]["Mana Cost"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    left_4 = Frame(left_half, bg = settings["colors"]["section_bg"])
    left_4.pack(fill = BOTH, expand = True, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(left_4, "Critical Chance", state_dict["Statistics"]["Critical Chance"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_4, "Magic Critical Chance", state_dict["Statistics"]["Magic Critical Chance"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_4, "Ranged Critical Chance", state_dict["Statistics"]["Ranged Critical Chance"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    left_5 = Frame(left_half, bg = settings["colors"]["section_bg"])
    left_5.pack(fill = BOTH, expand = True, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(left_5, "Critical Damage", state_dict["Statistics"]["Critical Damage"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(left_5, "Weak Spot Damage", state_dict["Statistics"]["Weak Spot Damage"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    right_half = Frame(statistics, bg = settings["colors"]["section_bg"])
    right_half.pack(side = RIGHT)

    right_1 = Frame(right_half, bg = settings["colors"]["section_bg"])
    right_1.pack(fill = BOTH, expand = True, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(right_1, "Melee Damage", state_dict["Statistics"]["Melee Damage"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_1, "Ranged Damage", state_dict["Statistics"]["Ranged Damage"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_1, "Spell Damage", state_dict["Statistics"]["Spell Damage"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_1, "Attack Speed", state_dict["Statistics"]["Attack Speed"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    right_2 = Frame(right_half, bg = settings["colors"]["section_bg"])
    right_2.pack(fill = BOTH, expand = True, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(right_2, "Sneak Damage", state_dict["Statistics"]["Sneak Damage"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_2, "Noise & Visibility", state_dict["Statistics"]["Noise"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    right_3 = Frame(right_half, bg = settings["colors"]["section_bg"])
    right_3.pack(fill = BOTH, expand = True, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(right_3, "Price of bought goods", state_dict["Statistics"]["Price of bought goods"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_3, "Price of sold goods", state_dict["Statistics"]["Price of sold goods"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_3, "", None, settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_3, "", None, settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    right_4 = Frame(right_half, bg = settings["colors"]["section_bg"])
    right_4.pack(fill = BOTH, expand = True, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(right_4, "Alchemy Bonus", state_dict["Statistics"]["Alchemy Bonus"], settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_4, "Cooking Bonus", state_dict["Statistics"]["Cooking Bonus"], settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_4, "Handcrafting Bonus", state_dict["Statistics"]["Handcrafting Bonus"], settings["sizes"]["statistic_name_width"]).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    right_5 = Frame(right_half, bg = settings["colors"]["section_bg"])
    right_5.pack(fill = BOTH, expand = True, padx = settings["sizes"]["section_padding"], pady = settings["sizes"]["section_padding"])
    Line(right_5, "Lifesteal", state_dict["Statistics"]["Lifesteal"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])
    Line(right_5, "Movement Speed Multiplier", state_dict["Statistics"]["Movement Speed Multiplier"], settings["sizes"]["statistic_name_width"], True).pack(fill = BOTH, expand = True, padx = settings["sizes"]["line_padding"], pady = settings["sizes"]["line_padding"])

    return statistics
