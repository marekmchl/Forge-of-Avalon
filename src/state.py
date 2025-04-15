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

def load_state():
    try:
        file = open("current_state.json", "r")
        state_dict = loads(file.read())
        file.close()
        return state_dict
    except Exception:
        file = open("default_state.json", "r")
        new_file = open("current_state.json", "x")
        new_file.write(file.read())
        new_file.close()
        file.close()
        file = open("current_state.json", "r")
        state_dict = loads(file.read())
        file.close()
        return state_dict

state_dict = load_state()

def update_level():
    state_dict["Level"].set(1 + max(state_dict["Invested_attribute_points"].get(), state_dict["Invested_skill_points"].get()))

def make_savable(dict):
    pass
