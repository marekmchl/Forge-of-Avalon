from tkinter import BooleanVar, IntVar, DoubleVar, StringVar
from json import loads

def make_updatable(master, state_var):
    if isinstance(state_var, dict):
        for (name, value) in state_var.items():
            if isinstance(value, dict):
                state_var[name] = make_updatable(master, value)
            elif isinstance(value, list):
                state_var[name] = make_updatable(master, value)
            elif isinstance(value, int):
                state_var[name] = IntVar(master, value, name)
            elif isinstance(value, float):
                state_var[name] = DoubleVar(master, value, name)
            elif isinstance(value, str):
                state_var[name] = StringVar(master, value, name)
            elif isinstance(value, bool):
                state_var[name] = BooleanVar(master, value, name)
    elif isinstance(state_var, list):
        for i, value in enumerate(state_var):
            state_var[i] = make_updatable(master, value)

    return state_var

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
