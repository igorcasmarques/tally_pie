import tkinter as tk
from config import commands, shortcuts


def define_key_binds(master, app, event=None):
    """Key binding for the app's shortcuts."""
    key_combos = {
        shortcuts.binds['new_pie']: lambda event: commands.create_new_pie(master, app, tk.Button),
        shortcuts.binds['new_wedge']: lambda event: commands.create_new_wedge(master, app, tk.Button),
        shortcuts.binds['save_pie']: lambda event: commands.save_pie(app.pie_chart.title, app.wedges),
        shortcuts.binds['open_pie']: lambda event: commands.open_pie(master, app, tk.Button),
        shortcuts.binds['rename_pie']: lambda event: commands.rename_pie(master, app, tk.Button),
        shortcuts.binds['erase_pie']: lambda event: commands.erase_pie(app),
    }

    for key_combo, action in key_combos.items():
        master.bind_all(key_combo, action)