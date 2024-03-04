from config import shortcuts

def define_key_binds(master, app, event=None):
    """Key binding for the app's shortcuts."""
    key_combos = {
        shortcuts.binds['new_cat']: lambda event: app.file_menu.new_cat(),
        shortcuts.binds['save_snapshot']: lambda event: app.file_menu.save_snapshot(),
        shortcuts.binds['load_snapshot']: lambda event: app.file_menu.load_snapshot(),
    }

    for key_combo, action in key_combos.items():
        master.bind_all(key_combo, action)