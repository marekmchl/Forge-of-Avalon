from tkinter import IntVar, DoubleVar
from json import loads

def make_updatable(master, state_dict):
    for (name, value) in state_dict.items():
        if isinstance(value, dict):
            state_dict[name] = make_updatable(master, value)
        elif isinstance(value, int):
            state_dict[name] = IntVar(master, value, name)
        elif isinstance(value, float):
            state_dict[name] = DoubleVar(master, value, name)

    return state_dict

def load_state(master):
    try:
        file = open("current_state.json", "r")
    except Exception:
        file = open("default_state.json", "r")
        new_file = open("current_state.json", "w")
        new_file.write(file.read())
        new_file.close()
    state_dict = loads(file.read())
    file.close()
    state_dict = make_updatable(master, state_dict)
    return state_dict

def make_savable(dict):
    pass
