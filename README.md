####os — Commands / Functions
import os

os.getcwd()                  # Current directory

os.listdir()                 # List files and folders

os.mkdir("test_folder")      # Create a folder

os.makedirs("a/b")            # Create nested folders

os.path.exists("main.py")    # Check path exists

os.path.isfile("main.py")    # Check file

os.path.isdir("test_folder") # Check folder

os.path.join("data", "a.txt") # Join paths

os.remove("a.txt")           # Delete a file

os.rmdir("test_folder")      # Delete empty folder



### sys — Commands / Attributes

import sys

sys.version       # Python version

sys.executable    # Python interpreter path

sys.argv          # Command-line arguments

sys.path          # Module search paths

sys.platform      # Operating system platform

sys.exit()        # Exit the program


###venv — Terminal commands

--python -m venv .venv

Create virtual environment

--.\.venv\Scripts\Activate.ps1

Activate in Windows PowerShell

--deactivate

Deactivate environment

--.\.venv\Scripts\python.exe --version

Check the environment's Python version without activating it.

### pip — Terminal commands

--python -m pip --version

Check pip version

--python -m pip install requests

Install a package.

--python -m pip list

List installed packages.

--python -m pip show requests

Show package details.

--python -m pip install --upgrade requests

Upgrade a package.

--python -m pip uninstall requests

Uninstall a package.

--python -m pip freeze

List installed packages with versions.


###requirements.txt — Commands

--python -m pip freeze > requirements.txt

Create/update the file with installed package versions.

--python -m pip install -r requirements.txt

Install all dependencies listed in the file.





