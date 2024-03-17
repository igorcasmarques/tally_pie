from tkinter import filedialog
import json

from config import messages, pie_changes, copy
from widgets.wedges import Wedge
from widgets import buttons


# SAVING

def save_file(title, wedge_data, filename=None):
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
            "wedges": [{'name': wedge.name, 'size': wedge.size} for wedge in wedge_data]
        }

        with open(filename, 'w') as f:
            json.dump(save_data, f, indent=4)


# LOADING

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
        if app.wedges:
            for wedge in app.wedges:
                wedge.frame.destroy()
            app.wedges.clear()

        # Load the existing session
        app.pie_chart.title = data['title']
        for wedge_data in data['wedges']:
            wedge = Wedge(app.master, app)
            wedge.name = wedge_data['name']
            wedge.size = wedge_data['size']
            wedge.label.config(text=wedge.name)
            wedge.size_label.config(text=wedge.size)
            app.wedges.append(wedge)

def load_saved_data(filename):
    """Load session data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        messages.error_box('not_found')
    except json.JSONDecodeError:
        messages.error_box('invalid_json')
