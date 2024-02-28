import tkinter as tk
from tkinter import messagebox

from cats import Cat

from messages import dict
messages = dict['buttons']
dialogues = dict['dialogues']


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
            master, tally, text=messages['plus'], command=self.increment_tally)
        self.pack(padx=5, pady=5, side=tk.RIGHT)
    

class MinusButton(TallyButton):
    """Button that decrements 1 from a tally category in the pie chart."""
    def decrement_tally(self):
        if self.tally.tally > 0:
            self.tally.tally -= 1
            self.tally.tally_label.config(text=self.tally.tally)

    def __init__(self, master, tally):
        super().__init__(
            master, tally, text=messages['minus'], command=self.decrement_tally)
        self.pack(padx=5, pady=5, side=tk.LEFT)


# CATEGORY BUTTONS
        
class NewCatButton(Button):
    """Button that adds a new tally category."""
    def __init__(self, master, tally_pie):
        super().__init__(master, text=messages['new_cat'], command=self.new_cat)
        self.tally_pie = tally_pie

    def new_cat(self):
        """Create a new tally category."""
        # New window
        new_cat_window = tk.Toplevel(self.master)

        # Entry field
        cat_name_entry = tk.Entry(new_cat_window)
        cat_name_entry.pack(padx=10, pady=10)
        cat_name_entry.focus()

        # Submit new category
        def submit_cat(event=None):
            """Submit a newly created category."""
            new_cat_name = cat_name_entry.get()
            if new_cat_name != "":
                if all(cat.cat_name != new_cat_name for cat in self.tally_pie.cats):
                    new_cat = Cat(self.master, self.tally_pie)
                    new_cat.cat_name = new_cat_name
                    self.tally_pie.cats.append(new_cat)
                    new_cat.label.config(text=new_cat_name)
                    new_cat_window.destroy()
                else:
                    messagebox.showerror(dialogues['error'], dialogues['repeated_cat'])
                    cat_name_entry.focus()
            else:
                messagebox.showerror(dialogues['error'], dialogues['empty_cat'])
                cat_name_entry.focus()
        
        # Key bindings
        new_cat_window.bind('<Return>', submit_cat)
        new_cat_window.bind('<Escape>', lambda event: new_cat_window.destroy())

        # Submit button
        submit_button = Button(
            new_cat_window, text=messages['submit_cat'], command=submit_cat)
        submit_button.pack(pady=5)
    

class DeleteCatButton(Button):
    """Button that deletes a tally category."""
    def __init__(self, master, cat_instance):
        super().__init__(master, text=messages['delete_cat'], command=self.delete_cat)
        self.cat_instance = cat_instance
        self.pack(side=tk.TOP, anchor=tk.NE)
    
    def delete_cat(self):
        """Delete the category."""
        self.cat_instance.frame.destroy()
        self.cat_instance.tally_pie.cats.remove(self.cat_instance)
    