app_name = 'Tally Pie'
total_tally = "Total items:"

menus = {
    'file': 'File',
    'new_pie': 'New pie chart',
    'new_cat': 'New category',
    'save_pie': 'Save pie chart...',
    'open_pie': 'Open pie chart...',
    'exit': 'Exit',
    'edit': 'Edit',
    'rename_pie': 'Rename pie chart',
    'erase_pie': 'Erase pie chart',
    'help': 'Help',
    'user_manual': 'User manual',
    'contribute': 'Contribute',
    'about': 'About Tally Pie',
}

accelerators = {
    'new_pie': 'Ctrl+N',
    'new_cat': 'Ctrl+Y',
    'save_pie': 'Ctrl+S',
    'open_pie': 'Ctrl+O',
    'rename_pie': 'Ctrl+R',
    'erase_pie': 'Ctrl+W',
    'exit': 'Alt+F4',
}

buttons = {
    'new_pie': 'New Pie Chart',
    'new_cat': 'New Category',
    'submit_pie': 'Create pie chart',
    'rename_pie': 'Rename pie chart',
    'submit_cat': 'Add category',
    'delete_cat': 'x',
    'plus': '+1',
    'minus': '-1',
}

confirms = {
    'confirm': 'Are you sure?',
    'new_pie': 'Creating a new pie chart will overwrite your current work.\nAre you sure you want to continue?',
    'open_pie': 'Opening a pie chart will overwrite your current work.\nAre you sure you want to continue?',
    'user_manual': 'You\'re being redirected to Tally Pie\'s user manual on the web. \nAre you sure you want to continue?',
    'contribute': 'You\'re being redirected to Tally Pie\'s GitHub repository. \nAre you sure you want to continue?',
    'exit': 'Do you want to save your pie chart before leaving?',
}

info_box = 'Tally Pie'
info = {
    'about': 'Tally Pie is a simple app to tally and categorize content with a dynamic pie chart.',
    'uses': 'You can use Tally Pie to count household objects, poll your friends\' opinions, analyze content on your social media, and much more.',
    'version': 'Version: 0.1.0 (Pre-Alpha)',
    'licence': 'Licence: GNU General Public License v3.0',
    'author': 'Author: Igor Coelho A. S. Marques',
}

warning_box = 'Oops'
warnings = {
    'empty_pie': 'This pie chart needs a title.',
    'no_pie': 'Create a pie first before adding categories.',
    'repeated_cat': 'This name is taken by another category.',
    'empty_cat': 'This category needs a name.',
    'too_many_cats': 'You can only add up to six categories.',
    'no_data': 'There is no data to save yet. Add some content before saving.',
}

error_box = 'Uh-oh'
errors = {
    'not_found': 'File not found.',
    'not_json': 'Invalid JSON file.',
}