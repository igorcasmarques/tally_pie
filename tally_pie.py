import tkinter as tk

import buttons
from messages import dict as messages

class TallyPie:
    """Tally and categorize content with a dynamic pie chart."""
    def __init__(self, master):
        self.master = master
        self.master.title(messages['app_name'])

        # Categories
        self.cats = []
        self.new_cat_button = buttons.NewCatButton(master, self)
        self.new_cat_button.pack()


def main():
    """Tally Pie's root window."""
    root = tk.Tk()
    TallyPie(root)
    root.mainloop()

if __name__ == "__main__":
    main()