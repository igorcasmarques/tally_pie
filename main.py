import tkinter as tk

import menus, widgets
from dicts import all_labels
menu_labels = all_labels['menus']

class App:
    """Tally and categorize content with a dynamic pie chart."""
    def __init__(self, master):
        self.master = master
        self.master.title(all_labels['app_name'])

        # In-memory
        self.cats = []

        # Menus
        self.menu = menus.MainMenu(master)
        self.file_menu = menus.FileMenu(master, self)
        self.menu.add_menu(menu_labels['file'], self.file_menu)

        # Buttons
        self.new_cat_button = widgets.NewCatButton(master, self)
        self.new_cat_button.grid(row=0, column=0)

        # Key bindings
        def new_cat_bind(event=None):
            """Key binding for adding a category."""
            self.file_menu.new_cat()

        def open_file_bind(event=None):
            """Key binding for opening a file."""
            self.file_menu.open_file()
        
        def save_file_bind(event=None):
            """Key binding for saving a session."""
            self.file_menu.save_file()

        master.bind_all('<Control-n>', new_cat_bind)
        master.bind_all('<Control-o>', open_file_bind)
        master.bind_all('<Control-s>', save_file_bind)


def main():
    """Tally Pie's root window."""
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()