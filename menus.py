import tkinter as tk

import actions
from dicts import all_labels
labels = all_labels['menus']
accels = all_labels['accels']


class MainMenu(tk.Menu):
    """Class to create the main menu."""
    def __init__(self, master):
        super().__init__(master)
        master.config(menu=self)

    def add_menu(self, label, menu):
        """Add a new menu to the main menu."""
        self.add_cascade(label=label, menu=menu)

class FileMenu(tk.Menu):
    """Class to create the file menu."""
    def __init__(self, master, app):
        super().__init__(master, tearoff=False)
        self.app = app

        self.add_command(
            label=labels['new'], command=self.new_cat, accelerator=accels['new'])
        self.add_command(
            label=labels['open'], command=self.open_file, accelerator=accels['open'])
        self.add_separator()
        self.add_command(
            label=labels['save'], command=self.save_file, accelerator=accels['save'])
        self.add_separator()
        self.add_command(
            label=labels['exit'], command=master.quit, accelerator=accels['exit'])
    
    def new_cat(self):
        """Function to handle the 'New category' menu item."""
        actions.new_cat(master=self.master, app=self.app, button=tk.Button)
    
    def save_file(self):
        """Function to handle the 'Save' menu item."""
        actions.save_file(data=self.app.cats)
    
    def open_file(self):
        """Function to handle the 'Open' menu item."""
        actions.open_file(app=self.app)
    
    
        