from ui_elements import Window, Line
from state import load_state

def main():
    win = Window("Forge of Avalon")
    state = load_state(win)
    lvl = Line(win, "Level", state["Level"])
    lvl.grid(row = 0, column = 0)
    state["Level"].set(state["Level"].get() + 3)
    win.mainloop()

if __name__ == "__main__":
    main()
