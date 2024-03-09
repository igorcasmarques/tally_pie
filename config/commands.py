from tkinter import filedialog
import json
import webbrowser

from config import dialogs, pie_changes, files, copy, hyperlinks, messages
from widgets import buttons


# FILE MENU

## NEW PIE CHART
def create_new_pie(master, app, button):
        """Create a new pie chart."""
        if app.pie_chart.title:
            confirm = messages.confirm_box('new_pie')
            if confirm:
                dialogs.create_new_pie_dialog(master, app, button)

        # Prevent other windows from opening
        elif hasattr(master, "pie_title_entry") and master.pie_title_entry.winfo_exists():
            master.pie_title_entry.focus()
            return

        else:
            dialogs.create_new_pie_dialog(master, app, button)

## NEW CATEGORY
def create_new_cat(master, app, button):
    """Create a new tally category."""
    if app.pie_chart.title:
        if len(app.cats) >= 6:
            messages.warning_box('too_many_cats')
            return

        elif hasattr(master, "cat_name_entry") and master.cat_name_entry.winfo_exists():
            master.cat_name_entry.focus()
            return

        else: 
            dialogs.create_entry_dialog(master, app, button,
                command=dialogs.submit_new_cat,
                label=copy.box_labels['new_cat'],
                text='submit_cat'
            )
    
    else:
        messages.warning_box('empty_pie')

## SAVE PIE
def save_pie(title, cat_data, filename=None):
    """Save a pie chart to a JSON file."""
    if title and cat_data:
        files.save_file(title, cat_data, filename=None)
    else:
        messages.warning_box('no_data')

## OPEN PIE
def open_pie(master, app, button):
    """Open a file dialog to choose a file to load."""
    if app.pie_chart.title:
        confirm = messages.confirm_box('open_pie')
        if confirm:
            files.load_pie_chart(app)
    else:
        files.load_pie_chart(app)


# EDIT MENU

## RENAME PIE
def rename_pie(master, app, button):
    """Rename an existing pie chart."""
    if app.pie_chart.title:
        dialogs.create_entry_dialog(master, app, button,
            command=pie_changes.change_title,
            label=copy.box_labels['rename_pie'],
            text='rename_pie'
        )
    else:
        create_new_pie(master, app, button)
    
## ERASE PIE
def erase_pie(app):
    """Erase an existing pie chart."""
    confirm = messages.confirm_box('erase_pie')
    if confirm:
        pie_changes.reset_pie(app)
        pie_changes.update_pie_chart(app)


# HELP MENU

## USER MANUAL
def user_manual():
    """Send users to the app's user_manual."""
    confirm = messages.confirm_box('user_manual')
    if confirm:
        webbrowser.open_new(hyperlinks.user_manual)

## CONTRIBUTE
def contribute():
    """Send users to the app's GitHub repository."""
    confirm = messages.confirm_box('contribute')
    if confirm:
        webbrowser.open_new(hyperlinks.github_repo)

## ABOUT
def about():
    """Open a new window to inform users about Tally Pie's current version."""
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
    
    messages.info_box(about_message)


# BUTTONS

## DELETE CATEGORY
def delete_cat(self, cat):
    """Delete a tally category."""
    app = self.cat.app
    self.cat.frame.destroy()
    app.cats.remove(self.cat)
    buttons.update_new_cat_button(app)
    pie_changes.update_pie_chart(app)
    if len(app.cats) == 0:
        pie_changes.reset_pie(app)
        buttons.update_main_button(app)
