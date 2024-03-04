import tkinter as tk


class CatFrame(tk.Frame):
    """Class for a category frame."""
    def __init__(self, master):
        super().__init__(master, bg="lightgray", bd=2, relief=tk.SOLID)
        self.grid(sticky="ew")
    