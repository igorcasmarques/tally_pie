import tkinter as tk

from config import commands, copy


class MainMenu(tk.Menu):
    """Class to create the main menu."""
    def __init__(self, master, app):
        super().__init__(master)
        master.config(menu=self)
        menus = [
            FileMenu(master, app),
            EditMenu(master, app),
            HelpMenu(master),
        ]
        for menu in menus:
            self.add_menu(copy.menus[menu.name], menu)


    def add_menu(self, label, menu):
        """Add the app's main menu."""
        self.add_cascade(label=label, menu=menu)


class FileMenu(tk.Menu):
    """Class to create the File menu."""
    def __init__(self, master, app):
        super().__init__(master, tearoff=False)
        self.app = app
        self.name = 'file'
        
        self.new_pie_chart = self.add_command(
            label=copy.menus['new_pie'], 
            command=self.new_pie,
            accelerator=copy.accelerators['new_pie']
        )
        self.add_separator()
        self.save_pie_chart = self.add_command(
            label=copy.menus['save_pie'],
            command=self.save_pie,
            accelerator=copy.accelerators['save_pie']
        )
        self.open_pie_chart = self.add_command(
            label=copy.menus['open_pie'], 
            command=self.open_pie, 
            accelerator=copy.accelerators['open_pie']
        )
        self.add_separator()
        self.exit = self.add_command(
            label=copy.menus['exit'],
            command=master.quit,
            accelerator=copy.accelerators['exit']
        )
        
    
    def new_pie(self):
        """Function to handle the 'New pie chart' menu item."""
        commands.create_new_pie(master=self.master, app=self.app, button=tk.Button)
    
    def save_pie(self):
        """Function to handle the 'Save' menu item."""
        commands.save_pie(title=self.app.pie_chart.title, wedge_data=self.app.wedges)
    
    def open_pie(self):
        """Function to handle the 'Load' menu item."""
        commands.open_pie(master=self.master, app=self.app, button=tk.Button)
    

class EditMenu(tk.Menu):
    """Class to create the Edit menu."""
    def __init__(self, master, app):
        super().__init__(master, tearoff=False)
        self.app = app
        self.name = 'edit'

        self.new_wedge = self.add_command(
            label=copy.menus['new_wedge'], 
            command=self.new_wedge,
            accelerator=copy.accelerators['new_wedge']
        )
        self.add_separator()
        self.rename_pie = self.add_command(
            label=copy.menus['rename_pie'],
            command=self.rename_pie,
            accelerator=copy.accelerators['rename_pie'],
        )
        self.erase_pie = self.add_command(
            label=copy.menus['erase_pie'],
            command=self.erase_pie,
            accelerator=copy.accelerators['erase_pie']
        )

    def new_wedge(self):
        """Function to handle the 'Add wedge' menu item."""
        commands.create_new_wedge(master=self.master, app=self.app, button=tk.Button)
    
    def rename_pie(self):
        """Function to allow users to rename the current pie chart."""
        commands.rename_pie(master=self.master, app=self.app, button=tk.Button)
    
    def erase_pie(self):
        """Function to allow users to erase a pie chart."""
        commands.erase_pie(app=self.app)


class HelpMenu(tk.Menu):
    """Class to create the Help menu."""
    def __init__(self, master):
        super().__init__(master, tearoff=False)
        self.name = 'help'

        self.user_guide = self.add_command(
            label=copy.menus['user_guide'],
            command=self.user_guide
        )
        self.add_separator()
        self.about = self.add_command(
            label=copy.menus['about'],
            command=self.about
        )
        
    def user_guide(self):
        """Function to send users to the app's user guide."""
        commands.user_guide()

    def about(self):
        """Function to handle the 'About' menu item."""
        commands.about()
     