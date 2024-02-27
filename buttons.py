import tkinter as tk


class Button(tk.Button):
    """Parent button for plus and minus buttons."""
    def __init__(self, master, tally_pie, text, command):
        self.tally_pie = tally_pie
        super().__init__(master, text=text, command=command)


class Plus_Button(Button):
    """Button that increments 1 to a category in the pie chart."""
    text = "+1"
    def increment_counter(self):
        self.tally_pie.counter += 1
        self.tally_pie.counter_label.config(text=self.tally_pie.counter)

    def __init__(self, master, tally_pie):
        super().__init__(master, tally_pie, text=self.text, command=self.increment_counter)
    

class Minus_Button(Button):
    """Button that decrements 1 from a category in the pie chart."""
    text = "-1"
    def decrement_counter(self):
        if self.tally_pie.counter > 0:
            self.tally_pie.counter -= 1
            self.tally_pie.counter_label.config(text=self.tally_pie.counter)

    def __init__(self, master, tally_pie):
        super().__init__(master, tally_pie, text=self.text, command=self.decrement_counter)
    
    