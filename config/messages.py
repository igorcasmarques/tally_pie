from tkinter import messagebox
from config import copy

def info_box(content):
    """Inform the user about the app."""
    info = messagebox.showinfo(copy.info_box, content)
    return info

def confirm_box(content):
    """Ask the user for confirmation to execute a command."""
    message = copy.confirms[content] + copy.confirms['are_you_sure']
    confirm = messagebox.askyesno(copy.confirms['confirm'], message)
    return confirm

def warning_box(content):
    """Warn the user why their command did not succeed."""
    warning = messagebox.showwarning(copy.warning_box, copy.warnings[content])
    return warning

def error_box(content):
    """Inform the user that an error has occurred."""
    messagebox.showerror(copy.error_box, copy.errors[content])
    return None