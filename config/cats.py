import tkinter as tk

from widgets import frames, labels, buttons

class Cat:
    """Class to keep track of a category's tally."""
    def __init__(self, master, app):
        self.master = master
        self.app = app

        # Attributes
        self.cat_name = ""
        self.tally = 0
        self.tally_percent = 0

        # Elements and buttons in the category frame
        self.frame = frames.CatFrame(master)
        self.label = labels.CatLabel(self.frame, text=self.cat_name)
        self.tally_label = labels.CatTallyLabel(self.frame, text=self.tally)
        self.delete_button = buttons.DeleteCatButton(self.frame, self)
        self.minus_button = buttons.MinusButton(self.frame, self)
        self.plus_button = buttons.PlusButton(self.frame, self)
    
