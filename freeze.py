import sys
from cx_Freeze import setup, Executable

setup(
    name="Tally Pie",
    version="0.1.0",
    description="Simple app to tally and categorize content with a dynamic pie chart.",
    executables=[Executable("main.py")],
)
