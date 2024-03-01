import tkinter as tk
from tkinter import messagebox, filedialog

import json

from cats import Cat

from dicts import all_labels
button_labels = all_labels['buttons']
warning_labels = all_labels['warnings']
error_labels = all_labels['errors']

# CREATE A NEW TALLY CATEGORY
def new_cat(master, app, button):
        """Create a new tally category."""
        # Check if the maximum number of cats has been reached
        if len(app.cats) >= 6:
            messagebox.showwarning(warning_labels['warning'], warning_labels['too_many_cats'])
            return

        # Check if a cat_name_entry (in a new_cat_window) already exists
        elif hasattr(master, "cat_name_entry") and master.cat_name_entry.winfo_exists():
            master.cat_name_entry.focus()
            return

        # Create a new_cat_window
        else: 
            # New window
            new_cat_window = tk.Toplevel(master)

            # Entry field
            cat_name_entry = tk.Entry(new_cat_window)
            master.cat_name_entry = cat_name_entry
            cat_name_entry.pack(padx=10, pady=10)
            cat_name_entry.focus()

            # Submit new category
            submit_cat = lambda event=None: _submit_cat(
                master, app, name=cat_name_entry, window=new_cat_window)
            
            # Key bindings
            new_cat_window.bind('<Return>', submit_cat)
            new_cat_window.bind('<Escape>', lambda event: new_cat_window.destroy())

            # Submit button
            submit_button = button(
                new_cat_window, text=button_labels['submit_cat'], command=submit_cat)
            submit_button.pack(pady=5)

def _submit_cat(master, app, name, window, event=None):
    """Submit a newly created category."""
    new_cat_name = name.get()
    if new_cat_name != "":
        if all(cat.cat_name != new_cat_name for cat in app.cats):
            new_cat = Cat(master, app)
            new_cat.cat_name = new_cat_name
            app.cats.append(new_cat)
            new_cat.label.config(text=new_cat_name)
            window.destroy()
        else:
            messagebox.showwarning(warning_labels['warning'], warning_labels['repeated_cat'])
            name.focus()
    else:
        messagebox.showwarning(warning_labels['warning'], warning_labels['empty_cat'])
        name.focus()

# SAVE FILE
def save_file(data, filename=None):
    """Save session data to a JSON file."""
    if filename is None:
        filename = filedialog.asksaveasfilename(
            defaultextension=".json", 
            filetypes=[("JSON files", "*.json")]
        )
        if not filename:
            return

    save_data = [
        {'cat_name': cat.cat_name, 'tally': cat.tally} 
        for cat in data
    ]

    with open(filename, 'w') as f:
        json.dump(save_data, f, indent=4)

# LOAD FILE
def open_file(app):
    """Open a file dialog to choose a file to load."""
    filename = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")],
        title="Select a file to open"
    )
    if filename:
        _load_file(filename, app)

def _load_file(filename, app):
    """Load saved data from a JSON file and update the application state."""
    data = _load_saved_data(filename)
    if data is not None:
        # Clear current session
        if app.cats:
            for cat in app.cats:
                cat.frame.destroy()
            app.cats.clear()

        # Load the existing session
        for cat_data in data:
            cat = Cat(app.master, app)
            cat.cat_name = cat_data['cat_name']
            cat.tally = cat_data['tally']
            cat.label.config(text=cat.cat_name)
            cat.tally_label.config(text=cat.tally)
            app.cats.append(cat)
            print(app.cats)

def _load_saved_data(filename):
    """Load session data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    except FileNotFoundError:
        # Handle the case when the file does not exist
        messagebox.showerror(error_labels['error'], error_labels['not_found'])
        return None
    except json.JSONDecodeError:
        # Handle the case when the file is not a valid JSON
        messagebox.showerror(error_labels['error'], error_labels['not_json'])
        return None
