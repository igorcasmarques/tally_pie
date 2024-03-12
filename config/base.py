app_name = 'Tally Pie'
package = ['tally_pie']
version_number = '0.1.0'
app_description = 'Simple app to count and categorize content with a dynamic pie chart.'
file_name = "app.py"
app_icon = "assets/app_icon.ico"
target_name = "tally_pie.exe"
base = "Win32GUI"

additional_files = [
    ('assets'),
]

build_exe_options = {
    'packages': [],
    'excludes': ['fontTools', 'jedi', 'jinja2', 'markupsafe', 'nbformat', 'parso', 'prompt_toolkit'],
    'include_files': additional_files,
}