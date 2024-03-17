import tkinter as tk

from config import commands, copy, pie_changes


# PARENT CLASSES

class Button(tk.Button):
    """Parent button for the app's buttons."""
    def __init__(self, master, text, command):
        super().__init__(master, text=text, command=command)

class SizeButton(Button):
    """Parent button for a wedge's size buttons."""
    def __init__(self, master, size, text, command):
        self.size = size
        super().__init__(master, text=text, command=command)


# MAIN BUTTONS BELOW PIE CHART

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

class NewWedgeButton(Button):
    """Button that adds a new wedge."""
    def __init__(self, master, app):
        super().__init__(master, text=copy.buttons['new_wedge'], command=self.new_wedge)
        self.app = app
        self.grid(row=2, column=0)
        self.configure(bg='light yellow')

    def new_wedge(self):
        """Create a new wedge with a button."""
        commands.create_new_wedge(self.master, self.app, button=Button)

def create_main_button(app):
    """Choose the main button on the app's startup."""
    app.new_wedge_button.grid_forget()
    app.new_pie_button.grid(row=2, column=0)

def update_main_button(app):
    """Determine which button should be shown below the pie chart."""
    pie_button = app.new_pie_button
    wedge_button = app.new_wedge_button
    
    if len(app.wedges) >= 6:
        pie_button.grid_forget()
        wedge_button.grid_forget() 
    elif app.pie_chart.title:
        pie_button.grid_forget()
        wedge_button.grid(row=2, column=0)
    else:
        wedge_button.grid_forget()
        pie_button.grid(row=2, column=0)

def update_new_wedge_button(app):
    """Set the visibility of the new_wedge button."""
    if len(app.wedges) >= 6:
        app.new_wedge_button.grid_forget()
    else:
        app.new_wedge_button.grid(row=2, column=0)


# WEDGE FRAME BUTTONS

class PlusButton(SizeButton):
    """Button that increments 1 to a wedge."""
    def increment_size(self):
        self.size.size += 1
        self.size.size_label.config(text=self.size.size)
        pie_changes.update_pie_chart(app=self.size.app)

    def __init__(self, master, size):
        super().__init__(
            master, size, text=copy.buttons['plus'], command=self.increment_size)
        self.grid(row=0, column=2, padx=5, pady=5)
        pale_blue = '#d0fefe'
        self.configure(bg=pale_blue)
    
class MinusButton(SizeButton):
    """Button that decrements 1 from a wedge."""
    def decrement_size(self):
        if self.size.size > 0:
            self.size.size -= 1
            self.size.size_label.config(text=self.size.size)
            pie_changes.update_pie_chart(app=self.size.app)

    def __init__(self, master, size):
        super().__init__(
            master, size, text=copy.buttons['minus'], command=self.decrement_size)
        self.grid(row=0, column=3, padx=5, pady=5)
        pale_pink = '#ffcfdc'
        self.configure(bg=pale_pink)
 
class DeleteWedgeButton(Button):
    """Button that deletes a wedge."""
    def __init__(self, master, wedge):
        super().__init__(master, text=copy.buttons['delete_wedge'], command=self.delete_wedge)
        self.wedge = wedge
        self.grid(row=0, column=4, padx=(5, 10), pady=5, sticky="e")
    
    def delete_wedge(self):
        """Delete a wedge with a button."""
        commands.delete_wedge(self, self.wedge)
    