from config import base


total_tally = "Total items:"

menus = {
    'file': 'File',
    'new_pie': 'New',
    'new_cat': 'Add slice',
    'save_pie': 'Save',
    'open_pie': 'Open',
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
    'new_cat': 'Ctrl+L',
    'save_pie': 'Ctrl+S',
    'open_pie': 'Ctrl+O',
    'rename_pie': 'Ctrl+R',
    'erase_pie': 'Ctrl+W',
    'exit': 'Alt+F4',
}

buttons = {
    'new_pie': 'New Pie',
    'new_cat': 'Add Slice',
    'submit_pie': 'Create pie',
    'rename_pie': 'Rename pie',
    'submit_cat': 'Add slice',
    'delete_cat': 'x',
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
    'new_cat': 'Give your new slice a name.',
    'rename_pie': 'Rename the title of your pie chart.',
}

info_box = 'Tally Pie'
info = {
    'about': f'Tally Pie is a {base.app_description.lower()}',
    'uses': 'Tally Pie is great for ad hoc surveys. You can use it to count household objects, poll your friends\' opinions, analyze content on your social media, and much more.',
    'version': f'Version: {base.version_number} (Alpha)',
    'licence': 'Licence: GNU General Public License v3.0',
    'author': 'Developed by Mudpuppy (Ottawa, Canada)',
}

warning_box = 'Oops'
warnings = {
    'empty_pie': 'This pie chart needs a title.',
    'too_long': 'This name cannot exceed 25 characters.',
    'repeated_cat': 'This name is taken by another slice.',
    'empty_cat': 'This slice needs a name.',
    'too_many_cats': 'You can only add up to six slices.',
    'no_data': 'There is no data to save yet. Add some content before saving.',
}

error_box = 'Uh-oh'
errors = {
    'not_found': 'File not found.',
    'not_json': 'Invalid JSON file.',
}