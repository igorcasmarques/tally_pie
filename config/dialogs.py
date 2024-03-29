import tkinter as tk
import sys

from config import copy, shortcuts, messages, pie_changes, paths
from widgets.wedges import Wedge
from widgets import buttons


# DIALOG BOX

def create_entry_dialog(master, app, button, command, label, text):
    """Open a dialog box for users to enter text."""
    entry_dialog = tk.Toplevel(master)
    float_window(entry_dialog)
    entry_dialog.iconbitmap(paths.app_icon)
    create_dialog_label(entry_dialog, label)
    create_entry_field(master, entry_dialog)
    submit = create_submit_button(
        master, app, entry_dialog, command, button, text
    )
    create_window_binds(app, entry_dialog, submit)

def create_new_pie_dialog(master, app, button):
    """Open a dialog box for users to create a new pie chart."""
    return create_entry_dialog(master, app, button,
        command=submit_new_pie,
        label=choose_dialog_label('new_pie'),
        text='submit_pie'
    )


# DIALOG BOX WIDGETS

def choose_dialog_label(box_label):
    """Populate the dialog box label with the right text."""
    text = copy.box_labels[box_label] + copy.box_labels['max_length']
    return text


def create_dialog_label(window, label):
    """Create an explanatory label for the entry field."""
    label = tk.Label(window, text=label)
    label.pack()

def create_entry_field(master, window):
    """Create an entry field in a window."""
    entry_field = tk.Entry(window)
    master.entry_field = entry_field
    entry_field.pack(padx=10, pady=10)
    entry_field.focus()

def create_submit_button(master, app, window, command, button, text):
    """Create a button that submits an entry field."""
    submit = lambda event=None: command(master, app, master.entry_field, window)
    submit_button = button(window, text=copy.buttons[text], command=submit)
    submit_button.pack(pady=5)
    return submit

def create_window_binds(app, window, submit):
    """Create key binds for entry windows."""
    window.bind(shortcuts.binds['submit'], submit)
    window.bind(shortcuts.binds['cancel'], lambda event: destroy_window(app, window))


# SUBMISSION METHODS

def submit_new_pie(master, app, name, window, event=None):
    """Submit a newly created wedge."""
    new_pie_name = name.get()

    if new_pie_name == '':
        messages.warning_box('empty_pie')
        name.focus()

    elif len(new_pie_name) > 25:
        messages.warning_box('too_long')
        name.focus()
    
    else:
        pie_changes.reset_pie(app, pie_title=new_pie_name)
        destroy_window(app, window)
        buttons.update_main_button(app)


def submit_new_wedge(master, app, name, window, event=None):
    """Submit a newly created wedge."""
    new_wedge_name = name.get()

    if new_wedge_name == '':
        messages.warning_box('empty_wedge')
        name.focus()

    elif len(new_wedge_name) > 25:
        messages.warning_box('too_long')
        name.focus()

    else:
        if all(wedge.name != new_wedge_name for wedge in app.wedges):
            new_wedge = Wedge(master, app)
            new_wedge.name = new_wedge_name
            app.wedges.append(new_wedge)
            new_wedge.label.config(text=new_wedge_name)
            destroy_window(app, window)
            buttons.update_new_wedge_button(app)
        else:
            messages.warning_box('repeated_wedge')
            name.focus()


# WINDOW BEHAVIOUR METHODS

def float_window(window):
    """Make a window float."""
    if sys.platform == 'win32':  
        window.attributes("-topmost", True)
    elif sys.platform == 'darwin': 
        window.wm_attributes('-topmost', 1)

def destroy_window(app, window):
    window.destroy()
    app.master.focus()