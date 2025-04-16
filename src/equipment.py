from json import loads

def load_equipment():
    file = open("equipment.json", "r")
    equipment_dict = loads(file.read())
    file.close()
    return equipment_dict

equipment_dict = load_equipment()
