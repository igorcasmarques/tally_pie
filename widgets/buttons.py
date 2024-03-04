import tkinter as tk

from config import commands, copy


# PARENT CLASS
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
        commands.update_pie_chart(app=self.tally.app)

    def __init__(self, master, tally):
        super().__init__(
            master, tally, text=copy.buttons['plus'], command=self.increment_tally)
        self.grid(row=0, column=2, padx=5, pady=5)
        pale_blue = '#d0fefe'
        self.configure(bg=pale_blue)
    
class MinusButton(TallyButton):
    """Button that decrements 1 from a tally category in the pie chart."""
    def decrement_tally(self):
        if self.tally.tally > 0:
            self.tally.tally -= 1
            self.tally.tally_label.config(text=self.tally.tally)
            commands.update_pie_chart(app=self.tally.app)

    def __init__(self, master, tally):
        super().__init__(
            master, tally, text=copy.buttons['minus'], command=self.decrement_tally)
        self.grid(row=0, column=3, padx=5, pady=5)
        pale_pink = '#ffcfdc'
        self.configure(bg=pale_pink)


# PIE BUTTONS
class NewPieButton(Button):
    """Button that creates a new pie chart."""
    def __init__(self, master, app):
        super().__init__(master, text=copy.buttons['new_pie'], command=self.new_pie)
        self.app = app
        self.grid(row=2, column=0)
        self.configure(bg='light green', font=("Arial", 10, "bold"))
    
    def new_pie(self):
        """Create a new pie chart with a button."""
        commands.create_new_pie(self.master, self.app, button=Button)

# CATEGORY BUTTONS
class NewCatButton(Button):
    """Button that adds a new tally category."""
    def __init__(self, master, app):
        super().__init__(master, text=copy.buttons['new_cat'], command=self.new_cat)
        self.app = app
        self.grid(row=2, column=0)
        self.configure(bg='light yellow')

    def new_cat(self):
        """Create a new tally category with a button."""
        commands.create_new_cat(self.master, self.app, button=Button)
          
class DeleteCatButton(Button):
    """Button that deletes a tally category."""
    def __init__(self, master, cat):
        super().__init__(master, text=copy.buttons['delete_cat'], command=self.delete_cat)
        self.cat = cat
        self.grid(row=0, column=4, padx=(5, 10), pady=5, sticky="e")
    
    def delete_cat(self):
        """Delete a category with a button."""
        commands.delete_cat(self, self.cat)
    