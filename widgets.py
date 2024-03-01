import tkinter as tk
from tkinter import messagebox

import actions

from dicts import all_labels
labels = all_labels['buttons']


class Button(tk.Button):
    """Parent button for the app's buttons."""
    def __init__(self, master, text, command):
        super().__init__(master, text=text, command=command)


# TALLY BUTTONS

class TallyButton(Button):
    """Parent button for the a category's tally buttons."""
    def __init__(self, master, tally, text, command):
        self.tally = tally
        super().__init__(master, text=text, command=command)


class PlusButton(TallyButton):
    """Button that increments 1 to a tally category in the pie chart."""
    def increment_tally(self):
        self.tally.tally += 1
        self.tally.tally_label.config(text=self.tally.tally)

    def __init__(self, master, tally):
        super().__init__(
            master, tally, text=labels['plus'], command=self.increment_tally)
        self.grid(row=0, column=2, padx=5, pady=5)
    

class MinusButton(TallyButton):
    """Button that decrements 1 from a tally category in the pie chart."""
    def decrement_tally(self):
        if self.tally.tally > 0:
            self.tally.tally -= 1
            self.tally.tally_label.config(text=self.tally.tally)

    def __init__(self, master, tally):
        super().__init__(
            master, tally, text=labels['minus'], command=self.decrement_tally)
        self.grid(row=0, column=3, padx=5, pady=5)


# CATEGORY BUTTONS
        
class NewCatButton(Button):
    """Button that adds a new tally category."""
    def __init__(self, master, app):
        super().__init__(master, text=labels['new_cat'], command=self.new_cat)
        self.app = app

    def new_cat(self):
        """Create a new tally category with a button."""
        actions.new_cat(self.master, self.app, button=Button)
    
class DeleteCatButton(Button):
    """Button that deletes a tally category."""
    def __init__(self, master, cat_instance):
        super().__init__(master, text=labels['delete_cat'], command=self.delete_cat)
        self.cat_instance = cat_instance
        self.grid(row=0, column=4, padx=(5, 10), pady=5, sticky="e")
    
    def delete_cat(self):
        """Delete the category."""
        self.cat_instance.frame.destroy()
        self.cat_instance.app.cats.remove(self.cat_instance)

# UI ELEMENTS
 
class CatFrame(tk.Frame):
    """Class for a category frame."""
    def __init__(self, master):
        super().__init__(master, bg="lightgray", bd=2, relief=tk.SOLID)
        self.grid(sticky="ew")

class CatLabel(tk.Label):
    """Class for a category label."""
    def __init__(self, master, text):
        super().__init__(master, text=text, font=("Arial", 10, "bold"))
        self.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="w")

class CatTallyLabel(tk.Label):
    """Class for a category tally label."""
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.grid(row=0, column=1, padx=5, pady=10, sticky="w")
    