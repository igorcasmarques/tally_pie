import sys
from cx_Freeze import setup, Executable

from config import base

setup(
    name=base.app_name,
    version=base.version_number,
    description=base.app_description,
    executables=[Executable(
                    base.file_name,
                    icon=base.app_icon,
                    target_name=base.target_name,
                    base=base.base,
                )
    ],
    packages=base.package,
    options={'build_exe': base.build_exe_options},
)
