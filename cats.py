import tkinter as tk

import buttons

class Cat:
    """Class to keep track of a category's tally."""
    def __init__(self, master, tally_pie):
        self.master = master
        self.tally_pie = tally_pie

        # Attributes
        self.cat_name = ""
        self.tally = 0

        # Elements and buttons in the category frame
        self.frame = CatFrame(master)
        self.label = CatLabel(self.frame, text=self.cat_name)
        self.tally_label = CatTallyLabel(self.frame, text=self.tally)
        self.delete_button = buttons.DeleteCatButton(self.frame, self)
        self.minus_button = buttons.MinusButton(self.frame, self)
        self.plus_button = buttons.PlusButton(self.frame, self)

class CatFrame(tk.Frame):
    """Class for a category frame."""
    def __init__(self, master):
        super().__init__(master, bg="lightgray", bd=2, relief=tk.SOLID)
        self.pack(padx=10, pady=10)

class CatLabel(tk.Label):
    """Class for a category label."""
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.pack(pady=10, side=tk.TOP)

class CatTallyLabel(tk.Label):
    """Class for a category tally label."""
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.pack(pady=10, side=tk.TOP)