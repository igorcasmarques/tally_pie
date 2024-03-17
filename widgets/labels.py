import tkinter as tk

from config import copy


class TotalCountLabel(tk.Label):
    """Class for a label for the app's total count."""
    def __init__(self, master, text):
        super().__init__(master, text=f"{copy.total_count} {text}")
        self.grid(row=0, column=0)

class WedgeLabel(tk.Label):
    """Class for a wedge label."""
    def __init__(self, master, text):
        super().__init__(master, text=text, font=("Arial", 10, "bold"))
        self.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="w")

class WedgeSizeLabel(tk.Label):
    """Class for a wedge's size label."""
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.grid(row=0, column=1, padx=5, pady=10, sticky="w")
    