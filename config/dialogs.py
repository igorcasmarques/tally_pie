import tkinter as tk

from config.cats import Cat
from config import copy, shortcuts, messages, pie_changes, paths
from widgets import buttons


# DIALOG BOX

def create_entry_dialog(master, app, button, command, label, text):
    """Open a dialog box for users to enter text."""
    entry_dialog = tk.Toplevel(master)
    entry_dialog.iconbitmap(paths.app_icon)
    create_dialog_label(entry_dialog, label)
    create_entry_field(master, entry_dialog)
    submit = create_submit_button(
        master, app, entry_dialog, command, button, text
    )
    create_window_binds(entry_dialog, submit)

def create_new_pie_dialog(master, app, button):
    """Open a dialog box for users to create a new pie chart."""
    return create_entry_dialog(master, app, button,
        command=submit_new_pie,
        label=copy.box_labels['new_pie'],
        text='submit_pie'
    )

# DIALOG BOX WIDGETS

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

def create_window_binds(window, submit):
    """Create key binds for entry windows."""
    window.bind(shortcuts.binds['submit'], submit)
    window.bind(shortcuts.binds['cancel'], lambda event: window.destroy())


# SUBMISSION METHODS

def submit_new_pie(master, app, name, window, event=None):
    """Submit a newly created category from the new category window."""
    new_pie_name = name.get()

    if new_pie_name == '':
        messages.warning_box('empty_pie')
        name.focus()

    elif len(new_pie_name) > 25:
        messages.warning_box('too_long_pie')
        name.focus()
    
    else:
        pie_changes.reset_pie(app, pie_title=new_pie_name)
        window.destroy()
        buttons.update_main_button(app)


def submit_new_cat(master, app, name, window, event=None):
    """Submit a newly created category from the new category window."""
    new_cat_name = name.get()

    if new_cat_name == '':
        messages.warning_box('empty_cat')
        name.focus()

    elif len(new_cat_name) > 25:
        messages.warning_box('too_long_cat')
        name.focus()

    else:
        if all(cat.cat_name != new_cat_name for cat in app.cats):
            new_cat = Cat(master, app)
            new_cat.cat_name = new_cat_name
            app.cats.append(new_cat)
            new_cat.label.config(text=new_cat_name)
            window.destroy()
            buttons.update_new_cat_button(app)
        else:
            messages.warning_box('repeated_cat')
            name.focus()