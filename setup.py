import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["PyQt5", "bson", "pymongo", "sys"],
    "include_files": ["UI/", "C:\\Users\\Иван\\Downloads\\onlinepharmacycheck.ico"],  # Укажите путь к вашему UI и иконке
    "excludes": ["tkinter"],
    "include_msvcr": True,
}

base = None
if sys.platform == "win64":
    base = "Win64GUI"

executables = [Executable("C:\\Users\\Иван\\Documents\\GitHub\\kyrsovyaya\\main.py", base=base, icon="C:\\Users\\Иван\\Downloads\\onlinepharmacycheck.ico")]

setup(
    name="Helsi2.0",
    version="1.0",
    description="Description of your app",
    options={"build_exe": build_exe_options},
    executables=executables,
)
