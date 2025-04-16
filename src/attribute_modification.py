from state import state_dict, update_level

def inc_str():
    state_dict["Attributes"]["Strength"].set(state_dict["Attributes"]["Strength"].get() + 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() + 1)
    update_level()
    state_dict["Statistics"]["Melee Damage"].set(state_dict["Statistics"]["Melee Damage"].get() + 1)
    state_dict["Statistics"]["Stamina"].set(state_dict["Statistics"]["Stamina"].get() + 3)
    state_dict["Statistics"]["Armor Weight Multiplier"].set(state_dict["Statistics"]["Armor Weight Multiplier"].get() - 1)

def dec_str():
    if state_dict["Attributes"]["Strength"].get() <=1:
        return
    state_dict["Attributes"]["Strength"].set(state_dict["Attributes"]["Strength"].get() - 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() - 1)
    update_level()
    state_dict["Statistics"]["Melee Damage"].set(state_dict["Statistics"]["Melee Damage"].get() - 1)
    state_dict["Statistics"]["Stamina"].set(state_dict["Statistics"]["Stamina"].get() - 3)
    state_dict["Statistics"]["Armor Weight Multiplier"].set(state_dict["Statistics"]["Armor Weight Multiplier"].get() + 1)

def inc_end():
    state_dict["Attributes"]["Endurance"].set(state_dict["Attributes"]["Endurance"].get() + 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() + 1)
    update_level()
    state_dict["Statistics"]["Health"].set(state_dict["Statistics"]["Health"].get() + 8)
    state_dict["Statistics"]["Encumbrance Limit"].set(state_dict["Statistics"]["Encumbrance Limit"].get() + 10)
    state_dict["Statistics"]["Stamina Regeneration/s"].set(round(state_dict["Statistics"]["Stamina Regeneration/s"].get() + 1.5, 2))

def dec_end():
    if state_dict["Attributes"]["Endurance"].get() <=1:
        return
    state_dict["Attributes"]["Endurance"].set(state_dict["Attributes"]["Endurance"].get() - 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() - 1)
    update_level()
    state_dict["Statistics"]["Health"].set(state_dict["Statistics"]["Health"].get() - 8)
    state_dict["Statistics"]["Encumbrance Limit"].set(state_dict["Statistics"]["Encumbrance Limit"].get() - 10)
    state_dict["Statistics"]["Stamina Regeneration/s"].set(round(state_dict["Statistics"]["Stamina Regeneration/s"].get() - 1.5, 2))

def inc_dex():
    state_dict["Attributes"]["Dexterity"].set(state_dict["Attributes"]["Dexterity"].get() + 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() + 1)
    update_level()
    state_dict["Statistics"]["Attack Speed"].set(state_dict["Statistics"]["Attack Speed"].get() + 4)
    state_dict["Statistics"]["Noise"].set(state_dict["Statistics"]["Noise"].get() - 3)
    state_dict["Statistics"]["Ranged Damage"].set(state_dict["Statistics"]["Ranged Damage"].get() + 1)

def dec_dex():
    if state_dict["Attributes"]["Dexterity"].get() <=1:
        return
    state_dict["Attributes"]["Dexterity"].set(state_dict["Attributes"]["Dexterity"].get() - 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() - 1)
    update_level()
    state_dict["Statistics"]["Attack Speed"].set(state_dict["Statistics"]["Attack Speed"].get() - 4)
    state_dict["Statistics"]["Noise"].set(state_dict["Statistics"]["Noise"].get() + 3)
    state_dict["Statistics"]["Ranged Damage"].set(state_dict["Statistics"]["Ranged Damage"].get() - 1)

def inc_spi():
    state_dict["Attributes"]["Spirituality"].set(state_dict["Attributes"]["Spirituality"].get() + 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() + 1)
    update_level()
    state_dict["Statistics"]["Spell Damage"].set(state_dict["Statistics"]["Spell Damage"].get() + 1)
    state_dict["Statistics"]["Mana"].set(state_dict["Statistics"]["Mana"].get() + 6)
    state_dict["Statistics"]["Mana Regeneration/s"].set(round((state_dict["Statistics"]["Mana Regeneration/s"].get() + 0.3), 2))

def dec_spi():
    if state_dict["Attributes"]["Spirituality"].get() <=1:
        return
    state_dict["Attributes"]["Spirituality"].set(state_dict["Attributes"]["Spirituality"].get() - 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() - 1)
    update_level()
    state_dict["Statistics"]["Spell Damage"].set(state_dict["Statistics"]["Spell Damage"].get() - 1)
    state_dict["Statistics"]["Mana"].set(state_dict["Statistics"]["Mana"].get() - 6)
    state_dict["Statistics"]["Mana Regeneration/s"].set(round((state_dict["Statistics"]["Mana Regeneration/s"].get() - 0.3), 2))

def inc_per():
    state_dict["Attributes"]["Perception"].set(state_dict["Attributes"]["Perception"].get() + 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() + 1)
    update_level()
    state_dict["Statistics"]["Critical Damage"].set(state_dict["Statistics"]["Critical Damage"].get() + 5)
    state_dict["Statistics"]["Critical Chance"].set(state_dict["Statistics"]["Critical Chance"].get() + 1)
    state_dict["Statistics"]["Sneak Damage"].set(state_dict["Statistics"]["Sneak Damage"].get() + 8)

def dec_per():
    if state_dict["Attributes"]["Perception"].get() <=1:
        return
    state_dict["Attributes"]["Perception"].set(state_dict["Attributes"]["Perception"].get() - 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() - 1)
    update_level()
    state_dict["Statistics"]["Critical Damage"].set(state_dict["Statistics"]["Critical Damage"].get() - 5)
    state_dict["Statistics"]["Critical Chance"].set(state_dict["Statistics"]["Critical Chance"].get() - 1)
    state_dict["Statistics"]["Sneak Damage"].set(state_dict["Statistics"]["Sneak Damage"].get() - 8)

def inc_pra():
    state_dict["Attributes"]["Practicality"].set(state_dict["Attributes"]["Practicality"].get() + 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() + 1)
    update_level()
    state_dict["Statistics"]["Alchemy Bonus"].set(round((state_dict["Statistics"]["Alchemy Bonus"].get() + 0.1), 2))
    state_dict["Statistics"]["Cooking Bonus"].set(round((state_dict["Statistics"]["Cooking Bonus"].get() + 0.1), 2))
    state_dict["Statistics"]["Handcrafting Bonus"].set(round((state_dict["Statistics"]["Handcrafting Bonus"].get() + 0.1), 2))
    state_dict["Statistics"]["Weak Spot Damage"].set(state_dict["Statistics"]["Weak Spot Damage"].get() + 5)
    state_dict["Statistics"]["Price of sold goods"].set(state_dict["Statistics"]["Price of sold goods"].get() + 10)
    state_dict["Statistics"]["Stamina and Mana Cost"].set(state_dict["Statistics"]["Stamina and Mana Cost"].get() - 1)

def dec_pra():
    if state_dict["Attributes"]["Practicality"].get() <=1:
        return
    state_dict["Attributes"]["Practicality"].set(state_dict["Attributes"]["Practicality"].get() - 1)
    state_dict["Invested_attribute_points"].set(state_dict["Invested_attribute_points"].get() - 1)
    update_level()
    state_dict["Statistics"]["Alchemy Bonus"].set(round((state_dict["Statistics"]["Alchemy Bonus"].get() - 0.1), 2))
    state_dict["Statistics"]["Cooking Bonus"].set(round((state_dict["Statistics"]["Cooking Bonus"].get() - 0.1), 2))
    state_dict["Statistics"]["Handcrafting Bonus"].set(round((state_dict["Statistics"]["Handcrafting Bonus"].get() - 0.1), 2))
    state_dict["Statistics"]["Weak Spot Damage"].set(state_dict["Statistics"]["Weak Spot Damage"].get() - 5)
    state_dict["Statistics"]["Price of sold goods"].set(state_dict["Statistics"]["Price of sold goods"].get() - 10)
    state_dict["Statistics"]["Stamina and Mana Cost"].set(state_dict["Statistics"]["Stamina and Mana Cost"].get() + 1)
