import tkinter as tk

import widgets

class Cat:
    """Class to keep track of a category's tally."""
    def __init__(self, master, app):
        self.master = master
        self.app = app

        # Attributes
        self.cat_name = ""
        self.tally = 0

        # Elements and buttons in the category frame
        self.frame = widgets.CatFrame(master)
        self.label = widgets.CatLabel(self.frame, text=self.cat_name)
        self.tally_label = widgets.CatTallyLabel(self.frame, text=self.tally)
        self.delete_button = widgets.DeleteCatButton(self.frame, self)
        self.minus_button = widgets.MinusButton(self.frame, self)
        self.plus_button = widgets.PlusButton(self.frame, self)
