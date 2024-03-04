import tkinter as tk

from config import copy


class TotalTallyLabel(tk.Label):
    """Class for a label for the app's total tally."""
    def __init__(self, master, text):
        super().__init__(master, text=f"{copy.total_tally} {text}")
        self.grid(row=0, column=0)

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
    