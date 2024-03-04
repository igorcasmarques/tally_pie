import tkinter as tk

from config import commands, copy


class MainMenu(tk.Menu):
    """Class to create the main menu."""
    def __init__(self, master, app):
        super().__init__(master)
        master.config(menu=self)
        menus = [
            FileMenu(master, app),
            HelpMenu(master),
        ]
        for menu in menus:
            self.add_menu(copy.menus[menu.name], menu)


    def add_menu(self, label, menu):
        """Add a new menu to the main menu."""
        self.add_cascade(label=label, menu=menu)


class FileMenu(tk.Menu):
    """Class to create the File menu."""
    def __init__(self, master, app):
        super().__init__(master, tearoff=False)
        self.app = app
        self.name = 'file'

        self.add_command(
            label=copy.menus['new_pie'], 
            command=self.new_pie,
            accelerator=copy.accelerators['new_pie']
        )
        self.add_command(
            label=copy.menus['new_cat'], 
            command=self.new_cat,
            accelerator=copy.accelerators['new_cat']
        )
        self.add_separator()
        self.add_command(
            label=copy.menus['save_pie'],
            command=self.save_snapshot,
            accelerator=copy.accelerators['save_pie']
        )
        self.add_command(
            label=copy.menus['open_pie'], 
            command=self.load_snapshot, 
            accelerator=copy.accelerators['open_pie']
        )
        self.add_separator()
        self.add_command(
            label=copy.menus['exit'], command=master.quit, accelerator=copy.accelerators['exit'])
    
    def new_pie(self):
        """Function to handle the 'New pie chart' menu item."""
        commands.create_new_pie(master=self.master, app=self.app, button=tk.Button)
    
    def new_cat(self):
        """Function to handle the 'New category' menu item."""
        commands.create_new_cat(master=self.master, app=self.app, button=tk.Button)
    
    def save_snapshot(self):
        """Function to handle the 'Save' menu item."""
        commands.save_snapshot(data=self.app.cats)
    
    def load_snapshot(self):
        """Function to handle the 'Load' menu item."""
        commands.load_snapshot(app=self.app)

class HelpMenu(tk.Menu):
    """Class to create the Help menu."""
    def __init__(self, master):
        super().__init__(master, tearoff=False)
        self.name = 'help'

        self.add_command(label=copy.menus['contribute'], command=self.contribute)
        self.add_separator()
        self.add_command(label=copy.menus['about'], command=self.about)
        
    def contribute(self):
        """Function to send users to the app's GitHub repository."""
        commands.contribute()

    def about(self):
        """Function to handle the 'About' menu item."""
        commands.about()
     