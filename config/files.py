from tkinter import filedialog
import json

from config import messages, pie_changes
from config.cats import Cat
from widgets import buttons

def save_file(title, cat_data, filename=None):
    """Save session data to a JSON file."""
    if filename is None:
        filename = filedialog.asksaveasfilename(
            defaultextension=".json", 
            filetypes=[("JSON files", "*.json")]
        )
        if not filename:
            return

        save_data = {
            "title": title,
            "categories": [{'cat_name': cat.cat_name, 'tally': cat.tally} for cat in cat_data]
        }

        with open(filename, 'w') as f:
            json.dump(save_data, f, indent=4)

def load_pie_chart(app):
    """Load a pie chart and update all necessary widgets."""
    filename = filedialog.askopenfilename(
                filetypes=[("JSON files", "*.json")],
                title="Select a file to open"
    )

    if filename:
        load_file(filename, app)
        pie_changes.update_pie_chart(app)
        buttons.update_main_button(app)

def load_file(filename, app):
    """Load saved data from a JSON file and update the application state."""
    data = load_saved_data(filename)
    if data is not None:
        # Clear current session
        if app.cats:
            for cat in app.cats:
                cat.frame.destroy()
            app.cats.clear()

        # Load the existing session
        app.pie_chart.title = data['title']
        for cat_data in data['categories']:
            cat = Cat(app.master, app)
            cat.cat_name = cat_data['cat_name']
            cat.tally = cat_data['tally']
            cat.label.config(text=cat.cat_name)
            cat.tally_label.config(text=cat.tally)
            app.cats.append(cat)

def load_saved_data(filename):
    """Load session data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        messages.error_box('not_found')
    except json.JSONDecodeError:
        messages.error_box('not_json')

