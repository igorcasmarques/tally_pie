import tkinter as tk
from tkinter import messagebox, filedialog
import json
import webbrowser

from config.cats import Cat
from config import copy, shortcuts, hyperlinks


# CATEGORY METHODS

def create_new_pie(master, app, button):
        """Create a new pie chart."""
        # Checks category space and name eligibility, then opens a new window
        if app.pie_chart.title:
            confirmation = messagebox.askyesno(
                copy.new_pie['new_pie'], copy.new_pie['confirmation'])
            if confirmation:
                open_pie_window(master, app, button)

        elif hasattr(master, "pie_title_entry") and master.pie_title_entry.winfo_exists():
            master.pie_title_entry.focus()
            return

        else: 
            open_pie_window(master, app, button)

def open_pie_window(master, app, button):
    """Open a new window for users to input the name of a new pie chart."""
    new_pie_window = tk.Toplevel(master)

    # Entry field
    pie_title_entry = tk.Entry(new_pie_window)
    master.pie_title_entry = pie_title_entry
    pie_title_entry.pack(padx=10, pady=10)
    pie_title_entry.focus()

    # Submit button
    submit_pie = lambda event=None: submit_new_pie(
        master, app, name=pie_title_entry, window=new_pie_window)
    submit_button = button(
        new_pie_window, text=copy.buttons['submit_pie'], command=submit_pie)
    submit_button.pack(pady=5)

    # Key binds
    new_pie_window.bind(shortcuts.binds['submit'], submit_pie)
    new_pie_window.bind(shortcuts.binds['cancel'], lambda event: new_pie_window.destroy())


def submit_new_pie(master, app, name, window, event=None):
    """Submit a newly created category from the new category window."""
    new_pie_name = name.get()
    if new_pie_name != "":
        cats = app.cats
        if cats:
            for cat in cats:
                cat.frame.destroy()
            cats.clear()
        
        pie_chart = app.pie_chart
        pie_chart.ax.clear()
        pie_chart.title = new_pie_name
        pie_chart.ax.set_title(new_pie_name)
        pie_chart.ax.pie(pie_chart.sizes, labels=pie_chart.labels, autopct='', startangle=90)
        pie_chart.ax.axis('equal')
        pie_chart.canvas.draw()
        window.destroy()
        update_main_button(app)

    else:
        messagebox.showwarning(copy.warning_box, copy.warnings['empty_pie'])
        name.focus()

def create_new_cat(master, app, button):
        """Create a new tally category."""
        # Checks category space and name eligibility, then opens a new window
        if len(app.cats) >= 6:
            messagebox.showwarning(copy.warning_box, copy.warnings['too_many_cats'])
            return

        elif hasattr(master, "cat_name_entry") and master.cat_name_entry.winfo_exists():
            master.cat_name_entry.focus()
            return

        else: 
            open_cat_window(master, app, button)


def open_cat_window(master, app, button):
    """Open a new window for users to input the name of a new tally category."""
    new_cat_window = tk.Toplevel(master)

    # Entry field
    cat_name_entry = tk.Entry(new_cat_window)
    master.cat_name_entry = cat_name_entry
    cat_name_entry.pack(padx=10, pady=10)
    cat_name_entry.focus()

    # Submit button
    submit_cat = lambda event=None: submit_new_cat(
        master, app, name=cat_name_entry, window=new_cat_window)
    submit_button = button(
        new_cat_window, text=copy.buttons['submit_cat'], command=submit_cat)
    submit_button.pack(pady=5)

    # Key binds
    new_cat_window.bind(
        shortcuts.binds['submit'], submit_cat)
    new_cat_window.bind(
        shortcuts.binds['cancel'], lambda event: new_cat_window.destroy())


def submit_new_cat(master, app, name, window, event=None):
    """Submit a newly created category from the new category window."""
    new_cat_name = name.get()
    if new_cat_name != "":
        if all(cat.cat_name != new_cat_name for cat in app.cats):
            new_cat = Cat(master, app)
            new_cat.cat_name = new_cat_name
            app.cats.append(new_cat)
            new_cat.label.config(text=new_cat_name)
            window.destroy()
            update_new_cat_button(app)
        else:
            messagebox.showwarning(copy.warning_box, copy.warnings['repeated_cat'])
            name.focus()
    else:
        messagebox.showwarning(copy.warning_box, copy.warnings['empty_cat'])
        name.focus()


def delete_cat(self, cat):
    """Delete a tally category."""
    app = self.cat.app
    self.cat.frame.destroy()
    app.cats.remove(self.cat)
    update_new_cat_button(app)
    update_pie_chart(app)
    if len(app.cats) == 0:
        pie_chart = app.pie_chart
        pie_chart.ax.clear()
        pie_chart.title = ''
        pie_chart.ax.set_title(pie_chart.title)
        pie_chart.ax.pie(pie_chart.sizes, labels=pie_chart.labels, autopct='', startangle=90)
        pie_chart.ax.axis('equal')
        pie_chart.canvas.draw()
        update_main_button(app)



# WIDGET METHODS
def create_main_button(app):
    """Choose the main button on the app's startup."""
    app.new_cat_button.grid_forget()
    app.new_pie_button.grid(row=2, column=0)

def update_main_button(app):
    """Determine which button should be shown below the pie chart."""
    if app.pie_chart.title:
        app.new_pie_button.grid_forget()
        app.new_cat_button.grid(row=2, column=0)
    else:
        app.new_cat_button.grid_forget()
        app.new_pie_button.grid(row=2, column=0)

def update_new_cat_button(app):
    """Set the visibility of the new_cat button."""
    if len(app.cats) >= 6:
        app.new_cat_button.grid_forget()
    else:
        app.new_cat_button.grid(row=2, column=0)


def update_pie_chart(app):
    """Update the pie chart each time a category is tallied up or down."""
    recalculate_total_tally(app)
    recalculate_tally_percentages(app)
    redraw_pie_chart(app)
    update_main_button(app)


def recalculate_total_tally(app):
    """Update the total tally of the app."""
    app.total_tally = sum(cat.tally for cat in app.cats)
    app.total_tally_label.config(text=f"{copy.total_tally} {app.total_tally}")


def recalculate_tally_percentages(app):
    """Update the tally percentages of all category."""
    if app.total_tally != 0:
        for cat in app.cats:
            cat.tally_percent = 100 * (cat.tally / app.total_tally)


def redraw_pie_chart(app):
    """Redraw the pie chart each time a category is tallied up or down."""
    pie_chart = app.pie_chart
    title = pie_chart.title
    pie_chart_labels = []
    pie_chart_sizes = []
    
    # Reset pie chart
    if app.total_tally == 0:
        pie_chart.ax.clear()
        pie_chart.ax.set_title(title)
        pie_chart.ax.pie(pie_chart.sizes, labels=pie_chart.labels, autopct='', startangle=90)
        pie_chart.ax.axis('equal')
        pie_chart.canvas.draw()
        return

    # Redraw pie chart
    for cat in app.cats:
        if cat.tally != 0:
            pie_chart_labels.append(cat.cat_name)
            pie_chart_sizes.append(cat.tally_percent)

    pie_chart.ax.clear()
    if app.cats:
        pie_chart.ax.pie(
            pie_chart_sizes, labels=pie_chart_labels, autopct='%1.1f%%', startangle=90)
    else:
        pie_chart.ax.pie(
            pie_chart.sizes, labels=pie_chart.labels, autopct='', startangle=90)
    pie_chart.ax.axis('equal')
    pie_chart.ax.set_title(title)
    pie_chart.canvas.draw()



# FILE MANAGEMENT METHODS

def save_snapshot(data, filename=None):
    """Save session data to a JSON file."""
    if data:
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
    
    else:
        messagebox.showwarning(copy.warning_box, copy.warnings['no_data'])


def load_snapshot(app):
    """Open a file dialog to choose a file to load."""
    filename = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")],
        title="Select a file to open"
    )
    if filename:
        load_file(filename, app)
        update_pie_chart(app)
        update_main_button(app)


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
        for cat_data in data:
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
        messagebox.showerror(copy.error_box, copy.errors['not_found'])
        return None
    except json.JSONDecodeError:
        messagebox.showerror(copy.error_box, copy.errors['not_json'])
        return None


# HELP MENU METHODS

def contribute():
    """Send users to the app's GitHub repository."""
    confirmation = messagebox.askyesno(
        copy.contribute['contribute'], copy.contribute['confirmation'])
    if confirmation:
        webbrowser.open_new(hyperlinks.github_repo)


def about():
    """Open a new window to inform users about Tally Pie."""
    line_break = '\n'
    about_message = ''
    values = list(copy.info.values())
    for i, value in enumerate(values):
        if i == len(values) - 1:
            line_content = value
            about_message += line_content
        else:
            line_content = value + line_break
            about_message += line_content
    
    about_window = messagebox.showinfo(copy.info_box, about_message)