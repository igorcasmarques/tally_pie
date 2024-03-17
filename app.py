import tkinter as tk

from config import base, key_binds, paths, dialogs
from widgets import menus, pies, buttons, labels


class App:
    """Count and categorize content with a dynamic pie chart."""
    def __init__(self, master):
        self.master = master
        dialogs.float_window(self.master)
        self.master.title(base.app_name)
        self.master.iconbitmap(paths.app_icon)       
               
        # Main attributes
        self.wedges = []
        self.total_count = 0

        # Widgets
        self.pie_chart = pies.PieChart(master)
        self.total_count_label = labels.TotalCountLabel(master, text=self.total_count)
        self.menu = menus.MainMenu(master, self)
        self.new_pie_button = buttons.NewPieButton(master, self)
        self.new_wedge_button = buttons.NewWedgeButton(master, self)
        buttons.create_main_button(self)

        # Key binds
        key_binds.define_key_binds(master, self)        
        
def main():
    """Tally Pie's root window."""
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()