import tkinter as tk
import sys

from buttons import Plus_Button, Minus_Button

class Tally_Pie:
    """Tally and categorize content with a dynamic pie chart."""
    title = "Tally Pie"

    def __init__(self, master):
        self.master = master
        self.master.title(self.title)
        
        # Floating window
        if sys.platform == 'win32':
            self.master.attributes("-topmost", True)

        # Counter
        self.counter = 0
        self.counter_label = tk.Label(self.master, text=self.counter)
        self.counter_label.pack()

        # Buttons
        self.minus_button = Minus_Button(self.master, self)
        self.minus_button.pack(side=tk.LEFT)
        self.plus_button = Plus_Button(self.master, self)
        self.plus_button.pack(side=tk.RIGHT)
        

def main():
    """Tally Pie's root window."""
    root = tk.Tk()
    Tally_Pie(root)
    root.mainloop()

if __name__ == "__main__":
    main()