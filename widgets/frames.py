import tkinter as tk


class WedgeFrame(tk.Frame):
    """Class for a wedge frame."""
    def __init__(self, master):
        super().__init__(master, bg="white", bd=2, relief=tk.FLAT)
        self.grid(sticky="ew")
    