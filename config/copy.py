from config import base


total_count = "Total count:"

menus = {
    'file': 'File',
    'new_pie': 'New',
    'new_wedge': 'Add wedge',
    'save_pie': 'Save',
    'open_pie': 'Open',
    'export_pie': 'Export',
    'exit': 'Exit',
    'edit': 'Edit',
    'rename_pie': 'Rename pie',
    'erase_pie': 'Erase pie',
    'help': 'Help',
    'user_guide': 'User guide',
    'about': 'About',
}

accelerators = {
    'new_pie': 'Ctrl+N',
    'new_wedge': 'Ctrl+L',
    'save_pie': 'Ctrl+S',
    'open_pie': 'Ctrl+O',
    'export_pie': 'Ctrl+E',
    'rename_pie': 'Ctrl+R',
    'erase_pie': 'Ctrl+W',
    'exit': 'Alt+F4',
}

buttons = {
    'new_pie': 'New Pie',
    'new_wedge': 'Add Wedge',
    'submit_pie': 'Create pie',
    'rename_pie': 'Rename pie',
    'submit_wedge': 'Add wedge',
    'delete_wedge': 'x',
    'plus': '+1',
    'minus': '-1',
}

confirms = {
    'confirm': 'Are you sure?',
    'are_you_sure': '\nAre you sure you want to continue?',
    'new_pie': 'Creating a new pie chart will overwrite your current work.',
    'open_pie': 'Opening a pie chart will overwrite your current work.',
    'erase_pie': 'This will erase your pie chart.',
    'user_guide': 'You\'re being redirected to Tally Pie\'s user guide on the web.',
    'exit': 'Do you want to save your pie chart before leaving?',
}

box_labels = {
    'max_length': '\nMax. length: 25 characters',
    'new_pie': 'Give your new pie chart a title.',
    'new_wedge': 'Give your new wedge a name.',
    'rename_pie': 'Rename the title of your pie chart.',
}

info_box = 'Tally Pie'
info = {
    'about': f'Tally Pie is a {base.app_description.lower()}',
    'uses': 'Tally Pie is great for ad hoc surveys. You can use it to count household objects, poll your friends\' opinions, analyze content on your social media, and much more.',
    'version': f'Version: {base.version_number} (Alpha)',
    'licence': 'Licence: GNU General Public License v3.0',
    'author': 'Developed by Mudpuppy (Ottawa, Canada)',
    'export_successful': 'The chart was exported successfully.',
}

warning_box = 'Oops'
warnings = {
    'empty_pie': 'This pie chart needs a title.',
    'too_long': 'This name cannot exceed 25 characters.',
    'repeated_wedge': 'This name is taken by another wedge.',
    'empty_wedge': 'This wedge needs a name.',
    'too_many_wedges': 'You can only add up to six wedges.',
    'no_data': 'There is no data to save yet. Add some content before saving.',
    'no_export': 'There is no data to export yet. Add some content before exporting.',
}

error_box = 'Uh-oh'
errors = {
    'not_found': 'File not found.',
    'invalid_json': 'Invalid JSON file.',
    'duplicate_wedges': 'Duplicate wedge names found.',
    'export_fail': 'Something went wrong. Chart export failed.',
}

def value_error_message(field_name, data_type):
    """Generate an error message for invalid JSON files."""
    return f"Invalid or missing '{field_name}' key in loaded data: Expecting a {data_type.__name__}."