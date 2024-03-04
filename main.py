import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from config import commands, copy, key_binds, paths
from widgets import menus, pies, buttons, labels


class App:
    """Tally and categorize content with a dynamic pie chart."""
    def __init__(self, master):
        self.master = master
        self.master.title(copy.app_name)
        self.master.iconbitmap(paths.app_icon)
        
        # Main attributes
        self.cats = []
        self.total_tally = 0

        # Widgets
        self.menu = menus.MainMenu(master, self)
        self.total_tally_label = labels.TotalTallyLabel(master, text=self.total_tally)
        self.pie_chart = pies.PieChart(master)
        self.new_pie_button = buttons.NewPieButton(master, self)
        self.new_cat_button = buttons.NewCatButton(master, self)
        commands.create_main_button(self)

        # Key binds
        key_binds.define_key_binds(master, self)        
        
def main():
    """Tally Pie's root window."""
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()